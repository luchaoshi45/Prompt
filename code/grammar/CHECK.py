# 定义 CHECK 约束的相关知识
CHECK = {
    "description": "The CHECK constraint in SQL specifies a condition that must be true for each row in a table.",
    "syntax": {
        "basic": "column_name datatype CHECK (condition);"
    },
    "examples": [
        {
            "example_description": "Creating a table with a CHECK constraint",
            "sql_query": "CREATE TABLE students ("
                         + " student_id INT PRIMARY KEY,"
                         + " age INT CHECK (age >= 18),"
                         + " name VARCHAR(100)"
                         + ");"
        },
        {
            "example_description": "Adding a CHECK constraint to an existing table",
            "sql_query": "ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary >= 30000);"
        }
    ]
}