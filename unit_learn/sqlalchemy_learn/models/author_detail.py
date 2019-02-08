#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from .base import BaseModel


class AuthorDetail(BaseModel):
    id = Column(Integer, primary_key=True)
    email = Column(String(50))
    phone = Column(String(50))
