import json

# 此类会被跑分服务器继承， 可以在类中自由添加自己的prompt构建逻辑, 除了parse_table 和 run_inference_llm 两个方法不可改动
# 注意千万不可修改类名和下面已提供的三个函数名称和参数， 这三个函数都会被跑分服务器调用
class submission():
    def __init__(self, table_meta_path):
        self.table_meta_path = table_meta_path
        self.is_log = False

    # 此函数不可改动, 与跑分服务器端逻辑一致， 返回值 grouped_by_db_id 是数据库的元数据（包含所有验证测试集用到的数据库）
    # 请不要对此函数做任何改动
    def parse_table(self, table_meta_path):
        with open(table_meta_path,'r') as db_meta:
            db_meta_info = json.load(db_meta)
        # 创建一个空字典来存储根据 db_id 分类的数据
        grouped_by_db_id = {}

        # 遍历列表中的每个字典
        for item in db_meta_info:
            # 获取当前字典的 db_id
            db_id = item['db_id']
            
            # 如果 db_id 已存在于字典中，将当前字典追加到对应的列表
            if db_id in grouped_by_db_id:
                grouped_by_db_id[db_id].append(item)
            # 如果 db_id 不在字典中，为这个 db_id 创建一个新列表
            else:
                grouped_by_db_id[db_id] = [item]
        return grouped_by_db_id

    # 此为选手主要改动的逻辑， 此函数会被跑分服务器调用，用来构造最终输出给模型的prompt， 并对模型回复进行打分。
    # 当前提供了一个最基础的prompt模版， 选手需要对其进行改进
    def construct_prompt(self, current_user_question):

        question_type = current_user_question['question_type']

        if question_type == 'text2sql':
            system_prompt, user_prompt = self.text2sql(current_user_question)
        elif question_type == 'multiple_choice':
            system_prompt, user_prompt = self.multiple_choice(current_user_question)
        elif question_type == 'true_false_question':
            system_prompt, user_prompt = self.true_false_question(current_user_question)

        else:
            system_prompt = "你是一个数据库专家"
            user_prompt = current_user_question['user_question']

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        self.log(messages)
        return messages

    # 此方法会被跑分服务器调用， messages 选手的 construct_prompt() 返回的结果
    # 请不要对此函数做任何改动
    def run_inference_llm(self, messages):
        pass

    def transform_dict(self, dictionary):
        transformed_dict = {}

        # Transform table names
        table_names = dictionary.get('table_names_original', [])
        transformed_dict['table_names'] = table_names

        # Transform column names
        column_names_original = dictionary.get('column_names_original', [])
        column_names_dict = {}
        for index, name in column_names_original:
            if index not in column_names_dict:
                column_names_dict[index] = []
            column_names_dict[index].append(name)

        transformed_dict['column_names'] = column_names_dict

        # Transform foreign keys
        foreign_keys = dictionary.get('foreign_keys', [])
        transformed_dict['foreign_keys'] = foreign_keys

        # Transform primary keys
        primary_keys = dictionary.get('primary_keys', [])
        transformed_dict['primary_keys'] = primary_keys

        return transformed_dict

    def text2sql(self, current_user_question):
        '''
        文本到 sql 转化
        :param cur_db_info: 数据库格式信息
        :param user_question: 用户问题
        :return: 提示词
        '''
        system_prompt = (
            "【你只能说英语  你只能输出SQL语句  你的任何额外的输出都会导致命性错误】"
            "【你只能输出SQL语句  你不要输出任何解释  你的任何非SQL语句输出都会造成灾难性后果】"
        )

        user_question = current_user_question['user_question']
        current_db_id = current_user_question['db_id']
        cur_db_info = self.parse_table(self.table_meta_path)[current_db_id]

        try:
            transformed_dict = self.transform_dict(cur_db_info[0])
        except Exception as e:
            transformed_dict = "参考数据库信息"
        else:
            pass

        if len(cur_db_info[0]) > 1000:
            transformed_dict = "参考数据库信息"

        user_prompt = (
            f"【转化之后的描述为SQL语句 {user_question}】"
            f"【数据库信息 {cur_db_info[0]}】"
            # f"【解析的数据库信息 {transformed_dict}】"
            f"【你只能说英语  你只能输出SQL语句  你的任何额外的输出都会导致命性错误】"
            f"【你只能输出SQL语句  你不要输出任何解释  你的任何非SQL语句输出都会造成灾难性后果】"
        )
        return system_prompt, user_prompt

    def multiple_choice(self, info):
        '''
        多选题
        :param user_question:
        :param options:
        :return:
        '''
        system_prompt = (
            "【你回答我之后给你的选择题  你的输出被我的程序直接捕获  它只能识别 A B C D  你的任何额外的输出都会导致命性错误】"
        )

        question = info['user_question']
        user_prompt = (
            f"【问题：{question}？（仅输出选项前的字母，如 A、B、C、D）】\r"
            f"【A {info['optionA']}  "
            f"B {info['optionB']}  "
            f"C {info['optionC']}  "
            f"D {info['optionD']}】 \r"
            f"【请仅输出选项前的字母 任何额外的输出都会导致命性错误】"
        )

        return system_prompt, user_prompt

    def true_false_question(self, current_user_question):
        '''
        判断题
        :param user_question:
        :return:
        '''
        system_prompt = (
            "请仅输出 True 或 False 你的任何额外的输出(例如 .)都会导致命性错误"
        )

        user_question = current_user_question['user_question']

        user_prompt = (
            f"【判断题 {user_question}】"
            f"【请仅输出 True 或 False 任何额外的输出都会导致命性错误】"
        )
        return system_prompt, user_prompt

    def log(self, x, path="../log/"):
        import logging, os
        from datetime import datetime
        if not os.path.exists(path):
            os.makedirs(path)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f"{path}{timestamp}.log"

        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            encoding='utf-8',
        )

        # 写入日志
        logging.info(x)



