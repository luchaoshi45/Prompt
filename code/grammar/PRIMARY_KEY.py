# 定义 PRIMARY KEY 的相关知识
PRIMARY_KEY = {
    "description": "The PRIMARY KEY constraint uniquely identifies each record in a table.",
    "syntax": {
        "basic": "column_name datatype PRIMARY KEY,"
    },
    "examples": [
        {
            "example_description": "Creating a table with a PRIMARY KEY constraint",
            "sql_query": "CREATE TABLE employees ("
                         + " employee_id INT PRIMARY KEY,"
                         + " first_name VARCHAR(50),"
                         + " last_name VARCHAR(50),"
                         + " department_id INT"
                         + ");"
        },
        {
            "example_description": "Adding a PRIMARY KEY constraint to an existing table",
            "sql_query": "ALTER TABLE employees ADD CONSTRAINT pk_employee_id PRIMARY KEY (employee_id);"
        }
    ]
}