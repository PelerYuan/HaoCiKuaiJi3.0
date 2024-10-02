import json
from json import JSONDecodeError


def open_json(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.loads(file.read())
    except JSONDecodeError:
        return {}


def write_json(path: str, data: dict):
    with open(path, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(data))
