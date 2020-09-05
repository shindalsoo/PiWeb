import datetime, random, pygame, os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from gtts import gTTS

app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartcat.db' #'mysql://root:''@localhost/crud'
app.config['SQlALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class LangAlarmConf(db.Model):
    __tablename__ = 'tblLangAlarmConf'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alarmtime = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    def __init__(self, alarmtime):
        self.alarmtime = alarmtime

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

@app.route('/bbs/list.html')
def bbslist():
    read_data = LangAlarmWord.query.all()
    return render_template('/bbs/list.html',langwords = read_data) 

@app.route('/bbs/<page>',methods=['POST','GET'])
def bbs(page):
    id = request.args.get('id','0')
    if page == 'list.html':
        conf_data = LangAlarmWord.query.all()
        read_data = LangAlarmWord.query.order_by(LangAlarmWord.id.desc()).all()
        return render_template('/bbs/'+page, langwords = read_data, alarmconf = conf_data)
    elif page=='add.html':
        read_data = ()
        return render_template('/bbs/'+page)
    elif page=='update.html':
        read_data = LangAlarmWord.query.get(id)
        return render_template('/bbs/'+page, langwords = read_data)

@app.route('/bbs_save_add', methods=['POST'])
def bbsadd():
    category = request.form['category']
    word = request.form['word']
    memo = request.form['memo']
    newWord = LangAlarmWord(category,word,memo)
    db.session.add(newWord)
    db.session.commit()
    return "add success"

@app.route('/bbs_save_update/<id>', methods=['POST'])
def bbsupdate(id):
    updateWord = LangAlarmWord.query.get(id)
    updateWord.category = request.form['category']
    updateWord.word = request.form['word']
    updateWord.memo = request.form['memo']
    db.session.commit()
    return "update success"

@app.route('/bbs_save_delete/<id>', methods=['POST'])
def bbsdelete(id):
    delWord = LangAlarmWord.query.get(id)
    db.session.delete(delWord)
    db.session.commit()
    return "update success"

def udfTtsPlay(text):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    filename = str(r2)+"randomtext"+str(r1)+".mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        pass

    # os.remove(filename) # Access Denide남

@app.route('/playvoice/<id>')
def playvoice(id):
    if str(id)=="0":
        readWord = LangAlarmWord.query.order_by(LangAlarmWord.id.desc()).all()
        text = ""
        for row in readWord:
            text = text + row.category + ","
            text = text + row.word + ","
            text = text + row.memo + ","
    else:
        readWord = LangAlarmWord.query.get(id)
        text = readWord.category + ","
        text = text + readWord.word + ","
        text = text + readWord.memo
    
    udfTtsPlay(text)
    return "고양이가 소리를 냈습니다."

@app.route('/movement/list.html')
def movement_list():
    return render_template('/movement/list.html')

@app.route('/lcd/list.html')
def lcd_list():
    return render_template('/lcd/list.html')