import requests
from recommender.config import API_KEY, API_URL
import logging


class MobiliseApi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.url = API_URL
        self.auth_header = {"Authorization": "Bearer " + API_KEY}

    def shifts(self):
        response = requests.get(self.url + "/shifts", headers=self.auth_header)
        return response.json()

    def volunteers(self):
        response = requests.get(self.url + "/volunteers", headers=self.auth_header)
        return response.json()