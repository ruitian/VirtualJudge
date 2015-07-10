from flask import Blueprint
from .index import IndexView

bp_index = Blueprint('index', __name__)

bp_index.add_url_rule(
    '',
    view_func = IndexView.as_view('index'),
    methods = ['GET']
)
