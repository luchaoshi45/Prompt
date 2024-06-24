# 定义 SQL WHERE 子句的相关知识
WHERE = {
    "description": "The WHERE clause in SQL is used to filter records based on a specified condition.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name"
                 + " WHERE condition;",
        "multiple_conditions": "SELECT column1, column2, ..."
                               + " FROM table_name"
                               + " WHERE condition1 AND/OR condition2 AND/OR ...;",
        "operators": {
            "=": "Equal",
            "<>": "Not equal",
            ">": "Greater than",
            "<": "Less than",
            ">=": "Greater than or equal",
            "<=": "Less than or equal",
            "BETWEEN": "Between an inclusive range",
            "LIKE": "Search for a pattern",
            "IN": "Matches any values in a list",
            "IS NULL": "NULL values",
            "IS NOT NULL": "Non-NULL values"
        }
    },
    "examples": [
        {
            "example_description": "Selecting employees with salary greater than 50000",
            "sql_query": "SELECT * FROM employees WHERE salary > 50000;"
        },
        {
            "example_description": "Selecting orders from a specific date range",
            "sql_query": "SELECT * FROM orders WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31';"
        }
    ]
}
