from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "ddddd"

@app.route('/heejune')
def heejune():
    return "안녕하세요 신희준입니다."