# 定义 DELETE 语句的相关知识
DELETE = {
    "description": "The DELETE statement in SQL is used to delete existing records (rows) from a table.",
    "syntax": {
        "basic": "DELETE FROM table_name"
                 + " WHERE condition;",
        "without_condition": "DELETE FROM table_name;"
    },
    "examples": [
        {
            "example_description": "Deleting a single row based on a condition",
            "sql_query": "DELETE FROM employees WHERE employee_id = 101;"
        },
        {
            "example_description": "Deleting all rows from a table",
            "sql_query": "DELETE FROM employees;"
        }
    ]
}