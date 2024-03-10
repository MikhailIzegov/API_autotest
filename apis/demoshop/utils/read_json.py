import json
import os


def load_schema(name):
    # Получаем текущую директорию (где находится этот скрипт)
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    # Путь к папке b относительно текущей директории
    dir_with_schemas = os.path.join('..', 'json_schemas')
    print(dir_with_schemas)

    # Полный путь к папке со схемами от этой папки
    path = os.path.abspath(os.path.join(current_dir, dir_with_schemas, name))

    print(path)

    with open(path) as file:
        json_schema = json.loads(file.read())
        print(json_schema)
    return json_schema
