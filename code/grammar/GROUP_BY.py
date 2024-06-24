# 定义 GROUP BY 的相关信息
GROUP_BY = {
    "描述": "SQL 中的 GROUP BY 语句用于根据一个或多个列对结果集进行分组，并允许对每个组应用聚合函数（如 SUM、COUNT、AVG、MAX、MIN 等）。",
    "语法": {
        "基本语法": "SELECT column1, aggregate_function(column2)"
                 + " FROM table_name"
                 + " GROUP BY column1;",
        "多列分组": "SELECT column1, column2, aggregate_function(column3)"
                 + " FROM table_name"
                 + " GROUP BY column1, column2;"
    },
    "示例": [
        {
            "示例描述": "计算每个产品类别的总销售额",
            "SQL查询": "SELECT category, SUM(sales_amount) AS total_sales"
                     + " FROM sales"
                     + " GROUP BY category;"
        },
        {
            "示例描述": "按部门计算平均工资",
            "SQL查询": "SELECT department_id, AVG(salary) AS avg_salary"
                     + " FROM employees"
                     + " GROUP BY department_id;"
        }
    ]
}
