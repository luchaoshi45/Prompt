import os
from openai import OpenAI
# 代理运行在 7890 端口
import os
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

# client = OpenAI(
#     api_key="9e1d9ed8bb2b4931aab234e9545d42af",
#     base_url="https://api.aimlapi.com",
# )
client = OpenAI(
    api_key="sk-0738f7176f0a44e8ae8bc1569c2b6032",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen1.5-14b-chat",
    messages=[
        {
            "role": "system",
            "content": "你是AI助手",
        },
        {
            "role": "user",
            "content": "你好"
        },
    ],
)

message = response.choices[0].message.content
print(f"Assistant: {message}")



# # -*- coding: utf-8 -*-
# from http import HTTPStatus
# import dashscope
# dashscope.api_key = "sk-0738f7176f0a44e8ae8bc1569c2b6032"
#
# message = "你好"
#
# response = dashscope.Generation.call(
#     model='qwen1.5-14b-chat',
#     prompt=message,
#     result_format='message',
#     max_tokens=2000,
#     temperature=0.0,
#     stream=False
# )
# if response.status_code == HTTPStatus.OK:
#     print(response)
# else:
#     print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
#         response.request_id, response.status_code,
#         response.code, response.message
#     ))