import logging

from flask_restful import Resource
from recommender.engine import ShiftRecommenderEngine


class Recommendations(Resource):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.engine = ShiftRecommenderEngine()

    def post(self):
        # TODO(sonjoonho): Authentication
        self.logger.debug("Recomputing")
        return self.engine.recommendations()
