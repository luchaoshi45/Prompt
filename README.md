# 2024中兴捧月大赛—精言妙喻 🎇🎇🎇

## 赛题背景
```markdown
随着大模型在各行业的广泛应用，其在各种任务中的应用价值与实际应用效果得到了进一步强化。 
Prompt 是与大模型交互的重要工具，高效的 Prompt 技巧能够精准的表达用户自定义任务的要求和特点，
减少大模型的幻觉，激发大模型的潜力。
```

## 任务简介
```markdown
Prompt，也被称为提示词，是用于向大模型传达任务指令的语句。
Prompt 可以是简单的单个输入,也可以是通过增加额外的上下文或示例的复杂输入。
通过巧妙地调整 Prompt 的表达方式，可以有效地引导模型产生最佳响应。 
选手将基于数据库场景设计个性化的 Prompt，本次比赛共设定三个不同的任务场景:
「Text2SQL」、「数据库通识类单项选择题」和「数据库通识类判断题」。
选手设计的 Prompt 需要同时满足这三个场景的任务要求。
```
## 注意事项
```markdown
本次比赛鼓励选手使用开源模型Qwen1.5-14B-Chat进行开发自测。
为确保比赛公平性,参赛者不得使用基于固定规则的方法直接输出结果。
为了确保参赛者设计的Prompt有效性，请遵循以下规则：
1.Prompt长度不得超过2048个Token。超过该长度的Prompt将被系统自动截断； 
2.构建单个问题Prompt的过程中，调用模型的次数不得超过5次。超过5次的调用将导致该题目直接判为错误。 
参赛者可以利用公开可访问的外部数据集对测试集进行优化Prompt设计。
使用的外部数据资源必须在初赛方案中一并提交。
```

## 构造提示词
```python
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
```

## text2sql🧑‍💻 
```python
# Text2SQL：即将自然语言的查询语句转化成数据库能够执行的sql语言。
def text2sql(self, current_user_question):
```
## 单项选择题🔠
```python
# 数据库通识类选择题：形式为单项选择题。其中，单项选择题有4个选项，仅一个选项是正确的。
def multiple_choice(self, current_user_question):
```
## 判断题✅
```python
# 数据库通识类判断题：形式为判断题。其中，判断题仅需要判断题目的描述是否正确。
def true_false_question(self, current_user_question):
```

## 日志函数📓
```python 
def log(self, x, path="recode.log"):
```