from recommender.config import API_KEY, API_URL
from recommender.app import db

import logging

from typing import Dict, Tuple

from recommender.models.shifts import Shifts
from recommender.models.shift_requirements import ShiftRequirements
from recommender.models.bookings import Bookings
from recommender.models.volunteers import Volunteers
from recommender.models.roles import Roles


class MobiliseApi:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.url = API_URL
        self.auth_header = {"Authorization": "Bearer " + API_KEY}

    def shifts(self):
        shifts_rows = Shifts.query.all()

        self.logger.info(dir(shifts_rows[0]))
        return shifts_rows

    def volunteers(self):
        volunteer_rows = Volunteers.query.all()

        self.logger.info(volunteer_rows)
        return volunteer_rows

    def write_expected_shortages(self, new_requirements: Dict[Tuple[str, str], float]):
        """Writes to the ShiftRequirements table"""
        self.logger.info(f"Writing expected shortages: {new_requirements}")

        shift_requirements_rows = ShiftRequirements.query.all()

        for requirement in shift_requirements_rows:
            requirement.expectedShortage = new_requirements[(requirement.shiftId, requirement.roleName)]

        db.session.commit()

        self.logger.info("Successfully wrote new shift expected shortages")
