# 定义 JOIN 的相关知识
JOIN = {
    "description": "The JOIN operation in SQL is used to combine rows from two or more tables, based on a related column between them.",
    "syntax": {
        "inner_join": "SELECT column1, column2, ..."
                      + " FROM table1"
                      + " INNER JOIN table2 ON table1.column_name = table2.column_name;",
        "left_join": "SELECT column1, column2, ..."
                     + " FROM table1"
                     + " LEFT JOIN table2 ON table1.column_name = table2.column_name;",
        "right_join": "SELECT column1, column2, ..."
                      + " FROM table1"
                      + " RIGHT JOIN table2 ON table1.column_name = table2.column_name;",
        "full_outer_join": "SELECT column1, column2, ..."
                           + " FROM table1"
                           + " FULL OUTER JOIN table2 ON table1.column_name = table2.column_name;"
    },
    "examples": [
        {
            "example_description": "Performing an inner join to combine employee and department information",
            "sql_query": "SELECT * FROM employees INNER JOIN departments ON employees.department_id = departments.department_id;"
        },
        {
            "example_description": "Performing a left join to include all employees even if they do not have a department assigned",
            "sql_query": "SELECT * FROM employees LEFT JOIN departments ON employees.department_id = departments.department_id;"
        },
        {
            "example_description": "Performing a right join to include all departments even if they do not have employees assigned",
            "sql_query": "SELECT * FROM employees RIGHT JOIN departments ON employees.department_id = departments.department_id;"
        },
        {
            "example_description": "Performing a full outer join to include all employees and departments",
            "sql_query": "SELECT * FROM employees FULL OUTER JOIN departments ON employees.department_id = departments.department_id;"
        }
    ]
}