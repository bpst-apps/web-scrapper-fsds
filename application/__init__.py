# import flask
from flask import Flask
from importlib import import_module


def register_blueprints(app):
    for module_name in ('home', 'image'):
        module = import_module(f'application.{module_name}.routes')
        app.register_blueprint(module.blueprint)


def create_app(config=''):
    # create flask application
    app = Flask(__name__)
    register_blueprints(app)
    return app
