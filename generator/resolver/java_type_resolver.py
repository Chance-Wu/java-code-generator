# 根据MySQL列类型和列名解析对应的Java类型
# 该函数处理常见的MySQL数据类型到Java类型的映射关系
def resolve(mysql_type, column_name):
    # 将MySQL类型转换为小写以便比较
    t = mysql_type.lower()
    # 如果是tinyint类型且列名以"is_"开头，则映射为Boolean类型
    if t.startswith("tinyint") and column_name.startswith("is_"):
        return "Boolean"
    # 如果是bigint类型，则映射为Long类型
    if t.startswith("bigint"):
        return "Long"
    # 如果是int类型，则映射为Integer类型
    if t.startswith("int"):
        return "Integer"
    # 如果包含decimal，则映射为BigDecimal类型
    if "decimal" in t:
        return "BigDecimal"
    # 如果包含datetime或timestamp，则映射为Date类型
    if "datetime" in t or "timestamp" in t:
        return "Date"
    # 如果包含json，则映射为String类型
    if "json" in t:
        return "String"
    # 默认情况下返回String类型
    return "String"
