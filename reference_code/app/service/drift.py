"""
 Created by 七月 on 2017/12/15.
"""
from app.models import db
from app.models.drift import Drift
from app.view_models.book import BookViewModel
from flask_login import current_user
from app.libs.email import send_email

__author__ = '七月'


class DriftService:
    """
        Wish服务层
    """

    @classmethod
    def save_a_drift(cls, drift_form, current_gift):
        with db.auto_commit():
            book = BookViewModel(current_gift.book.first)

            drift = Drift()
            drift_form.populate_obj(drift)
            drift.gift_id = current_gift.id
            drift.requester_id = current_user.id
            drift.requester_nickname = current_user.nickname
            drift.gifter_nickname = current_gift.user.nickname
            drift.gifter_id = current_gift.user.id
            drift.book_title = book.title
            drift.book_author = book.author
            drift.book_img = book.image
            drift.isbn = book.isbn
            # 当请求生成时，不需要让这个礼物处于锁定状态
            # 这样赠送者是可以收到多个索取请求的，由赠送者选择送给谁
            # current_gift.launched = True
            # 请求者鱼豆-1
            current_user.beans -= 1
            # 但是赠送者鱼豆不会立刻+1
            # current_gift.user.beans += 1
            db.session.add(drift)
        send_email(current_gift.user.email, '有人想要一本书', 'email/get_gift',
                   wisher=current_user,
                   gift=current_gift)
