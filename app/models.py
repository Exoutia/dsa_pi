from sqlalchemy import Column, Integer, String

from .database import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    link = Column(String)
    solution_link = Column(String)

