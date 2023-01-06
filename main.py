from flask import Flask, render_template, request, redirect #こちらに変更
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(host="localhost", port=8888, debug=True)