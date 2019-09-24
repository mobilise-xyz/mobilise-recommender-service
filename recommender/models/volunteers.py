from sqlalchemy.dialects.postgresql import UUID, ARRAY, INTEGER, CHAR
from recommender.app import db


class Volunteers(db.Model):
    __tablename__ = "Volunteers"
    __table_args__ = {'schema': 'public'}
    userId = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)

    roles = db.Column(ARRAY(INTEGER))
    # createdAt
    # updatedAt
    availability = db.Column(ARRAY(CHAR))
    # lastWeekShifts
    # lastWeekHours
    # lastWeekIncrease
