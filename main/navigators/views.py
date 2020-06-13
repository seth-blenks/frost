from ..blog_blueprint import blog_print
from flask import render_template,abort,g,url_for
from jinja2 import TemplateNotFound
from re import search
from pathlib import Path





@blog_print.route('/')
def homepage():
    
    return render_template('blogger/index.html')


@blog_print.route('/about')
def about():
    return render_template('blogger/About.html')

@blog_print.route('/plant')
def plant():
    articles = {}
    articles['heading'] = "This is the title"
    articles['paragraph'] = "This is the paragraph"
    articles['link'] = 'this is the link'
    Job = [articles]
    return render_template('blogger/Plant/index.html',Articles= Job)

@blog_print.route('/animal')
def animal():
    articles = {}
    articles['heading'] = "This is the title"
    articles['paragraph'] = "This is the paragraph"
    articles['link'] = 'this is the link'
    Job = [articles]
    return render_template('blogger/Animal/index.html',Articles=Job)

@blog_print.route('/cell')
def cell():
    articles = {}
    articles['heading'] = "This is the title"
    articles['paragraph'] = "This is the paragraph"
    articles['link'] = 'this is the link'
    Job = [articles]
    return render_template('blogger/Cell/index.html',Articles=Job)


#article display
@blog_print.route('/cell/<name>')
def p_article(name):
    try:
        return render_template(f'blogger/Cell/{name}')
    except FileNotFoundError:
        abort(404)
    

@blog_print.route('/plant/<name>')
def c_article(name):
    try:
        return render_template(f'blogger/Plant/{name}')
    except FileNotFoundError:
        abort(404)

@blog_print.route('/animal/<name>')
def b_article(name):
    try:
        return render_template(f'blogger/Animal/{name}')
    except FileNotFoundError:
        abort(404)

