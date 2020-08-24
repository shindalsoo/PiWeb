import datetime
from flask import Flask, render_template, request
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
    word = db.Column(db.String(100), unique=False, nullable=False)
    memo = db.Column(db.String(200), unique=False, nullable=True)
    cntplayed = db.Column(db.Integer, unique=False, nullable=True)
    useyn = db.Column(db.String(1), unique=False, nullable=True)
    regdate = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)

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

@app.route('/bbs/<page>',methods=['POST','GET'])
def bbs(page):
    id = request.args.get('id','0')
    if page == 'list.html':
        read_data = LangAlarmWord.query.order_by(LangAlarmWord.id.desc()).all()
    elif page=='insert.html':
        read_data = ()
    elif page=='update.html':
        read_data = LangAlarmWord.query.get(id)
    return render_template('/bbs/'+page, langwords = read_data)

@app.route('/bbs_save_insert', methods=['POST'])
def bbsinsert():
    category = request.form['category']
    word = request.form['word']
    memo = request.form['memo']
    newWord = LangAlarmWord(category,word,memo)
    db.session.add(newWord)
    db.session.commit()
    return "insert success"

@app.route('/bbs_save_update', methods=['POST'])
def bbsupdate():
    updateWord = LangAlarmWord.query.get(request.form.get('id'))
    updateWord.category = request.form['category']
    updateWord.word = request.form['word']
    updateWord.memo = request.form['memo']
    db.session.commit()
    return "update success"
