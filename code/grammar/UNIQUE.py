# 定义 UNIQUE 约束的相关知识
UNIQUE = {
    "description": "The UNIQUE constraint in SQL ensures that all values in a column (or a group of columns) are unique (no duplicates).",
    "syntax": {
        "basic": "column_name datatype UNIQUE,"
    },
    "examples": [
        {
            "example_description": "Creating a table with a UNIQUE constraint",
            "sql_query": "CREATE TABLE products ("
                         + " product_id INT UNIQUE,"
                         + " product_name VARCHAR(100) UNIQUE,"
                         + " price DECIMAL(10, 2),"
                         + " category_id INT"
                         + ");"
        },
        {
            "example_description": "Adding a UNIQUE constraint to an existing table",
            "sql_query": "ALTER TABLE products ADD CONSTRAINT uc_product_name UNIQUE (product_name);"
        }
    ]
}