# 定义 SET 更新语句的相关知识
SET = {
    "description": " SQL的\'SET\'数据类型用于存储一组可能的值。 The SET statement in SQL is used to update existing records in a table.",
    "syntax": {
        "basic": "UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;"
    },
    "examples": [
        {
            "example_description": "Updating the salary of an employee",
            "sql_query": "UPDATE employees SET salary = 60000 WHERE employee_id = 101;"
        },
        {
            "example_description": "Setting the status of an order to 'Shipped'",
            "sql_query": "UPDATE orders SET status = 'Shipped' WHERE order_id = 12345;"
        }
    ]
}