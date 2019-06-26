from dataclasses import dataclass
import datetime
from typing import List

import requests
from recommender.config import API_KEY, API_URL
import logging


# Representation of resources. Do not contain all fields - refer to API documentation.
# TODO these aren't actually used right now.


@dataclass
class Volunteer:
    availability: List[List[float]]


@dataclass
class Booking:
    shiftId: str


@dataclass
class Requirement:
    numberRequired: int
    bookings: List[Booking]


@dataclass
class Shift:
    id: str
    date: datetime.date
    start: datetime.time
    stop: datetime.time
    requirements: List[Requirement]


class MobiliseApi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.url = API_URL
        self.auth_header = {"Authorization": "Bearer " + API_KEY}

    def shifts(self):
        shifts_json = requests.get(self.url + "/shifts", headers=self.auth_header).json()
        # return self._parse_shifts(shifts_json)
        return shifts_json

    def _parse_requirements(self, requirements_json) -> List[Requirement]:
        self.logger.debug(requirements_json)
        return [Requirement(numberRequired=requirement["numberRequired"], bookings=requirement["bookings"]) for
                requirement in
                requirements_json]

    def _parse_shifts(self, shifts_json) -> List[Shift]:
        return [Shift(id=shift["id"], date=shift["date"], start=shift["start"], stop=shift["stop"],
                      requirements=self._parse_requirements(shift["requirements"])) for shift in shifts_json]

    def volunteers(self):
        response = requests.get(self.url + "/volunteers", headers=self.auth_header)
        return response.json()
