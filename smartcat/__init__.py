from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pages/<page>')
def pages(page):
    return render_template('/pages/'+page)
    
