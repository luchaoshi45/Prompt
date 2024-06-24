# 定义 DEFAULT 约束的相关知识
DEFAULT = {
    "description": "The DEFAULT constraint in SQL specifies a default value for a column when no value is specified.",
    "syntax": {
        "basic": "column_name datatype DEFAULT default_value,"
    },
    "examples": [
        {
            "example_description": "Creating a table with a DEFAULT constraint",
            "sql_query": "CREATE TABLE students ("
                         + " student_id INT PRIMARY KEY,"
                         + " first_name VARCHAR(50) NOT NULL,"
                         + " last_name VARCHAR(50) NOT NULL,"
                         + " grade INT DEFAULT 0"
                         + ");"
        },
        {
            "example_description": "Adding a DEFAULT constraint to an existing column",
            "sql_query": "ALTER TABLE employees ADD COLUMN department_id INT DEFAULT 1;"
        }
    ]
}