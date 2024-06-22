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
    "您答我之后给你的文本转 SQL 语句题  您的输出将被我的程序直接捕获  它将直接调用 SQL 数据库执行您的输出  您的任何额外的输出都会导致命性错误  "
    "我希望您在回答我之前充当 SQL 终端  首先执行您输出  确保准确无误后在输出给我的程序。"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"【需要转化 SQL 的问题 {user_question}】"
    f"【数据库信息 {cur_db_info[0]}】"
    f"【解析的数据库信息 {transformed_dict}】"
    f"任何额外的输出都会导致命性错误"
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
    "【你回答我之后给你的选择题  你的输出被我的程序直接捕获  它只能识别 A B C D  你的任何额外的输出都会导致命性错误】"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"【问题：{question}？（仅输出选项前的字母，如 A、B、C、D）】\r"
    f"【A {info['optionA']}  "
    f"B {info['optionB']}  "
    f"C {info['optionC']}  "
    f"D {info['optionD']}】 \r"
    f"【请仅输入选项前的字母 任何额外的输出都会导致命性错误】"
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
    "你回答我之后给你的判断题  你的输出被我的程序直接捕获  它只能识别 True False  你的任何额外的输出都会导致命性错误"
)
```
##### 用户提示词：
```python
user_prompt = (
    f"【判断 {user_question}】"
    f"分析关键词  回答 True False  任何额外的输出都会导致命性错误"
)
```


