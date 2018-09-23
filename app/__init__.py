from flask import Flask
from flask_restful import Api, Resource, reqparse

import config




def create_app(config_filename):
    app = Flask(__name__)

    api = Api(app, prefix ='/api/v1')

    app.config.from_object('config')


    from app.api.v1.views import Order
    from app.api.v1.views import Order_list

    api.add_resource(Order, '/orders/<int:orderid>')
    api.add_resource(Order_list, '/orders')



    return app

