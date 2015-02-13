from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from library import views, models
from reg_auth.views import login_page
from search.views import search_page

app.register_blueprint(login_page)
app.register_blueprint(search_page)