from flask import g, url_for, redirect, render_template, request
from flask.ext.login import current_user
from flask import jsonify
from flask import Blueprint
from config import MAX_SEARCH_RESULTS, WHOOSH_ENABLED
from library import app
from library.models import Author, Book
from library.resources import Resources
from library.forms import SearchForm

search_page = Blueprint('search', __name__, template_folder='templates')
search_model = ''

@app.before_request
def before_request():
    g.user = current_user
    g.search_form = SearchForm()
    g.search_enabled = WHOOSH_ENABLED


@app.route('/echo/', methods=['GET'])
def echo():
    global search_model
    ret_data = request.args.get('echoValue')
    search_model = ret_data
    return jsonify(results=ret_data)


@app.route('/search/', methods=['POST'])
def search():
    if not g.search_form.validate_on_submit():
        return redirect(url_for('/'))
    return redirect(url_for('search_results', query=g.search_form.search.data, search_model=search_model))

resources = Resources(authors=Author, books=Book)


@app.route('/search_results/<search_model>/<query>')
def search_results(query, search_model):
    model = resources.get_context(str(search_model))
    results = model.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
    return render_template('search_results.html',
                           query=query,
                           results=results, search_model=search_model)