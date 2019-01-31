#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import Blueprint


web = Blueprint('web', __name__)


from app.web import book
from app.web import user
