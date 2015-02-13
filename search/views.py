from flask import g, url_for, redirect, render_template
from flask.ext.login import current_user
from flask import Blueprint
from config import MAX_SEARCH_RESULTS
from library import app
from library.models import Author, Book
from library.forms import SearchForm

search_page = Blueprint('search', __name__, template_folder='templates')


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