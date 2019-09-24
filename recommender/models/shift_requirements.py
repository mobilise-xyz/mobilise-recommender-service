from sqlalchemy.dialects.postgresql import UUID, INTEGER, TIMESTAMP
from recommender.app import db


class ShiftRequirements(db.Model):
    __tablename__ = "ShiftRequirements"
    __table_args__ = {'schema': 'public'}
    shiftId = db.Column(UUID(as_uuid=True), db.ForeignKey("public.Shifts.id"), unique=True, nullable=False,
                        primary_key=True)

    roleName = db.Column(INTEGER, db.ForeignKey("public.Roles.name"), primary_key=True)
    numberRequired = db.Column(INTEGER)
    createdAt = db.Column(TIMESTAMP)
    updatedAt = db.Column(TIMESTAMP)
    expectedShortage = db.Column(INTEGER)

    bookings = db.relationship("Bookings")
    roles = db.relationship("Roles")
