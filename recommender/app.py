import os

from flask import Flask
from flask_restful import Api
from recommender.config import ProductionConfig, DevelopmentConfig

from recommender.database import db

import logging

app = Flask(__name__)

if os.environ['FLASK_ENV'] == 'production':
    config = ProductionConfig()
else:
    config = DevelopmentConfig()
app.config.from_object(config)

db.init_app(app)

from recommender.resources.recommendations import Recommendations

api = Api(app)
api.add_resource(Recommendations, '/')

logging.basicConfig(level=logging.DEBUG)
