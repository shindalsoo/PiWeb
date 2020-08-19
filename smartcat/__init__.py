from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcat.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class LangAlarmWord(db.Model):
    __tablename__ = 'tblLangAlarmWord'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(30), unique=False, nullable=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    memo = db.Column(db.String(200), unique=False, nullable=True)
    cntplayed = db.Column(db.Integer, unique=False, nullable=True)
    useyn = db.Column(db.String(1), unique=False, nullable=True)

    def __init__(self, category, word, memo):
        self.category = category
        self.word = word
        self.memo = memo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def pages(page):
    return render_template('/pages/'+page)
    
@app.route('/contents/<page>')
def contents(page):
    return render_template('/contents/'+page)

@app.route('/bbs/<page>')
def bbs(page):
    all_data = LangAlarmWord.query.all()
    return render_template('/bbs/'+page, langwords = all_data)
