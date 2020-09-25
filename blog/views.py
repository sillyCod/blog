from flask.blueprints import Blueprint


article_bp = Blueprint("article", __name__)


@article_bp.route("/list")
def articles():
    return list()

