from flask import Flask
from pip._internal.resolution.resolvelib import candidates

from utils import load_json, get_all_candidates, format_candidates, get_candidate_by_id, get_candidate_by_skill

app = Flask(__name__)

@app.route('/')
def page_name():
    '''Главная страница'''
    candidate: list[dict] = get_all_candidates()
    result: str = format_candidates(candidates)
    return result

@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    '''Поиск кандидиата по id'''
    candidate: dict = get_candidate_by_id(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    '''Поиск по навыку'''
    skill_lower = skill.lower()
    candidates: list[dict] = get_candidate_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run()