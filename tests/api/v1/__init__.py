from flask import Flask
from flask_restful import Api, Resource, reqparse

import config




def create_app(config_filename):
    app = Flask(__name__)

    api = Api(app, prefix ='/api/v1')

    app.config.from_object('config')