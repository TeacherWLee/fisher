from flask import json
from tests.api._base import TestOrgCase

__author__ = 'bliss'


class TestOrgGroup(TestOrgCase):
    def test_org_group_create(self):
        data = {
            'organization_id': 1,
            'title': '分组1'
        }
        json_data = json.dumps(data)
        headers = self.get_authorized_header()
        rv = self.client.post('v1/org/lecture/group', data=json_data, headers=headers)
        self.assertEqual(201, rv.status_code)

    def test_org_group_delete(self):
        pass
