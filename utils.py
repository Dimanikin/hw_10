import json


def load_candidates():
    """
    Функция открывает файл и складывает в список
    :return: список
    """
    with open("candidates.json", "r", encoding="UTF-8") as file:
        items = json.load(file)
        return items
