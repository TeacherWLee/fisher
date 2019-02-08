#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Author(BaseModel):
    name = Column(String(20), nullable=False)
    author_detail_id = Column(Integer, ForeignKey('author_detail.id'))
    author_detail = relationship('AuthorDetail', backref='author', uselist=False)
