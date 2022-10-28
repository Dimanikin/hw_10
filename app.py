from flask import Flask

from utils import load_candidates

app = Flask(__name__)


@app.route("/")
def get_all():
    """
    Функция возвращает всех кандидатов
    :return:
    """
    items = load_candidates()
    result = '<pre>'
    for candidate in items:
        result += f"""
            {candidate['name']}
            {candidate['position']}
            {candidate['skills']}
        """
    result += '</pre>'
    return result

@app.route("/candidates/<int:pk>")
def get_by_pk(pk) -> str | None:
    """
    Функция возвращает кандидата по pk
    :param pk:
    :return:
    """
    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate["pk"]:
            return f"<img src='{candidate['picture']}'/>" \
                   f"<pre>Имя кандидата - {candidate['name']}\n" \
                   f"Позиция кандидата: {candidate['position']}\n" \
                   f"Навыки через запятую: {candidate['skills']}</pre>"
    return None


@app.route("/skills/<skill_name>")
def get_by_skill(skill_name):
    """
    Функция возвращает кандидата по навыку
    :param skill_name:
    :return:
    """
    skills = load_candidates()
    result = '<pre>'
    for skill in skills:
        if skill_name.lower() in skill["skills"].split(", "):
            result += f"""
                    {skill['name']}
                    {skill['position']}
                    {skill['skills']}
                """
    result += '</pre>'
    return result


app.run()
