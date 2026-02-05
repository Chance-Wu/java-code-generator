import pymysql

from generator.model.field import FieldMeta
from generator.model.table import TableMeta
from generator.resolver.java_type_resolver import resolve


def snake_to_camel(name, upper=False):
    """
    将snake_case格式的字符串转换为camelCase格式

    Args:
        name (str): 需要转换的字符串
        upper (bool): 是否转换为首字母大写的PascalCase格式，默认为False

    Returns:
        str: 转换后的camelCase或PascalCase字符串
    """
    parts = name.split('_')
    if upper:
        return ''.join(p.capitalize() for p in parts)
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])


def load_table(table, config):
    """
    从MySQL数据库加载表结构信息
    
    Args:
        table (str): 表名
        config (dict): 数据库连接配置
        
    Returns:
        TableMeta: 包含表元数据的对象
    """
    # 连接数据库
    conn = pymysql.connect(**config)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    # 执行查询获取表字段信息
    cur.execute(f"SHOW FULL COLUMNS FROM {table}")
    rows = cur.fetchall()
    # 关闭数据库连接
    conn.close()

    fields = []
    # 遍历所有字段行，构建字段元数据对象
    for r in rows:
        f = FieldMeta(
            column=r['Field'],  # 字段列名
            field=snake_to_camel(r['Field']),  # 转换为驼峰命名的字段名
            mysql_type=r['Type'],  # MySQL数据类型
            comment=r.get('Comment') or r['Field'],  # 字段注释，若没有则使用字段名
            pk=r['Key'] == 'PRI',  # 是否为主键
            nullable=r['Null'] == 'YES'  # 是否可为空
        )
        # 解析MySQL类型到Java类型的映射
        f.java_type = resolve(f.mysql_type, f.column_name)
        fields.append(f)

    # 返回表元数据对象，包含表名、类名(驼峰命名)和字段列表
    return TableMeta(table, snake_to_camel(table, True), fields)
