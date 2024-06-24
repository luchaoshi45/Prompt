# 定义 SQL AND 操作符的相关知识
AND = {
    "description": "The AND operator in SQL is used to combine multiple conditions in a WHERE clause. "
                   "It requires that all specified conditions must be true for the record to be included in the result set.",
    "usage": "Syntax: condition1 AND condition2",
    "examples": [
        {
            "example_description": "Selecting employees with salary greater than 50000 and in the 'IT' department",
            "sql_query": "SELECT * FROM employees WHERE salary > 50000 AND department = 'IT';"
        },
        {
            "example_description": "Selecting orders placed by customer 'John Doe' and with total amount over 1000",
            "sql_query": "SELECT * FROM orders WHERE customer_name = 'John Doe' AND total_amount > 1000;"
        }
    ]
}