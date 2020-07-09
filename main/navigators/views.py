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
    return render_template('blogger/about.html')


@blog_print.route('/terms_and_conditions')
def terms_and_conditions():
    return render_template('blogger/terms.html')

@blog_print.route('/favicon.ico')
def banner():
    image = b''
    with open('static/images/favicon.ico','rb') as r_file:
        image = r_file.read()
    return image



@blog_print.route('/programming')
def programming():
    
    return render_template('blogger/Programming/index.html')

@blog_print.route('/chemistry')
def animal():
    
    return render_template('blogger/Chemistry/index.html')

@blog_print.route('/biology')
def cell():
    
    return render_template('blogger/Biology/index.html')


#article display
@blog_print.route('/biology/<name>')
def p_article(name):
    try:
        return render_template(f'blogger/Biology/{name}')
    except TemplateNotFound:
        print('here')
        abort(404)
    

@blog_print.route('/programming/<name>')
def c_article(name):
    try:
        return render_template(f'blogger/Programming/{name}')
    except TemplateNotFound:
        abort(404)

@blog_print.route('/chemistry/<name>')
def b_article(name):
    try:
        return render_template(f'blogger/Chemistry/{name}')
    except TemplateNotFound:
        abort(404)

