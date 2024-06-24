# 定义 NOT NULL 约束的相关知识
NOT_NULL = {
    "description": "The NOT NULL constraint in SQL ensures that a column does not accept NULL values.",
    "syntax": {
        "basic": "column_name datatype NOT NULL,"
    },
    "examples": [
        {
            "example_description": "Creating a table with a NOT NULL constraint",
            "sql_query": "CREATE TABLE employees ("
                         + " employee_id INT NOT NULL,"
                         + " first_name VARCHAR(50) NOT NULL,"
                         + " last_name VARCHAR(50) NOT NULL,"
                         + " department_id INT"
                         + ");"
        },
        {
            "example_description": "Altering an existing table to add a NOT NULL constraint",
            "sql_query": "ALTER TABLE employees MODIFY department_id INT NOT NULL;"
        }
    ]
}
