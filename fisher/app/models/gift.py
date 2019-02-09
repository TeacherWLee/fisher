#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from flask import current_app

from models.wish import Wish
from spider.yushu_book import YuShuBook

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func
from sqlalchemy.orm import relationships
from app.models.base import Base, db


class Gift(Base):
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_count(cls, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched==False,
                                      Wish.isbn.in_(isbn_list),
                                      Wish.status==1).group_by(
            Wish.isbn).all()
        count_dict = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_dict

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        recent_gift = Gift.query.filter_by(
                    launched=False).group_by(
                    Gift.isbn).order_by(
                    desc(Gift.create_time)).limit(
                    current_app.config['RECENT_BOOK_COUNT']).all()
        # recent_gift = Gift.query.filter_by(
        #     launched=False).limit(current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
