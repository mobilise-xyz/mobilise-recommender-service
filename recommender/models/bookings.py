from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP, VARCHAR
from recommender.database import db


class Bookings(db.Model):
    __tablename__ = "Bookings"
    __table_args__ = {'schema': 'public'}
    shiftId = db.Column(UUID(as_uuid=True), db.ForeignKey("public.ShiftRequirements.shiftId"), unique=True,
                        nullable=False,
                        primary_key=True)

    volunteerId = db.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
    roleName = db.Column(VARCHAR)
    createdAt = db.Column(TIMESTAMP)
    updatedAt = db.Column(TIMESTAMP)
    repeatedId = db.Column(UUID(as_uuid=True))
