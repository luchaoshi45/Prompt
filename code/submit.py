import json

# 此类会被跑分服务器继承， 可以在类中自由添加自己的prompt构建逻辑, 除了parse_table 和 run_inference_llm 两个方法不可改动
# 注意千万不可修改类名和下面已提供的三个函数名称和参数， 这三个函数都会被跑分服务器调用
class submission():
    def __init__(self, table_meta_path):
        self.table_meta_path = table_meta_path
        self.is_log = False
        self.db_metadata = self.parse_table(table_meta_path)

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

    def get_db_description(self, db_id):
        cur_db_info = self.db_metadata.get(db_id, [])
        cur_db_info = cur_db_info[0]
        return str(cur_db_info)

    def text2sql(self, current_user_question):
        context = "你是一个数据库专家，需要帮助用户查询一个SQL数据库。"
        objective = "生成一个正确的SQL查询语句，以便用户能够从数据库中获取所需的信息。"
        action = "阅读用户的问题，并基于提供的数据库格式信息生成SQL查询语句。"
        support = (
            "数据库的具体格式如下：\n"
            f"{self.get_db_description(current_user_question['db_id'])}\n"
        )
        technology = "请只输出可直接执行的SQL查询语句，不要输出任何额外内容。"

        system_prompt = (
            f"{context}\n\n"
            f"{objective}\n\n"
            f"{action}\n\n"
            f"{support}\n\n"
            f"{technology}"
        )

        user_prompt = current_user_question['user_question']
        return system_prompt, user_prompt

    def multiple_choice(self, current_user_question):
        system_prompt = "你在帮我做SQL选择题目，你的回答必须简洁，因为我只认识 A B C D，所以你只能输出 A B C D。"

        context = (
            f"用户的问题是：{current_user_question['user_question']}。\n"
            "选项如下：\n"
            f"A. {current_user_question['optionA']}；\n"
            f"B. {current_user_question['optionB']}；\n"
            f"C. {current_user_question['optionC']}；\n"
            f"D. {current_user_question['optionD']}"
        )

        objective = "输出 A B C D 其中一个。"
        action = "阅读用户的问题及选项，做出认真合理的分析。"
        support = "这些题目往往都是计算机专业的工作的面试题目，你可以参考相关的场景。"
        technology = "mysql 数据库的知识。"

        user_prompt = (
            f"{context}\n\n"
            f"{objective}\n\n"
            f"{action}\n\n"
            f"{support}\n\n"
            f"{technology}"
        )

        return system_prompt, user_prompt

    def true_false_question(self, current_user_question):
        context = "你是一个SQL数据库专家，需要帮助用户判断一个关于SQL数据库的命题真伪。"
        objective = "判断命题的真伪，以便用户能够了解其准确性。"
        action = "阅读用户的问题，并判断其是真还是假。"
        support = f"用户的问题是：{current_user_question['user_question']}"
        technology = "请只输出 True 或 False，不要输出任何额外内容。"

        system_prompt = (
            f"{context}\n\n"
            f"{objective}\n\n"
            f"{action}\n\n"
            f"{support}\n\n"
            f"{technology}"
        )

        user_prompt = current_user_question['user_question']
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
