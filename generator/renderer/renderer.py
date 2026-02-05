from jinja2 import FileSystemLoader, Environment

def render(template, context):
    """
    渲染指定的模板文件，并传入上下文数据。

    :param template: 模板文件名
    :param context: 传递给模板的上下文数据（字典形式）
    :return: 渲染后的字符串结果
    """
    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True,
        lstrip_blocks=True
    )
    return env.get_template(template).render(**context)
