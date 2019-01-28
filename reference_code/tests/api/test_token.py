from tests.api._base import TestUserCSUCase

__author__ = 'bliss'

import json, time


class TestToken(TestUserCSUCase):
    def test_get_token(self):
        """Token：CSU用户通过账号密码获取令牌"""
        data = json.dumps({
            'account': '17777777777',
            'secret': '123123',
            'type': '200'
        })

        rv = self.client.post('/v1/token', data=data)
        assert rv.status_code == 201

    def test_csu_get_token_by_social(self):
        """Token:CSU第三方登录用户的令牌获取"""
        data = json.dumps({
            'account': 'openid',
            'secret': '',
            'type': 230
        })

        rv = self.client.post('/v1/token', data=data)
        assert rv.status_code == 201

        data = json.dumps({
            'account': 'openid',
            'type': 230
        })
        rv = self.client.post('/v1/token', data=data)
        assert rv.status_code == 201

    def test_token_expired(self):
        """Token:是否按时过期"""
        headers = self.get_authorized_header(expiration=1)
        time.sleep(3)
        rv = self.client.get('/v1/test/auth', headers=headers)
        assert rv.status_code == 401
        assert b'1003' in rv.data


