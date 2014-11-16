
import os

import flask

def make_app():
    app = flask.Flask('tstflask')

    @app.route("/")
    def home_page():
        return "<h1 class='handler-header'>welcome</h1>"

    return app

