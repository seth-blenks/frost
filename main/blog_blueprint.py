from flask import Blueprint

blog_print = Blueprint('blogger',__name__)

from .navigators import errors
from .navigators import views
