# 定义 UPDATE 语句的相关知识
UPDATE = {
    "description": "The UPDATE statement in SQL is used to modify existing records (rows) in a table.",
    "syntax": {
        "basic": "UPDATE table_name"
                 + " SET column1 = value1, column2 = value2, ..."
                 + " WHERE condition;",
    },
    "examples": [
        {
            "example_description": "Updating the salary of an employee",
            "sql_query": "UPDATE employees SET salary = 85000 WHERE employee_id = 101;"
        },
        {
            "example_description": "Updating multiple columns using a condition",
            "sql_query": "UPDATE employees SET department = 'IT', manager_id = 201 WHERE department = 'HR';"
        }
    ]
}