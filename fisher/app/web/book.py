#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import jsonify
from flask import request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from app.forms.book import SearchForm

from . import web


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)


# @web.route('/')
# def test_root():
#     return 'test_root'
#
#
# @web.route('/test')
# def test_test():
#     return 'test_test'


