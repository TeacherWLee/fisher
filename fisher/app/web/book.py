#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
