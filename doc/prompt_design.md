# 提示词设计 ✨
## 一、文本到SQL语句 🧑‍💻
### 分析
本题通过验证SQL语句在数据库的执行结果，判断题目是否回答正确。
```markdown
1.让大模型充分了解用户的数据库结构
2.根据问题产生可以执行的SQL语句
3.system_prompt给出样例结果
4.user_prompt 强调只需要输出SQL语句，不要输出其他内容
```
### Prompt
#### 系统提示词：
```python
system_prompt = (
    "你是SQL数据库专家，你回答我之后给你的文本到SQL语句转换题，"
    "你的输出会被我后端的服务器程序直接捕获，"
    "它通过运行捕获的结果，判断你的回答是否正确，"
    "如果包含任何额外字符或文字，导致SQL执行错误，仍然判定为错误。"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"问题: {user_question} \n"
    f"数据库信息: {cur_db_info}\n"
    f"给我最简洁的输出"
)
```

## 二、单项选择题 🔠
### 分析
```markdown
本题通过验证SQL语句在数据库的执行结果，判断题目是否回答正确。
1.让大模型充分了解问题
2.system_prompt 限定你只能回答 A B C D 其中的一个
3.user_prompt 强调你只能回答 A B C D 其中的一个，不要输出其他内容
```
### Prompt
#### 系统提示词：
```python
system_prompt = (
    "你是SQL数据库专家，你回答我之后给你的单选题，"
    "你的输出会被我后端的服务器程序直接捕获，"
    "它只能识别 A B C D，并且它只能捕获一个字符。"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"项选题:{user_question} \n"
    f"选项为：{options} \n"
    f"给我最简洁的输出"
)
```


## 三、判断题 ✅
### 分析
```markdown
本题通过验证SQL语句在数据库的执行结果，判断题目是否回答正确。
1.让大模型充分了解问题
2.system_prompt 限定你只能回答问题真伪(True/False)
3.user_prompt 强调你只能回答 A B C D 其中的一个，不要输出其他内容
```
### Prompt
#### 系统提示词：
```python
system_prompt = (
    "你是SQL数据库专家，你回答我之后给你的判断题，"
    "你的输出会被我后端的服务器程序直接捕获，"
    "它只能识别 True False。"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"判断题：{user_question}"
    f"给我最简洁的输出"
)
```


