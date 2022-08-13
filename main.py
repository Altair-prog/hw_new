from flask import Flask

from utils import load_candidates, get_all, get_by_pk, get_by_skill

FILENAME = 'candidates.json'
data = get_all(load_candidates(FILENAME))

app = Flask(__name__)

@app.route('/')
def index():
    candidate_str = '<pre>'
    for i in data:
        candidate_str += f'{i} \n \n'
    candidate_str += '</pre>'
    return candidate_str


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        candidate_str = f'<img src = "{user.picture}">'
        candidate_str += f'<pre> {user} </pre>'
    else:
        candidate_str = 'NOT FOUND'
    return candidate_str

@app.route('/skills/<x>')
def get_users(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        candidate_str = '<pre>'
        for i in users:
            candidate_str += f'{i} \n \n'
        candidate_str += '</pre>'
    else:
        candidate_str = 'NOT FOUND'
    return candidate_str







if __name__ == '__main__':
    app.run(port=5000)
