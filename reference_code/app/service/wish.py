"""
 Created by 七月 on 2017/12/15.
"""
from app.models.wish import Wish
from sqlalchemy import func
from app.models import db
from app.models.gift import Gift

__author__ = '七月'


class WishService:
    """
        Wish服务层
    """

    @classmethod
    def get_gifts_count(cls, wish_list):
        book_isbn_list = [wish.isbn for wish in wish_list]
        count_list = db.session.query(func.count(Gift.id), Gift.isbn). \
            filter(Gift.launched == False, Gift.isbn.in_(book_isbn_list), Gift.status == 1).all()
        return count_list
