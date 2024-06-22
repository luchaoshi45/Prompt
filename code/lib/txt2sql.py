# SQL 语句
txt2sql_lib = """
-- 数据查询（SELECT）
-- 查询所有列
SELECT * FROM table_name;
-- 查询特定列
SELECT column1, column2 FROM table_name;
-- 使用条件查询
SELECT * FROM table_name WHERE condition;
-- 排序
SELECT * FROM table_name ORDER BY column1 ASC;
-- 分组和聚合
SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
-- 使用聚合函数
SELECT AVG(column1), SUM(column2) FROM table_name;
-- 使用LIMIT
SELECT * FROM table_name LIMIT 10;
-- JOIN查询
SELECT a.column1, b.column2 FROM table1 a JOIN table2 b ON a.common_column = b.common_column;

-- 数据插入（INSERT）
-- 插入单行数据
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
-- 插入多行数据
INSERT INTO table_name (column1, column2) VALUES (value1, value2), (value3, value4);

-- 数据更新（UPDATE）
-- 更新特定行
UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;
-- 更新所有行
UPDATE table_name SET column1 = value1;

-- 数据删除（DELETE）
-- 删除特定行
DELETE FROM table_name WHERE condition;
-- 删除所有行
DELETE FROM table_name;

-- 创建表（CREATE TABLE）
-- 创建表
CREATE TABLE table_name ( column1 datatype PRIMARY KEY, column2 datatype, column3 datatype );

-- 删除表（DROP TABLE）
-- 删除表
DROP TABLE table_name;

-- 修改表（ALTER TABLE）
-- 添加列
ALTER TABLE table_name ADD column_name datatype;
-- 删除列
ALTER TABLE table_name DROP COLUMN column_name;
-- 修改列的数据类型
ALTER TABLE table_name MODIFY COLUMN column_name new_datatype;

-- 创建索引（CREATE INDEX）
-- 创建索引
CREATE INDEX index_name ON table_name (column_name);

-- 删除索引（DROP INDEX）
-- 删除索引
DROP INDEX index_name ON table_name;

-- 常用的聚合函数
-- COUNT()
SELECT COUNT(column_name) FROM table_name;
-- AVG()
SELECT AVG(column_name) FROM table_name;
-- SUM()
SELECT SUM(column_name) FROM table_name;
-- MAX()
SELECT MAX(column_name) FROM table_name;
-- MIN()
SELECT MIN(column_name) FROM table_name;
"""
