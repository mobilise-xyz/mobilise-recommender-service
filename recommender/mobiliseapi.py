from recommender.database import db

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

    def shifts(self):
        self.logger.info("Retrieving shifts")
        return Shifts.query.all()

    def volunteers(self):
        self.logger.info("Retrieving volunteers")
        return Volunteers.query.all()

    def write_expected_shortages(self, new_requirements: Dict[Tuple[str, str], float]):
        """Writes to the ShiftRequirements table"""
        self.logger.info(f"Writing expected shortages: {new_requirements}")

        shift_requirements_rows = ShiftRequirements.query.all()

        for requirement in shift_requirements_rows:
            requirement.expectedShortage = new_requirements[(requirement.shiftId, requirement.roleName)]

        db.session.commit()

        self.logger.info("Successfully wrote new shift expected shortages")
