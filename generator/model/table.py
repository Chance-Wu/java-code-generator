class TableMeta:
    """
    表元数据类，用于存储表的基本信息和字段信息。
    
    Attributes:
        table_name (str): 数据库表名
        class_name (str): 对应的Java类名
        fields (list): 字段列表，包含FieldMeta对象
    """
    
    def __init__(self, table_name, class_name, fields):
        """
        初始化TableMeta实例
        
        Args:
            table_name (str): 数据库表名
            class_name (str): 对应的Java类名
            fields (list): 字段列表，包含FieldMeta对象
        """
        self.table_name = table_name
        self.class_name = class_name
        self.fields = fields
        self.imports = self._resolve_imports()

    @property
    def pk_field(self):
        """
        获取主键字段
        
        Returns:
            FieldMeta: 主键字段对象，如果没有主键则返回None
        """
        return next((f for f in self.fields if f.is_pk), None)

    def _resolve_imports(self):
        imports = set()

        for f in self.fields:
            jt = f.java_type
            if jt == 'Date':
                imports.add('java.util.Date')
            elif jt == 'BigDecimal':
                imports.add('java.math.BigDecimal')
            elif jt == 'LocalDateTime':
                imports.add('java.time.LocalDateTime')

        imports.add('java.io.Serializable')
        return sorted(imports)