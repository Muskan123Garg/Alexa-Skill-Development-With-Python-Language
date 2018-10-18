from flask import flask
from flask_ask import Ask, Statement, question, session
import json
import requests
import time
import unidecode


app = Flask(__name__)
ask = Ask(app, "/reddit_reader")


def get_headlines():
    pass

www.websit.com/reddit_reader
@app.route('/')
def homepage():
    return "hi there, how you doing?"

if __name__== '__main__':
    app.run(debug=True)
