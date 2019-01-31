#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from flask import Flask

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
