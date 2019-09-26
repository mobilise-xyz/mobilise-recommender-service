import unittest
from flask import Flask
from flask_restful import Api
from recommender.resources.recommendations import Recommendations


class TestRecommendations(unittest.TestCase):

    def test_bad_key(self):
        app = Flask(__name__)
        app.config["COMPUTATION_KEY"] = ""
        api = Api(app)
        api.add_resource(Recommendations, '/')

        with app.test_client() as client:
            self.assertEqual(client.post('/').status_code, 401)
