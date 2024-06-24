# 定义 INSERT INTO 语句的相关知识
INSERT_INTO = {
    "description": "The INSERT INTO statement in SQL is used to insert new records (rows) into a table.",
    "syntax": {
        "basic": "INSERT INTO table_name (column1, column2, ...)"
                 + " VALUES (value1, value2, ...);",
        "with_select": "INSERT INTO table_name (column1, column2, ...)"
                       + " SELECT value1, value2, ..."
                       + " FROM another_table WHERE condition;"
    },
    "examples": [
        {
            "example_description": "Inserting a single row into the employees table",
            "sql_query": "INSERT INTO employees (employee_id, first_name, last_name, department, salary)"
                         + " VALUES (101, 'John', 'Doe', 'IT', 80000);"
        },
        {
            "example_description": "Inserting multiple rows using a SELECT statement",
            "sql_query": "INSERT INTO employees (employee_id, first_name, last_name, department, salary)"
                         + " SELECT employee_id, first_name, last_name, 'HR', 75000"
                         + " FROM candidates WHERE experience_years > 5;"
        }
    ]
}
