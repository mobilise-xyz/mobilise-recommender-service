import logging

from flask_restful import Resource, reqparse, abort
from flask import current_app
from recommender.engine import ShiftRecommenderEngine


class Recommendations(Resource):
    def __init__(self):

        self.parser = reqparse.RequestParser()
        self.parser.add_argument('key', type=str, help="Computation key")

        self.logger = logging.getLogger(__name__)

        self.engine = ShiftRecommenderEngine()

    def post(self):
        args = self.parser.parse_args()
        if args["key"] != current_app.config['COMPUTATION_KEY']:
            abort(401)

        self.logger.info("=== Recomputing ===")
        try:
            self.engine.write_recommendations()
        except Exception:
            return "There was a problem computing recommendations", 500
        return "Computation successful"
