import os

from generator.config import BASE_PACKAGE, AUTHOR, OUTPUT_DIR
from generator.renderer.renderer import render


def write(pkg, name, content):
    path = os.path.join(OUTPUT_DIR, pkg.replace('.', '/'))
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, name), 'w', encoding='utf-8') as f:
        f.write(content)


def generate(table):
    ctx = {
        "table": table,
        "package": BASE_PACKAGE,
        "author": AUTHOR
    }

    files = {
        "entity.java.j2": (f"{BASE_PACKAGE}.dal.entitys", f"{table.class_name}.java"),
        "mapper.java.j2": (f"{BASE_PACKAGE}dal.persistence", f"{table.class_name}Mapper.java"),
        "mapper.xml.j2": (f"{BASE_PACKAGE}dal.persistence", f"{table.class_name}Mapper.xml"),
        "service.java.j2": (f"{BASE_PACKAGE}.service", f"{table.class_name}Service.java"),
        "serviceImpl.java.j2": (f"{BASE_PACKAGE}.service", f"{table.class_name}ServiceImpl.java"),
        "controller.java.j2": (f"{BASE_PACKAGE}.controller", f"{table.class_name}Controller.java"),
    }

    for tpl, (pkg, name) in files.items():
        content = render(tpl, ctx)
        write(pkg, name, content)
