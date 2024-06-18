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
system_prompt = "你是一个数据库专家, 你只能回答可以直接执行的SQL语句，不要输出其他内容，比如输出 SELECT * FROM User。"
```
##### 用户提示词：
```python
user_prompt = (f"我有一个SQL数据库，"
               f"其具体格式为：{cur_db_info}，"
               f"我想要查询：{user_question}，"
               f"请根据上述提供的信息，生成正确运行的SQL语句。"
               f"请注意，只需要输出SQL语句，不要输出其他内容。")
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
system_prompt = "你是一个SQL数据库专家，你只能回答 A B C D 其中的一个。"
```
##### 用户提示词：
```python
user_prompt = (f"我有一个关于SQL数据库的单项选择题，"
               f"其题目为：{user_question}，"
               f"选项为：{options}，"
               f"请给出正确的选项。"
               f"请注意，你只能回答 A B C D 其中的一个，不要输出其他内容。")
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
system_prompt = "你是一个SQL数据库专家， 你只能回答问题真伪(True/False)。"
```
##### 用户提示词：
```python
user_prompt = (f"我有一个判断题，"
               f"其题目为：{user_question}"
               f"请判断问题真伪(True/False)。"
               f"请注意，只需要输出正确选项的判断结果，不要输出其他内容。")
```


