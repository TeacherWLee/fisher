#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger
from sqlalchemy.orm import relationships

from app.models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
