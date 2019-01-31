from flask import json

from advancer.models.org.teacher_group import TeacherGroup
from tests.api._base import TestOrgCase
from advancer.models.base import db

class TestLecture(TestOrgCase):

   def test_create_teacher_group(self):
      """Info：测试老师分组的添加"""

      headers = self.get_authorized_header(scope='OrgAdmin')

      org_info = {
         'organization_id':100000,
         'title':'哈哈哈哈'
      }

      json_data = json.dumps(org_info)

      rv1 = self.client.post('v1/org/lecture/group',data = json_data,headers = headers)
      self.assertEqual(rv1.status_code,201)

      count = db.session.query(TeacherGroup).count()
      self.assertEqual(count,1)

     # title = db.session.query(TeacherGroup.title).first()
     # self.assertEqual(title,"melodytest")

      org_info = {
         'organization_id':1000010,
         'title':'再插入一条'
      }

      json_data = json.dumps(org_info)

      rv2 = self.client.post('v1/org/lecture/group',data = json_data,headers = headers)
      self.assertEqual(rv2.status_code,201)

      count = db.session.query(TeacherGroup).count()
      self.assertEqual(count,2)


      org_info = [
            {
                'organization_id': 1000010,
                'title': '两条一起插入',
            },
            {
                'organization_id': 10000009,
                'title': '两条一起插入',
            }
        ]

      json_data = json.dumps(org_info)

      rv3 = self.client.post('v1/org/lecture/group', data=json_data, headers=headers)
      self.assertEqual(rv3.status_code, 400)

      lecturer_info = {
                'oid': 2,
                'uid': 530,
                'teacher_group_id': 3
      }


      json_data = json.dumps(lecturer_info)

      rv4 = self.client.post('v1/org/lecture/group/join', data=json_data, headers=headers)
      self.assertEqual(rv4.status_code, 201)










