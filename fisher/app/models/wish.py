#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

from spider.yushu_book import YuShuBook

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, SmallInteger, desc, func
from sqlalchemy.orm import relationships

from app.models.base import Base, db


class Wish(Base):
    __table_args__ = {"useexisting": True}
    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_count(cls, isbn_list):
        from models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched==False,
                                      Gift.isbn.in_(isbn_list),
                                      Gift.status==1).group_by(
            Gift.isbn).all()
        count_dict = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_dict

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
