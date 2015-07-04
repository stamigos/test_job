__author__ = 'amigos'
from flask import render_template, Blueprint
from library import app

shop_page = Blueprint('shop', __name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/successful')
def successful():
    return render_template('successful.html')


@app.route('/fail')
def fail():
    return render_template('fail.html')


@app.route('/pending')
def pending():
    return render_template('pending.html')