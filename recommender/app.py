import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import logging

from recommender.config import ProductionConfig, DevelopmentConfig
from recommender.resources.recommendations import Recommendations


app = Flask(__name__)

if os.environ['FLASK_ENV'] == 'production':
    config = ProductionConfig()
else:
    config = DevelopmentConfig()
app.config.from_object(config)
db = SQLAlchemy(app)

api = Api(app)
api.add_resource(Recommendations, '/')

logging.basicConfig(level=logging.DEBUG)
