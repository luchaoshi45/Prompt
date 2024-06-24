# 定义 ALTER 的相关知识
ALTER = {
    "description": "The ALTER statement in SQL is used to modify existing database objects such as tables and indexes.",
    "syntax": {
        "table_add_column": "ALTER TABLE table_name ADD column_name datatype;",
        "table_modify_column": "ALTER TABLE table_name MODIFY column_name datatype;",
        "table_drop_column": "ALTER TABLE table_name DROP COLUMN column_name;",
        "rename_table": "ALTER TABLE old_table_name RENAME TO new_table_name;",
        "add_constraint": "ALTER TABLE table_name ADD CONSTRAINT constraint_name constraint_details;",
        "drop_constraint": "ALTER TABLE table_name DROP CONSTRAINT constraint_name;"
    },
    "examples": [
        {
            "example_description": "Adding a new column to a table",
            "sql_query": "ALTER TABLE employees ADD hire_date DATE;"
        },
        {
            "example_description": "Modifying the data type of a column",
            "sql_query": "ALTER TABLE employees MODIFY salary DECIMAL(10,2);"
        },
        {
            "example_description": "Dropping a column from a table",
            "sql_query": "ALTER TABLE employees DROP COLUMN department_id;"
        },
        {
            "example_description": "Renaming a table",
            "sql_query": "ALTER TABLE old_table RENAME TO new_table;"
        },
        {
            "example_description": "Adding a new constraint to a table",
            "sql_query": "ALTER TABLE orders ADD CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id);"
        },
        {
            "example_description": "Dropping a constraint from a table",
            "sql_query": "ALTER TABLE orders DROP CONSTRAINT fk_customer_id;"
        }
    ]
}