from tests.api._base import TestUserCSUCase

from advancer.models.mall.order_duiba import OrderDuiBa


__author__ = 'bliss'

import time
from advancer.libs.httper import Httper
from advancer.models.base import db
from advancer.models.user.user_csu_credit_dynamic import UserCSUCreditDynamic
from advancer.models.user.user_csu import UserCSU


class TestMall(TestUserCSUCase):

    def test_create_order_duiba(self):
        """商城：积分的扣除是否正常"""

        get_params = ("?uid=1&orderNum=order-for-test-1447670790415&"
                      "credits=1000&params=15045678901&type=phonebill&"
                      "paramsTest10=10&ip=192.168.1.100&sign=4ae02d3ac2e007f877b8912361445780&"
                      "timestamp=1447670790415&waitAudit=true&actualPrice=1000&"
                      "description=%E6%89%8B%E6%9C%BA%E5%8F%B7%3A15045678901+%E5%85%85%E5%80%BC10%E5%85%83&"
                      "facePrice=1000&appKey=tLCk6CH9b3deXPbedS8TEfmLbnR&")

        with self.subTest():
            # 测试当参数被修改时是否会正确提示
            wrong_sign_params = get_params+'name=33'
            url_w_sign = '/v1/mall/duiba/order' + wrong_sign_params
            r_w = self.client.get(url_w_sign)
            assert r_w.status_code == 400 and b'999' in r_w.data

        user_score = db.session.query(UserCSU.score).filter_by(uid=1).first()
        url = '/v1/mall/duiba/order'+get_params
        rv = self.client.get(url)

        # 正确返回200
        assert rv.status_code == 200

        # 测试分数充足时，是否正确的扣除了用户的分数
        user_score_after = db.session.query(UserCSU.score).filter_by(uid=1).first()
        assert user_score_after[0] == user_score[0] - 1000

        # 是否正确的加入了积分动态
        user_dynamic_credit = db.session.query(UserCSUCreditDynamic.credit_dynamic,
                                               UserCSUCreditDynamic.left_credit).first()
        dynamic_credit = user_dynamic_credit[0]
        left_credit = user_dynamic_credit[1]
        assert dynamic_credit == -1000
        assert left_credit == user_score_after[0]

    def test_create_order_create_time(self):
        """商城：两次订单的创建时间是否不一样"""
        get_params = ("?uid=1&orderNum=order-for-test-1447670790415&"
                      "credits=1000&params=15045678901&type=phonebill&"
                      "paramsTest10=10&ip=192.168.1.100&sign=4ae02d3ac2e007f877b8912361445780&"
                      "timestamp=1447670790415&waitAudit=true&actualPrice=1000&"
                      "description=%E6%89%8B%E6%9C%BA%E5%8F%B7%3A15045678901+%E5%85%85%E5%80%BC10%E5%85%83&"
                      "facePrice=1000&appKey=tLCk6CH9b3deXPbedS8TEfmLbnR&")

        url = '/v1/mall/duiba/order'+get_params
        rv = self.client.get(url)
        assert rv.status_code == 200

        time.sleep(2)

        rv1 = self.client.get(url)
        assert rv1.status_code == 200

        dynamic_credits = UserCSUCreditDynamic.query.filter_by(uid=1).all()
        orders = OrderDuiBa.query.filter_by(uid=1).all()
        self.assertEqual(len(dynamic_credits), 2)
        self.assertEqual(len(orders), 2)
        self.assertNotEqual(dynamic_credits[0].create_time, dynamic_credits[1].create_time)
        self.assertNotEqual(orders[0].create_time, orders[1].create_time)

    def test_create_order_duiba_not_enough_coin(self):
        """商城：积分不足时候的扣分情况
        uid=2 只有300分
        """

        get_params = ("?uid=2&paramsTest32=32&orderNum=order-for-test-1447732196174&"
                      "credits=1000&params=15045678901&type=phonebill&ip=192.168.1.100&"
                      "sign=3680acf95d90232d406b7eb52b44eb83&timestamp=1447732196174&"
                      "waitAudit=true&actualPrice=1000&"
                      "description=%E6%89%8B%E6%9C%BA%E5%8F%B7%3A15045678901+%E5%85%85%E5%80%BC10%E5%85%83&"
                      "facePrice=1000&appKey=tLCk6CH9b3deXPbedS8TEfmLbnR&")

        user_score = db.session.query(UserCSU.score).filter_by(uid=2).first()
        url = '/v1/mall/duiba/order'+get_params
        rv = self.client.get(url)

        # 当积分不足时返回码是400
        assert rv.status_code == 400

        # 当积分不足时，用户积分不应该被扣除
        user_score_after = db.session.query(UserCSU.score).filter_by(uid=2).first()
        assert user_score_after[0] == user_score[0]
        assert user_score_after[0] == 300

        # 用户的积分动态也不应该生成，应该为None
        user_dynamic_credit = db.session.query(UserCSUCreditDynamic.credit_dynamic,
                                               UserCSUCreditDynamic.left_credit).first()
        assert user_dynamic_credit is None

    def test_update_order_duiba(self):
        pass

    def test_redirect_to_duiba(self):
        """商城：生成免登录Url后重定向到兑吧"""
        headers = self.get_authorized_header(scope='UserCSU')
        rv = self.client.get('/v1/mall/duiba/index', headers=headers)
        http = Httper()

        r_redirect = http.get(rv.location)

        assert r_redirect.status == 200

