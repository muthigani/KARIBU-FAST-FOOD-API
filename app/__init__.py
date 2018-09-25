from flask import Flask
from flask_restful import Api, Resource, reqparse


'''importing local class'''
import config




def create_app(config_filename):
""" created create_app function so that the app run on __init__.py"""
    app = Flask(__name__)

    api = Api(app, prefix ='/api/v1')

    app.config.from_object('config')

""" import class resources from Views"""
    from app.api.v1.views import Order
    from app.api.v1.views import Order_list
    
 """" These are my API endpoints"""

    api.add_resource(Order, '/orders/<int:orderid>')
    api.add_resource(Order_list, '/orders')



    return app

