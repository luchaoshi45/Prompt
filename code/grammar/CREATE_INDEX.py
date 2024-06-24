# 定义 CREATE INDEX 语句的相关知识
CREATE_INDEX = {
    "description": "The CREATE INDEX statement in SQL is used to create an index on a table, which improves the speed of data retrieval operations.",
    "syntax": {
        "basic": "CREATE INDEX index_name ON table_name (column_name);"
    },
    "examples": [
        {
            "example_description": "Creating an index on a table",
            "sql_query": "CREATE INDEX idx_last_name ON employees (last_name);"
        },
        {
            "example_description": "Creating a unique index on a table",
            "sql_query": "CREATE UNIQUE INDEX idx_email ON customers (email);"
        }
    ]
}
