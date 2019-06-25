from flask import Flask
from flask_restful import Api
import logging

from recommender.resources.recommendations import Recommendations


app = Flask(__name__)

# config_object = ProductionConfig if get_env_variable("FLASK_ENV") != "development" else DevelopmentConfig

# app.config.from_object(config_object)

# db = SQLAlchemy(app)

api = Api(app)
api.add_resource(Recommendations, '/')

logging.basicConfig(level=logging.DEBUG)
