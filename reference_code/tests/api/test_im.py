# -*- coding: utf-8 -*-
import json
import unittest
import requests
from advancer.libs.lean_cloud_system_message import LeanCloudSystemMessage


class TestIm(unittest.TestCase):

    # 创建群组
    # def test_create_im_group(self):
    #     body_data = {
    #         "group_name": '测试群02',
    #         "member_client_ids": ['c001'],
    #         "organization_id": 2,
    #         #"conversation_id": '000121',
    #         "group_avatar": 'http://test.jpg',
    #         "description": '单元测试时创建的群',
    #         "admin_uid": 'c565'
    #     }
    #     resp = requests.post('http://localhost:5000/v1/im/group', data=json.dumps(body_data))
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 201)
    #
    # # 修改群名称
    # def test_update_im_group_name(self):
    #     body_data = {
    #         "group_name": '修改后的群名称'
    #     }
    #     resp = requests.put('http://localhost:5000/v1/im/group/16', data=json.dumps(body_data))
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 200)
    #
    # # 删除群
    # def test_delete_im_group(self):
    #     resp = requests.delete('http://localhost:5000/v1/im/group/16')
    #     self.assertEqual(resp.status_code, 204)
    #
    # # 群主解散群
    # def test_dismiss_im_group(self):
    #     resp = requests.delete('http://localhost:5000/v1/im/user/o123/group/16')
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 204)
    #
    # # 添加群成员
    # def test_add_im_group_member(self):
    #     body_data = {
    #         "member_client_ids": "c01:c02"
    #     }
    #     resp = requests.post('http://localhost:5000/v1/im/group/27/member', data=json.dumps(body_data))
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 201)
    #
    # # 移除群成员
    def test_delete_im_group_member(self):
        body_data = {
            "member_client_ids": "c01"
        }
        resp = requests.delete('http://localhost:5000/v1/im/group/27/member', data=json.dumps(body_data))
        print(resp.text)
        self.assertEqual(resp.status_code, 204)
    #
    # # 向班级群发通知
    # def test_send_message_to_class(self):
    #     resp = requests.post('http://localhost:5000/v1/im/org/5/message')
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 201)
    #
    # # 用户加群通知
    # def test_im_user_join_group_notification(self):
    #     resp = requests.post('http://localhost:5000/v1/im/user/c63/group/16/join_group_notification')
    #     print(resp.text)
    #     self.assertEqual(resp.status_code, 201)

    # 系统消息调试
    # def test_tmp_sys_message(self):
    #     message_content = {
    #         "_lctype": 1,
    #         "_lctext": "XXX 被移出群聊",
    #         "_lcattrs": {
    #             "message_info": "XXX 被移出群聊",
    #             "sys_message_type": "removed_from_group",
    #             "uid": "c102",
    #             "gid": 12,
    #             "member_client_ids": ["c001", "c002"]
    #         }
    #     }
    #     message_content = json.dumps(message_content)
    #     body_data = {
    #         "from_peer": "c558",
    #         "message": message_content,
    #         "to_peers": ["c565", "c558"],
    #         "conv_id": "568a17a160b27e9b19579a6f",
    #         "transient": True,
    #         "no_sync": True
    #     }
    #     body_data = json.dumps(body_data)
    #     print(body_data)
    #     code, resp = LeanCloudSystemMessage.send_system_message(body_data)
    #     print(code, resp)
