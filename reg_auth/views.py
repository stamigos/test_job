from flask import request, redirect, url_for, render_template
from flask.ext.login import login_user, logout_user
from flask import Blueprint
from library import db, app
from library.models import User

login_page = Blueprint('login', __name__, template_folder='templates')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET'])
def register_get():
        return render_template('register.html')


@app.route('/register', methods=['POST'])
def register_post():
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login_get'))


@app.route('/login', methods=['GET'])
def login_get():
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        return redirect(url_for('login_get'))
    login_user(registered_user)
    return redirect(request.args.get('next') or url_for('index'))