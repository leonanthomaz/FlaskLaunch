# app/web/__init__.py

from flasklaunch import Blueprint
from .views import index

bp = Blueprint("web", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)

def init_app(app):
    app.register_blueprint(bp)
