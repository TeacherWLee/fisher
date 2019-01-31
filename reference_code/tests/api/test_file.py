import json
from tests.api._base import TestCase

__author__ = 'bliss'


class TestFile(TestCase):
    def test_create_qrcode(self):
        data = {
            "url": "http://map.baidu.com/?newmap=1&s=con%26wd%3D%E6%AD"
                   "%A6%E6%B1%89%E4%B8%9C%E6%9D%A5%E9%A1%BA%26c%3D218&from=alamap&tpl=mapdots"
        }
        json_str = json.dumps(data)
        rv = self.client.post('v1/file/qrcode', data=json_str)
        self.assertEqual(rv.status_code, 201)
