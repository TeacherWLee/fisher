from tests.api._base import TestOrgCase

__author__ = 'bliss'


class TestTag(TestOrgCase):

    def test_tag_query(self):
        type_id = '100'
        headers = self.get_authorized_header()
        rv = self.client.get('/v1/tag/' + type_id, headers=headers)
        self.assertEqual(rv.status_code, 200)