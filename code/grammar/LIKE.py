# 定义 LIKE 操作符的相关知识
LIKE = {
    "description": "The LIKE operator in SQL is used to search for a specified pattern in a column.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name"
                 + " WHERE column_name LIKE pattern;",
        "wildcards": {
            "%": "Matches any sequence of characters (including zero characters).",
            "_": "Matches any single character."
        }
    },
    "examples": [
        {
            "example_description": "Selecting customers with names starting with 'A'",
            "sql_query": "SELECT * FROM customers WHERE customer_name LIKE 'A%';"
        },
        {
            "example_description": "Selecting products with names containing 'apple'",
            "sql_query": "SELECT * FROM products WHERE product_name LIKE '%apple%';"
        },
        {
            "example_description": "Selecting employees with last names ending in 'son'",
            "sql_query": "SELECT * FROM employees WHERE last_name LIKE '%son';"
        }
    ]
}