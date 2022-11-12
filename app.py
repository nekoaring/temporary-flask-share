import random
from flask import Flask
from flask import make_response
app = Flask(__name__)

omikujis = [
    {
        "name": "daikyo",
        "weight": 0.5
    },
    {
        "name": "suekichi",
        "weight": 1
    },
    {
        "name": "kichi",
        "weight": 5
    },
    {
        "name": "daikichi",
        "weight": 0.5
    },
]

def shake():
    """おみくじを抽選します."""
    names = [x["name"] for x in omikujis]
    weights = [x["weight"] for x in omikujis]
    res = random.choices(names, weights=weights)[0]
    return res 


@app.route("/")
def shake_omikuji():
    """おみくじを抽選し、結果を返却します."""
    kuji = shake()
    resp = make_response(kuji)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    resp.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return resp
