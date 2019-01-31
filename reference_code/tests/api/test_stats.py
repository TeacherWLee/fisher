from flask import json

from advancer.models.org.enroll import Enroll
from tests.api._base import TestOrgCase
from advancer.models.base import db


class TestStats(TestOrgCase):
    def test_get_student_stats_count(self):
        headers = self.get_authorized_header(scope='OrgAdmin')
        rv = self.client.get('v1/org/1/student/enroll/stats/count', headers=headers)
        self.assertEqual(rv.status_code, 200)
        # print(rv.jsonData)

    def test_get_sign_in_count_stats(self):
        headers = self.get_authorized_header(scope='OrgAdmin')
        rv = self.client.get('v1/org/1/student/sign-in/stats/count', headers=headers)
        self.assertEqual(rv.status_code, 200)
        # print(rv.jsonData)

    def get_sign_in_count_status_single(self):
        headers = self.get_authorized_header(scope='OrgAdmin')
        rv = self.client.get('v1/org/1/student/sign-in/2015-12-08/stats/count', headers=headers)
        self.assertEqual(rv.status_code, 200)
        # print(rv.jsonData)
