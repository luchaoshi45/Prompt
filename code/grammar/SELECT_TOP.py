# 定义 SELECT TOP 语句的相关知识
SELECT_TOP = {
    "description": "The SELECT TOP clause is used in SQL to limit the number of rows returned by a query.",
    "syntax": {
        "basic": "SELECT TOP number|percent column1, column2, ..."
                 + " FROM table_name;",
        "with_order_by": "SELECT TOP number|percent column1, column2, ..."
                         + " FROM table_name"
                         + " ORDER BY column1 ASC|DESC;"
    },
    "examples": [
        {
            "example_description": "Selecting the top 5 employees by salary",
            "sql_query": "SELECT TOP 5 * FROM employees ORDER BY salary DESC;"
        },
        {
            "example_description": "Selecting the top 10% of orders by amount",
            "sql_query": "SELECT TOP 10 PERCENT * FROM orders ORDER BY amount DESC;"
        }
    ]
}