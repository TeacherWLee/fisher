#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from flask import Flask
from app.models.book import db

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
