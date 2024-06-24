# 定义 ORDER BY 子句的相关知识
ORDER_BY = {
    "description": "The ORDER BY clause in SQL is used to sort the result set of a query by one or more columns in ascending or descending order.",
    "syntax": {
        "basic": "SELECT column1, column2, ..."
                 + " FROM table_name"
                 + " ORDER BY column1 ASC|DESC;",
        "multiple_columns": "SELECT column1, column2, ..."
                            + " FROM table_name"
                            + " ORDER BY column1 ASC|DESC, column2 ASC|DESC, ...;"
    },
    "examples": [
        {
            "example_description": "Sorting employees by salary in descending order",
            "sql_query": "SELECT * FROM employees ORDER BY salary DESC;"
        },
        {
            "example_description": "Sorting orders by order date and amount",
            "sql_query": "SELECT * FROM orders ORDER BY order_date ASC, amount DESC;"
        }
    ]
}