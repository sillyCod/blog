from flask import Flask
from blog.views import article_bp



def create_app():
    app = Flask(__name__)
    app.register_blueprint(article_bp, url_prefix="/article")
    return app


if __name__ == "__main__":
    app = create_app()
    print(app.url_map)
    app.run()