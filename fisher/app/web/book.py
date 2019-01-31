#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


from flask import jsonify
from flask import Blueprint

from helper import is_isbn_or_key
from yushu_book import YuShuBook


web = Blueprint('web', __name__)


#@web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search(q, page):
    return 'test_search'
    # isbn_or_key = is_isbn_or_key(q)
    # if isbn_or_key == 'isbn':
    #     result = YuShuBook.search_by_isbn(q)
    # else:
    #     result = YuShuBook.search_by_keyword(q)
    # return jsonify(result)


@web.route('/')
def test_root():
    return 'test_root'

@web.route('/test')
def test_test():
    return 'test_test'
