#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from .base import BaseModel


class Tag(BaseModel):
    id = Column(Integer, primary_key=True)
    tag_title = Column(String(20), nullable=False)
