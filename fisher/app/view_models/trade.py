#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from models.user import User


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        __len__ = {int}
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d'),
        else:
            time = '未知'

        return dict(
            user_name=User.query.get(single.uid).nickname,
            time=time,
            id=single.id
        )
