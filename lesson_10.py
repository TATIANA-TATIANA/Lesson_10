from flask import Flask
from service import load_json
from service import find_candidate
from service import find_skill

app = Flask(__name__)

html_format = ["<pre>", "</pre>"]


@app.route("/")
def main_page():
    """
    Главная страница
    """
    candidates = load_json("candidates.json")
    answer = html_format[0]
    for candidate in candidates:
        answer += f"Имя: {candidate['name']}\nПозиция: {candidate['position']}\nНавыки: {candidate['skills']}\n"
    answer += html_format[1]
    return answer


@app.route("/candidate/<int:uid>")
def candidate_page(uid):
    """
    Профиль кандидата
    """
    candidate = find_candidate("candidates.json", uid)
    answer = f"<img src='{candidate['picture']}'>"
    answer += html_format[0]
    answer += f"Имя: {candidate['name']}\nПозиция: {candidate['position']}\nНавыки: {candidate['skills']}\n"
    answer += html_format[1]
    return answer


@app.route("/skills/<skill>")
def skill_page(skill):
    """
    Кандидаты с нужным навыком
    """
    useful_candidates = find_skill("candidates.json", skill)
    answer = html_format[0]
    for candidate in useful_candidates:
        answer += f"Имя: {candidate['name']}\nПозиция: {candidate['position']}\nНавыки: {candidate['skills']}\n"
    answer += html_format[1]
    return answer


app.run()
