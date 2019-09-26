from sqlalchemy.dialects.postgresql import UUID, DATE, TIMESTAMP
from recommender.database import db


class Shifts(db.Model):
    __tablename__ = "Shifts"
    __table_args__ = {'schema': 'public'}
    id = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)

    # title
    # description
    date = db.Column(DATE)
    start = db.Column(TIMESTAMP)
    # stop
    # address
    # createdAt
    # updatedAt
    # creatorId
    # repeatedId

    requirements = db.relationship("ShiftRequirements")
