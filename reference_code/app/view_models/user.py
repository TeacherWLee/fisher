"""
 Created by 七月 on 2017/12/16.
"""
__author__ = '七月'

from collections import namedtuple

# UserSummary = namedtuple('UserSummary', ['nickname', 'beans', 'send_receive'])


class UserSummary:
    @classmethod
    def user(cls, user):
        return dict(
            nickname=user.nickname,
            beans=user.beans,
            email=user.email,
            send_receive=str(user.send_counter) + '/' + str(user.receive_counter)
        )
