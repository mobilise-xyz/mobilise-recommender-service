from datetime import time
from typing import List, Dict, Tuple
import logging

from recommender.mobiliseapi import MobiliseApi

import numpy as np

# Constant estimating the number of available volunteers that will book.
P_BOOK = 0.3


class ShiftRecommenderEngine:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.api = MobiliseApi()

    def recommendations(self):
        """Calculates recommendations"""
        recommendations = self._compute_expected_shortages()
        self.logger.info(f"Returning recommendations: {recommendations}")
        return recommendations

    def write_recommendations(self) -> None:
        """Writes the result of the recommender to the database"""
        recommendations = self.recommendations()
        # Use the shiftId + roleName (PK) to update the expectedShortage value.
        self.api.write_expected_shortages(recommendations)

    def _compute_cumulative_availability(self) -> List[List[float]]:
        availabilities = [np.asarray(v.availability, dtype=np.float64) for v in self.api.volunteers()]
        cumulative_availability = sum(availabilities)

        # This typecast is mainly so the type hinting works as expected
        return list(cumulative_availability.tolist())

    @staticmethod
    def _get_slot_for_time(shift_time: time) -> int:
        if shift_time < time(12, 00, 00):
            return 0
        elif shift_time > time(16, 00, 00):
            return 2
        else:
            return 1

    def _compute_predicted_bookings(self, shift, requirement) -> float:
        cumulative_availability = self._compute_cumulative_availability()

        n_booked = len(requirement.bookings)

        day_of_week = shift.date.weekday()
        time_slot = self._get_slot_for_time(shift.start)

        predicted_bookings = cumulative_availability[day_of_week][time_slot] - n_booked * P_BOOK

        return predicted_bookings

    def _compute_expected_shortages(self) -> Dict[Tuple[str, str], float]:
        self.logger.info("Computing expected shortages")

        shifts = self.api.shifts()

        self.logger.info(f"Shifts: {shifts}")

        expected_shortages: Dict[Tuple[str, str], float] = {}

        for shift in shifts:
            for requirement in shift.requirements:
                remaining_spaces = requirement.numberRequired - len(requirement.bookings)
                n_booked = len(requirement.bookings)
                predicted_bookings = self._compute_predicted_bookings(shift, requirement)

                role_name = requirement.roleName

                expected_shortages[
                    (shift.id, role_name)] = remaining_spaces - n_booked - predicted_bookings

        return expected_shortages
