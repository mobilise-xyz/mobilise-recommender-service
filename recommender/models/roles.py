from sqlalchemy.dialects.postgresql import VARCHAR
from recommender.database import db


class Roles(db.Model):
    __tablename__ = "Roles"
    __table_args__ = {'schema': 'public'}

    name = db.Column(VARCHAR, primary_key=True, nullable=False)
    # involves
    # createdAt
    # updatedAt
    # colour
