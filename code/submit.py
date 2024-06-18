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

        # self.log(messages)
        return messages

    # 此方法会被跑分服务器调用， messages 选手的 construct_prompt() 返回的结果
    # 请不要对此函数做任何改动
    def run_inference_llm(self, messages):
        pass

    def text2sql(self, current_user_question):
        '''
        文本到 sql 转化
        :param cur_db_info: 数据库格式信息
        :param user_question: 用户问题
        :return: 提示词
        '''
        system_prompt = "你是一个数据库专家, 你只能回答可以直接执行的SQL语句，不要输出其他内容，比如输出 SELECT * FROM User。"

        user_question = current_user_question['user_question']
        current_db_id = current_user_question['db_id']
        cur_db_info = self.parse_table(self.table_meta_path)[current_db_id]

        user_prompt = (f"我有一个SQL数据库，"
                       f"其具体格式为：{cur_db_info}，"
                       f"我想要查询：{user_question}，"
                       f"请根据上述提供的信息，生成正确运行的SQL语句。"
                       f"请注意，只需要输出SQL语句，不要输出其他内容。")
        return system_prompt, user_prompt

    def multiple_choice(self, current_user_question):
        '''
        多选题
        :param user_question:
        :param options:
        :return:
        '''
        system_prompt = "你是一个SQL数据库专家，你只能回答 A B C D 其中的一个。"

        user_question = current_user_question['user_question']
        options = ("A." + current_user_question['optionA'] + '；'
                   + "B." + current_user_question['optionB'] + '；'
                   + "C." + current_user_question['optionC'] + '；'
                   + "D." + current_user_question['optionD'])

        user_prompt = (f"我有一个关于SQL数据库的单项选择题，"
                       f"其题目为：{user_question}，"
                       f"选项为：{options}，"
                       f"请给出正确的选项。"
                       f"请注意，你只能回答 A B C D 其中的一个，不要输出其他内容。")
        return system_prompt, user_prompt

    def true_false_question(self, current_user_question):
        '''
        判断题
        :param user_question:
        :return:
        '''
        system_prompt = "你是一个SQL数据库专家， 你只能回答问题真伪(True/False)。"

        user_question = current_user_question['user_question']
        user_prompt = (f"我有一个判断题，"
                       f"其题目为：{user_question}"
                       f"请判断问题真伪(True/False)。"
                       f"请注意，只需要输出正确选项的判断结果，不要输出其他内容。")
        return system_prompt, user_prompt

    def log(self, x, path="recode.log"):
        import logging, os
        if not self.is_log:
            self.is_log = True
            if os.path.exists(path):
                os.remove(path)

        logging.basicConfig(
            filename=path,
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            encoding='utf-8',
        )

        # 写入日志
        logging.info(x)
