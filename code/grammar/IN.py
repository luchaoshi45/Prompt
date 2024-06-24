# 定义 IN 操作符的相关知识
IN = {
    "description": "The IN operator in SQL is used to specify multiple values in a WHERE clause.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name"
                 + " WHERE column_name IN (value1, value2, ...);"
    },
    "examples": [
        {
            "example_description": "Selecting products in a specific category",
            "sql_query": "SELECT * FROM products WHERE category_id IN (1, 3, 5);"
        },
        {
            "example_description": "Selecting orders with specific statuses",
            "sql_query": "SELECT * FROM orders WHERE status_code IN ('Pending', 'Processing');"
        },
        {
            "example_description": "Selecting employees with specific IDs",
            "sql_query": "SELECT * FROM employees WHERE employee_id IN (101, 102, 103);"
        }
    ]
}
