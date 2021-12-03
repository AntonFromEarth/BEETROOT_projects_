from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import my_cv_server
    #app.register_blueprint(my_cv_server.bp)
    app.register_blueprint(my_cv_server.bp)

    return app