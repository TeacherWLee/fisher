from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.base import db


class Test(db.Model):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    test = Column(Integer,default=1)

class Test1():
    test = 0


