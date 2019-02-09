#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from flask_login import current_user

from models.gift import Gift
from models.wish import Wish
from view_models.trade import TradeInfo

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import jsonify
from flask import request
from flask import render_template
from flask import flash
import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.book import SearchForm
from app.view_models.book import BookCollection, BookViewModel

from . import web


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')

    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False
    # 取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # if current_user.is_authoenticated:
    if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
        has_in_gifts = True
    if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
        has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template(
        'book_detail.html',
        book=book,
        wishes=trade_wishes_model,
        gifts=trade_gifts_model,
        has_in_gifts=has_in_gifts,
        has_in_wishes=has_in_wishes
    )


@web.route('/unit_learn')
def test():
    r = {
        'name': 'LW',
        'age': 16
    }
    flash('hello flash message.')
    return render_template('test.html', data=r)
