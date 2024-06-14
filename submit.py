import json

# 此类会被跑分服务器继承， 可以在类中自由添加自己的prompt构建逻辑, 除了parse_table 和 run_inference_llm 两个方法不可改动
# 注意千万不可修改类名和下面已提供的三个函数名称和参数， 这三个函数都会被跑分服务器调用
class submission():
    def __init__(self, table_meta_path):
        self.table_meta_path = table_meta_path

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
        user_question = current_user_question['user_question']
        system_prompt = "你是一个数据库专家"
        if question_type == 'text2sql':
            current_db_id = current_user_question['db_id']
            cur_db_info = self.parse_table(self.table_meta_path)[current_db_id]
            user_prompt = f"我有一个数据库，其具体格式为：{cur_db_info}，我想要查询：{user_question},请根据上述提供的信息，生成正确运行的SQL语句。请注意，只需要输出SQL语句，不要输出其他内容。"
        elif question_type == 'multiple_choice':
            options = "A." + current_user_question['optionA'] + "B." + current_user_question['optionB']+ "C." + current_user_question['optionC']+ "D." + current_user_question['optionD']
            user_prompt = f"我有一个单项选择题，其题目为:{user_question}，选项为：{options}，请给出正确的选项。请注意，只需要输出正确选项的字母，不要输出其他内容。"
        elif question_type == 'true_false_question':
            user_prompt = f"我有一个判断题，其题目为:{user_question}，请判断问题真伪(True/False)。请注意，只需要输出正确选项的判断结果，不要输出其他内容。"

        messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
        ]
        return messages

    # 此方法会被跑分服务器调用， messages 选手的 construct_prompt() 返回的结果
    # 请不要对此函数做任何改动
    def run_inference_llm(self, messages):
        pass