#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .base import BaseModel, db
from .article_tag import article_tag_table


class Article(BaseModel):
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey('author.id'))

    author = relationship('Author', backref='article')
    tags = relationship('Tag', backref='article', secondary=article_tag_table)
