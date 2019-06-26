from flask import Flask
from flask_restful import Api
import logging

from recommender.resources.recommendations import Recommendations


app = Flask(__name__)

api = Api(app)
api.add_resource(Recommendations, '/')

logging.basicConfig(level=logging.DEBUG)
