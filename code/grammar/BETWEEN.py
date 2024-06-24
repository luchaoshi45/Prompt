# 定义 BETWEEN 操作符的相关知识
BETWEEN = {
    "description": "The BETWEEN operator in SQL is used to filter the result set within a specified range of values.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name"
                 + " WHERE column_name BETWEEN value1 AND value2;"
    },
    "examples": [
        {
            "example_description": "Selecting products with a price between $10 and $50",
            "sql_query": "SELECT * FROM products WHERE price BETWEEN 10 AND 50;"
        },
        {
            "example_description": "Selecting orders placed between two dates",
            "sql_query": "SELECT * FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';"
        },
        {
            "example_description": "Selecting employees with a salary between $50000 and $80000",
            "sql_query": "SELECT * FROM employees WHERE salary BETWEEN 50000 AND 80000;"
        }
    ]
}