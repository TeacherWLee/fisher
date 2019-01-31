from tests.api._base import TestOrgCase

__author__ = 'bliss'


class TestOrgNews(TestOrgCase):
    def test_org_news_paging(self):
        """News：对Org的新闻查询接口做测试"""
        url = '/v1/org/news?page=1&count=2'
        headers = self.get_authorized_header(scope='OrgAdmin')
        rv = self.client.get(url, headers=headers)
        self.assertEqual(rv.status_code, 200)