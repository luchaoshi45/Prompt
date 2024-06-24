# 定义 NULL 的相关知识
NULL = {
    "description": "In SQL, NULL is a special marker used to indicate that a data value does not exist in the database.",
    "usage": {
        "definition": "column_name datatype NULL,"
    },
    "examples": [
        {
            "example_description": "Creating a table where a column allows NULL values",
            "sql_query": "CREATE TABLE students ("
                         + " student_id INT PRIMARY KEY,"
                         + " first_name VARCHAR(50) NOT NULL,"
                         + " last_name VARCHAR(50) NULL,"
                         + " age INT"
                         + ");"
        },
        {
            "example_description": "Inserting NULL values into a table",
            "sql_query": "INSERT INTO students (student_id, first_name, last_name, age) VALUES (1, 'John', NULL, 25);"
        },
        {
            "example_description": "Querying rows with NULL values",
            "sql_query": "SELECT * FROM students WHERE last_name IS NULL;"
        }
    ]
}