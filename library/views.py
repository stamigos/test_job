from flask import request, g, redirect, url_for, render_template, flash
from forms import SearchForm
from wtforms.ext.sqlalchemy.orm import model_form
from flask.ext.login import current_user, login_required
from flask.ext.login import LoginManager
from library import db, app
from library.resources import Resources
from library.models import User, Book, Author
from config import MAX_SEARCH_RESULTS

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
def index():
    return render_template('index.html',
                           authors=Author.query.all())


resources = Resources(authors=Author, books=Book)


@app.route('/<curr_model>/', methods=['GET'])
@login_required
def get_list(curr_model):
    path = '/' + curr_model + '/'
    model = resources.get_context(str(curr_model))
    obj = db.session.query(model).all()
    return render_template('list_view.html',
                           obj=obj,
                           path=path)



@app.route('/<curr_model>/new/', methods=['GET'])
@login_required
def get_new(curr_model):
    path = '/' + curr_model + '/'
    model = resources.get_context(str(curr_model))
    Objform = model_form(model, db.session)
    form = Objform()
    action = path
    return render_template('detail_view.html',
                           action=action,
                           path=path,
                           form=form)


@app.route('/<curr_model>/<obj_id>/delete/', methods=['GET'])
@login_required
def get_delete(curr_model, obj_id):
    path = '/' + curr_model + '/'
    model = resources.get_context(str(curr_model))
    obj = db.session.query(model).get(obj_id)
    db.session.delete(obj)
    db.session.commit()
    return redirect(path)


@app.route('/<curr_model>/<obj_id>/edit/', methods=['GET'])
@login_required
def get_edit(curr_model, obj_id):
    path = '/' + curr_model + '/'
    model = resources.get_context(str(curr_model))
    ObjForm = model_form(model, db.session)
    obj = db.session.query(model).get(obj_id)
    form = ObjForm(obj=obj)
    return render_template('detail_view.html',
                           form=form,
                           action=path,
                           path=path)

@app.route('/<curr_model>/', methods=['POST'])
@login_required
def post(curr_model, obj_id=''):
    model = resources.get_context(str(curr_model))
    if obj_id:
        obj = db.session.query(model).get(obj_id)
    else:
        obj = model()

    path = '/' + curr_model + '/'
    ObjForm = model_form(model, db.session)
    form = ObjForm(request.form)
    form.populate_obj(obj)

    db.session.add(obj)
    db.session.commit()

    return redirect(path)


@app.before_request
def before_request():
    g.user = current_user
    g.search_form = SearchForm()


@app.route('/search', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('/'))
    return redirect(url_for('search_results_authors', query=g.search_form.search.data))


@app.route('/search_results/<query>')
def search_results_authors(query):
    results = Author.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
                           query=query,
                           results=results)
