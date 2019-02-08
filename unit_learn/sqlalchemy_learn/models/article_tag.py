#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from sqlalchemy import Column, Integer, ForeignKey
from .base import db


article_tag_table = db.Table('art_tag',
                             Column('art_id', Integer, ForeignKey('article.id')),
                             Column('tag_id', Integer, ForeignKey('tag.id'))
                             )
