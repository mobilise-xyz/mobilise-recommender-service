import logging

from recommender.mobiliseapi import MobiliseApi
import numpy as np


class ShiftRecommenderEngine:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api = MobiliseApi()

    def recommendations(self):
        return self._compute_cumulative_availability()

    def _compute_cumulative_availability(self):
        availabilities = [np.asarray(v["availability"], dtype=np.float64) for v in self.api.volunteers()]

        cumulative_availability = sum(availabilities)
        return cumulative_availability.tolist()

    def _compute_expected_shortages(self):
        pass


