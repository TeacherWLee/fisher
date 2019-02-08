#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

__author__ = 'Wei Li (liw@sicnu.edu.cn)'


class BookViewModel:
    def __init__(self, book):
        print(book)
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.isbn = book['isbn']
        self.image = book['image']

    def intro(self):
        intros = list(filter(lambda x: True if x else False, [self.author, self.publisher, self.price]))
        return ' / '.join(intros)


book = {'title': '挪威的森林',
        'author': ['[日]村上春树'],
        'publisher': '上海译文出版社',
        'price': '18.80元',
        'pages': '350',
        'summary': '这是一部动人心弦的、平缓舒雅的、略带感伤的恋爱小说。',
        'isbn': '9787532725694',
        'image': 'img'}


bv = BookViewModel(book)
i = bv.intro()
print(i)

