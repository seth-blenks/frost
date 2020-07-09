from ..blog_blueprint import blog_print
from flask import render_template,abort,g,url_for

@blog_print.app_errorhandler(404)
def filenotfound(e):
    return render_template('blogger/404.html'),404