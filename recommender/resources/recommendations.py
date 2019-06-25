from flask_restful import Resource

class Recompute(Resource):
    def post(self):
        print("Recomputing...")