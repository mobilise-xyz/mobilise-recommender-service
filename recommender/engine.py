from datetime import datetime, time
import logging
from typing import List, Iterable, Dict, Any, Union

from recommender.mobiliseapi import MobiliseApi
import numpy as np

# Constant estimating the number of available volunteers that will book.
P_BOOK = 0.3


class ShiftRecommenderEngine:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.api = MobiliseApi()

    def recommendations(self):
        return self._compute_expected_shortages()

    def _compute_cumulative_availability(self) -> List[List[float]]:
        availabilities = [np.asarray(v["availability"], dtype=np.float64) for v in self.api.volunteers()]
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

        n_booked = len(requirement["bookings"])

        day_of_week = datetime.strptime(shift["date"], "%Y-%m-%d").weekday()
        time_slot = self._get_slot_for_time(datetime.strptime(shift["start"], "%H:%M:%S").time())

        predicted_bookings = cumulative_availability[day_of_week][time_slot] - n_booked * P_BOOK

        return predicted_bookings

    def _compute_expected_shortages(self) -> List[Dict[str, Union[float, str]]]:
        shifts = self.api.shifts()

        expected_shortages: List[Dict[str, Union[float, str]]] = []

        for shift in shifts:
            shift_expected_shortages = {}
            for requirement in shift["requirements"]:
                remaining_spaces = requirement["numberRequired"] - len(requirement["bookings"])
                n_booked = len(requirement["bookings"])
                predicted_bookings = self._compute_predicted_bookings(shift, requirement)

                role_name = requirement["role"]["name"]

                shift_expected_shortages["shiftId"] = shift["id"]
                shift_expected_shortages["roleName"] = role_name
                shift_expected_shortages["expectedShortage"] = remaining_spaces - n_booked - predicted_bookings

                expected_shortages.append(shift_expected_shortages)

        return expected_shortages
