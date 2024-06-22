import openai

from submit import submission
import json
from openai import OpenAI
import requests

# 本代码为测试用例，选手可自己调用本地大语言模型接口进行测试，具体的格式为OpenAI格式的接口形式
# openai_api_key = "sk-b4MHQYUadvMtIqax6uRMKEUSwwYd50QbJyxTfZOIGwmxxE3U"  #请参照openai api使用文档，按照实际填写
# openai_api_base = "https://api.chatanywhere.tech/v1"
# openai = OpenAI(api_key=openai_api_key, base_url=openai_api_base)

openai.api_key = 'sk-TA1eIqqydtm1695499D7795bB64b4f0180B0B222A425E83e'
openai.base_url = "https://free.gpt.ge/v1/"
openai.default_headers = {"x-foo": "true"}

# 代理运行在 7890 端口
import os
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# 评估哪类问题
EVAL = ['text2sql', 'multiple_choice', 'true_false_question']
# EVAL = ['text2sql']
# EVAL = ['multiple_choice']
# EVAL = ['true_false_question']

def evaluate_mcq(predicted_answer, label):
    return predicted_answer.upper().strip() == label.upper().strip()

def evaluate_sql(predicted_answer, label):
    system_prompt = "判断答案1和答案2执行结果否一致  你的输出被我的程序直接捕获  它只能识别 True False  你的任何额外的输出都会导致命性错误"
    user_prompt = (
        f"答案1:{predicted_answer}\n"
        f"答案2：{label}\n"
        f"只 True False 任何额外的输出都会导致命性错误"
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_response = openai.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",  # 这里填写所选择的LLM名称，推荐使用Qwen1.5-14B-Chat模型进行线下开发评估
        max_tokens=2048,
        temperature=0.0,  # temperature 实际跑分时默认设置为0.0，避免随机性
        stream=False
    )
    llm_outputs = llm_response.choices[0].message.content
    if "True" in llm_outputs or "执行结果是一致的" in llm_outputs or "执行结果一致" in llm_outputs:
        return True
    else:
        print(llm_outputs)
        return False




class eval_submission(submission):
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

    def run_inference_llm(self, constructed_prompts):
        if isinstance(constructed_prompts, str):
            pass
        elif isinstance(constructed_prompts, list):
            pass
        elif isinstance(constructed_prompts, dict):
            pass
        messages = constructed_prompts
        # print(f"调用模型进行测试,用户的prompt为：{constructed_prompts}")
        llm_response = openai.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",  # 这里填写所选择的LLM名称，推荐使用Qwen1.5-14B-Chat模型进行线下开发评估
            max_tokens=2048,
            temperature= 0.0,           #  temperature 实际跑分时默认设置为0.0，避免随机性
            stream=False  
        )
        llm_outputs = llm_response.choices[0].message.content
        return llm_outputs

if __name__ == "__main__":
    user_submission = eval_submission(table_meta_path ="样例数据/sample_tables.json")
    question_jsonl_filename = "样例数据/sample_question.jsonl"
    gt_jsonl_filename = "样例数据/sample_answer.jsonl"
    answer_dict = {}

    num_questions, num_correct_answer = 0, 0
    with open(gt_jsonl_filename, 'r', encoding='utf-8') as gt_file:
        for line in gt_file:
            data = json.loads(line)
            answer_dict[data['question_id']]=data['answer']

    with open(question_jsonl_filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = json.loads(line)
            if data['question_type'] not in EVAL:
                continue

            message = user_submission.construct_prompt(data)
            response = user_submission.run_inference_llm(message)
            question_id = data['question_id']
            question_type = data['question_type']

            user_submission.log(response)
            user_submission.log(answer_dict[question_id])


            if question_type == "text2sql":
                db_name = data['db_id']
                label = answer_dict[question_id]
                judge_result = evaluate_sql(response, label)

            if question_type == "multiple_choice":
                label = answer_dict[question_id]
                judge_result = evaluate_mcq(response, label)

            if question_type == "true_false_question":
                label = answer_dict[question_id]
                judge_result = evaluate_mcq(response, label)

            num_questions += 1
            if judge_result:
                print("right")
                num_correct_answer += 1
            else:
                print("error")
            print(f"Dynamic accuracy:{num_correct_answer / num_questions}")

            user_submission.log(f"Dynamic accuracy:{num_correct_answer / num_questions}")
            user_submission.log(100 * "-")
            user_submission.log(100 * "-")
            user_submission.log(100 * "-")
            user_submission.log(100 * "-")
    print(f"Accuracy:{num_correct_answer/num_questions}")