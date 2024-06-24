# 定义 FOREIGN KEY 的相关知识
FOREIGN_KEY = {
    "description": "The FOREIGN KEY constraint in SQL establishes a link between two tables by referencing the primary key or unique key of another table.",
    "syntax": {
        "basic": "FOREIGN KEY (child_column) REFERENCES parent_table(parent_column);"
    },
    "examples": [
        {
            "example_description": "Creating a table with a FOREIGN KEY constraint",
            "sql_query": "CREATE TABLE orders ("
                         + " order_id INT PRIMARY KEY,"
                         + " customer_id INT,"
                         + " order_date DATE,"
                         + " FOREIGN KEY (customer_id) REFERENCES customers(customer_id)"
                         + ");"
        },
        {
            "example_description": "Adding a FOREIGN KEY constraint to an existing table",
            "sql_query": "ALTER TABLE order_items ADD CONSTRAINT fk_order_id FOREIGN KEY (order_id) REFERENCES orders(order_id);"
        }
    ]
}