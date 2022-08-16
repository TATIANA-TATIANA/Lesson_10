import json


def load_json(file_json):
    """
    Распаковывает список из JSON в PYTHON
    """
    with open(file_json, "r", encoding="utf-8") as i:
        new_list = json.load(i)
        return new_list


def find_candidate(list, id):
    """
    Ищет кандидата в указанном списке по ID
    """
    candidates_list = load_json(list)
    for candidate in candidates_list:
        if candidate["id"] == id:
            return candidate
    return None


def find_skill(list, skill):
    """
    Ищет в указанном списке кандидатов с нужными навыками
    """
    candidates_list = load_json(list)
    useful_candidates = []
    for candidate in candidates_list:
        if skill.lower() in candidate["skills"].lower().split(", "):
            useful_candidates.append(candidate)
    return useful_candidates
