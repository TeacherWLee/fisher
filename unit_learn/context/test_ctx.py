#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import Flask, current_app

app = Flask(__name__)


ctx = app.app_context()
ctx.push()

a = current_app
b = current_app.config['DEBUG']
print(b)
ctx.pop()

with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']
    print(b)
