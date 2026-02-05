class FieldMeta:
    """
    字段元数据类，用于存储数据库字段的相关信息。

    Attributes:
        column_name (str): 数据库列名
        field_name (str): 对应的Java字段名
        mysql_type (str): MySQL数据类型
        comment (str): 字段注释
        is_pk (bool): 是否为主键，默认为False
        nullable (bool): 是否允许为空，默认为True
        java_type (str): 对应的Java数据类型，默认为None
    """

    def __init__(self, column, field, mysql_type, comment, pk=False, nullable=True):
        self.column_name = column
        self.field_name = field
        self.mysql_type = mysql_type
        self.comment = comment
        self.is_pk = pk
        self.nullable = nullable
        self.java_type = None
