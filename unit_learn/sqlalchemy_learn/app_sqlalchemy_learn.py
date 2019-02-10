#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_learn.models.base import db
from sqlalchemy_learn.spider.data import data
from sqlalchemy_learn.models.author import Author
from sqlalchemy_learn.models.author_detail import AuthorDetail
from sqlalchemy_learn.models.article import Article
from sqlalchemy_learn.models.tag import Tag


# ---------------- Flask App 创建与配置 ---------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:wlee0721@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()


# ---------------- SQLAlchemy 创建并配置 ----------------
db.init_app(app=app)


# ---------------- 演示功能配置 ----------------
demo_config = {
    'drop_all_tables': False,
    'create_all_tables': False,
    'fill_records': False,
    'query': True,
    'insert_record': False,
    'delete_record': False,
    'rollback': False
}


class SQLAlchemyDemo:
    def __init__(self, sqlalchemy_db, db_data, demo_config):
        self.db = sqlalchemy_db
        self.data = db_data
        self.config = demo_config

    def __drop_all_tables(self):
        self.db.drop_all()

    def __create_all_tables(self):
        self.db.create_all()

    def __fill_all_records(self):
        for foo in data:
            author = Author(name=foo['name'])
            author_detail = AuthorDetail(email=foo['email'], phone=foo['phone'])
            article = Article(title=foo['title'])
            for t in foo['tags']:
                tag = Tag(tag_title=t)
                article.tags.append(tag)
                self.db.session.add(tag)
            self.db.session.add(author)
            self.db.session.add(author_detail)
            self.db.session.add(article)
            self.db.session.commit()

        for foo in data:
            author = Author.query.filter_by(name=foo['name']).first()
            author_detail = AuthorDetail.query.filter_by(email=foo['email']).first()
            article = Article.query.filter_by(title=foo['title']).first()
            author.author_detail_id = author_detail.id
            article.author_id = author.id
            self.db.session.commit()

    def __query_demo(self):
        # 通过指定字段查询
        author_q1 = Author.query.filter_by(name='刘慈欣', status=0).first()
        print(author_q1)

        # 通过主键查询
        author_q2 = Author.query.get(1)
        print(author_q2)

        # 按某种规则对用户排序:
        author_q_order_1 = Author.query.order_by(Author.name).all()
        print(author_q_order_1)

        # 正向查询
        author1_obj = Author.query.filter_by(name='刘慈欣').first()
        print(author1_obj.author_detail.email)
        article1_obj = Article.query.get(1)
        print(article1_obj.tags)

        # 反向查询
        author_detail1_obj = AuthorDetail.query.filter_by(email='cixin@example.com').first()
        print(author_detail1_obj.author[0].name)

        # 链式调用
        author_q3 = Author.query.filter_by().order_by(Author.name).limit(3).all()
        print(author_q3)

        # 作者数量
        author_cnt = Author.query.filter_by(status=0).count()
        print(author_cnt)

    def __insert_record(self):
        author = Author(name='[日]村上春树')
        self.db.session.add(author)
        self.db.session.commit()

    def __delete_record(self):
        author = Author.query.filter_by(name='[日]村上春树').first()
        self.db.session.delete(author)
        self.db.session.commit()

    def __rollback(self):
        self.db.session.rollback()

    def start(self):
        if self.config['drop_all_tables']:
            self.__drop_all_tables()
        if self.config['create_all_tables']:
            self.__create_all_tables()
        if self.config['fill_records']:
            self.__fill_all_records()
        if self.config['query']:
            self.__query_demo()
        if self.config['insert_record']:
            self.__insert_record()
        if self.config['delete_record']:
            self.__delete_record()
        if self.config['rollback']:
            self.__rollback()


if __name__ == '__main__':
    sqlalchemy_demo = SQLAlchemyDemo(sqlalchemy_db=db, db_data=data, demo_config=demo_config)
    sqlalchemy_demo.start()
