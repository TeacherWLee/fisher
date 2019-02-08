#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(db.Integer, primary_key=True)
    status = Column(db.Integer, nullable=False, default=0)
