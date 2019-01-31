import unittest
from flask import app
from advancer.libs.jpush import JPushService
from advancer.service.im import get_reg_id_by_client_id

__author__ = 'yangchujie'


class TestImPush(unittest.TestCase):

    def test_im_user_removed_from_group(self):
        """
        :return: b'{"sendno":"12345","msg_id":"2418821557"}'
        """
        JPushService.push_removed_from_group_message('0813a6507f0')

    # def test_im_user_added_to_group_message(self):
    #     """
    #     :return: b'{"sendno":"12345","msg_id":"705279095"}'
    #     """
    #     JPushService.push_added_to_group_message('0813a6507f0')
    #
    # def test_im_group_info_been_modified_message(self):
    #     """
    #     :return: b'{"sendno":"12345","msg_id":"1533293858"}'
    #     """
    #     JPushService.push_group_info_been_modified_message('0813a6507f0')
