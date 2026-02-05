from generator.config import DB_CONFIG
from generator.datasource.mysql_loader import load_table
from generator.generator import generate


def run(table_name):
    table = load_table(table_name, DB_CONFIG)
    generate(table)
