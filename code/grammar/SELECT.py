# 定义 SQL SELECT 语句的相关知识
SELECT = {
    "description": "The SELECT statement is used to retrieve data from one or more tables in a database.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name;",
        "with_conditions": "SELECT column1, column2, ..."
                           + " FROM table_name"
                           + " WHERE condition;",
        "with_aliases": "SELECT column1 AS alias1, column2 AS alias2, ..."
                        + " FROM table_name;",
        "with_functions": "SELECT COUNT(column1), AVG(column2), ..."
                          + " FROM table_name;"
    },
    "examples": [
        {
            "example_description": "Selecting all columns from a table",
            "sql_query": "SELECT * FROM employees;"
        },
        {
            "example_description": "Selecting specific columns with a condition",
            "sql_query": "SELECT employee_id, first_name, last_name FROM employees WHERE department = 'IT';"
        },
        {
            "example_description": "Selecting columns with aliases",
            "sql_query": "SELECT employee_id AS id, first_name AS first, last_name AS last FROM employees;"
        },
        {
            "example_description": "Using aggregate functions",
            "sql_query": "SELECT COUNT(employee_id) AS num_employees, AVG(salary) AS avg_salary FROM employees;"
        }
    ]
}