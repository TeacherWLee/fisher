from tests.api._base import TestOrgCase
from flask import json
__author__ = 'shaolei'


class TestFeedback(TestOrgCase):

    def test_feedback_add(self):
        feedback_info = {
            'organization_id': 2,
            'qq': '1173838760',
            'content': '闪退'
        }
        headers = self.get_authorized_header(scope='OrgAdmin')
        feedback_json = json.dumps(feedback_info)
        rv = self.client.post('v1/org/feedback/advice', data=feedback_json, headers=headers)
        self.assertEqual(rv.status_code, 201)
