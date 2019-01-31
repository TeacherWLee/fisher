import base64
import unittest
from advancer.libs.enums import TagType
from advancer.models.news.news_org import NewsOrg
from advancer.models.org.info import Info
from advancer.models.tag import Tag
from advancer.models.user.id_realeation import IdRelation
from advancer.models.user.identity import Identity
from advancer.models.user.user_org import OrgAdmin
from flask_oauthlib.utils import to_unicode, to_bytes
from advancer.models.base import db
from advancer import create_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from advancer.models.org.enroll import Enroll
from advancer.models.org.sign_in import StudentSignIn

__author__ = 'bliss'

SQLALCHEMY_BINDS = {
    # online database
    'online': 'sqlite:///tmp/online.db',

    # app register database
    'heroapi': 'sqlite:///tmp/heroapi.db',

    # organization database
    'org': 'sqlite:///tmp/org.db',

    # consumer database
    'csu': 'sqlite:///tmp/csu.db'
}


def encode_base64(text):
    text = to_bytes(text)
    return to_unicode(base64.b64encode(text))


class TestCase(unittest.TestCase):
    def setUp(self):
        app = create_app({
            'SQLALCHEMY_BINDS': SQLALCHEMY_BINDS,
            'SECRET_KEY': 'secret',
        })
        app.testing = True

        self._ctx = app.app_context()
        self._ctx.push()

        db.init_app(app)

        db.drop_all()
        db.create_all()

        self.app = app
        self.client = app.test_client()
        self.prepare_data()

    def prepare_data(self):
        pass

    def tearDown(self):
        self._ctx.pop()

    def get_authorized_header(self, user_id=1, scope='OrgAdmin', expiration=7200):
        # prepare token
        token = self.generate_auth_token(user_id, 200, scope, expiration)

        return {
            'Authorization': 'basic %s' % encode_base64(str(token, 'utf-8') + ':'),
            'Content-Type': 'application/json',
        }

    def generate_auth_token(self, uid, ac_type, scope, expiration=7200):
        from flask import current_app
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'uid': uid, 'type': int(ac_type), 'scope': scope})


class TestUserCSUCase(TestCase):
    def prepare_data(self):
        prepare_user_data()


class TestOrgCase(TestCase):
    def prepare_data(self):
        prepare_user_data()
        prepare_org_data()


def prepare_user_data():
        from advancer.models.user.user_csu import UserCSU
        from advancer.models.user.user_csu_secure import UserCSUSecure

        users_csu = [
            ('leilei', 5000),
            ('zy', 300),
            ('social', 100)
        ]
        for nickname, score in users_csu:
            user = UserCSU()
            user.nickname = nickname
            user.score = score
            db.session.add(user)
        db.session.commit()

        users_secure =[
            ('1', 'aswind', 17777777777, '123123'),
            ('2', 'bliss', 18888888888, '111222333'),
            ('3', 'openid', '', '123456')
        ]

        for uid, username, mobile, password in users_secure:
            user = UserCSUSecure()
            user.id = uid
            user.username = username
            user.password = password
            user.mobile = mobile
            db.session.add(user)
        db.session.commit()

        identities = [
            ('设计师', '普通设计师学员'),
            ('教师', '机构老师')
        ]

        for title, description in identities:
            iden = Identity()
            iden.title = title
            iden.description = description
            db.session.add(iden)
        db.session.commit()

        identities_realation = [
            (1, 1), (2, 2)
        ]
        for uid, iden in identities_realation:
            iden_r = IdRelation()
            iden_r.uid = uid
            iden_r.group_id = iden
            db.session.add(iden_r)
        db.session.commit()


def prepare_org_data():
    users_org = [
        ('18607131949', '123123', 1),
        ('18607138888', '111222333', 2)
    ]
    for mobile, password, organization_id in users_org:
        user = OrgAdmin()
        user.mobile = mobile
        user.password = password
        user.organization_id = organization_id
        db.session.add(user)
    db.session.commit()

    news = [
        ('头条', '开业酬宾', '头条内容'),
        ('头条', '开业酬宾', '头条内容'),
        ('头条', '开业酬宾', '头条内容'),
        ('头条', '开业酬宾', '头条内容'),
        ('头条', '开业酬宾', '头条内容')
    ]
    for tag, title, content in news:
        news = NewsOrg()
        news.tag = tag
        news.title = title
        news.content = content
        db.session.add(news)
    db.session.commit()

    tags = [
        (TagType.org_advantage, '世界500强CEO授课'),
        (TagType.org_advantage, '无敌的培训学校'),
        (TagType.org_type, '设计培训'),
        (TagType.org_type, '互联网精英培训')
    ]

    for tag_type, value in tags:
        tag = Tag()
        tag.type = tag_type.value
        tag.value = value
        db.session.add(tag)
    db.session.commit()

    orgs = [
        ('北大青鸟', '培训！培训！培训万岁', '武汉市洪山区光谷新世界1602', '武汉',
         '114.421816', '30.498029', '设计培训#精英培训', 1, '0278888888', '无敌#高效', 1,
         '介绍', 'video', 'video_img', 'logo'),
        ('火星时代', '培训！培训！培训万岁', '武汉市洪山区光谷新世界1602', '北京',
         '114.421816', '30.498029', '设计培训#精英培训', 1, '0278888888', '无敌#高效', 2,
         '介绍', 'video', 'video_img', 'logo')
    ]

    for org_info in orgs:
        org = Info()
        org.name = org_info[0]
        org.slogan = org_info[1]
        org.location = org_info[2]
        org.city = org_info[3]
        org.lon = org_info[4]
        org.lat = org_info[5]
        org.type = org_info[6]
        org.audit_status = org_info[7]
        org.phone_num = org_info[8]
        org.advantage = org_info[9]
        org.uid = org_info[10]
        org.introduce = org_info[11]
        org.video = org_info[12]
        org.video_img = org_info[13]
        org.logo = org_info[14]
        db.session.add(org)
    db.session.commit()

    enrolls = [
        ('1', '5', '张三', '18765862122', '南望山男子技术学院', '3', '2'),
        ('1', '7', '嘿嘿', '18765862122', '挖掘机技术学院', '3', '2'),
        ('1', '23', 'ss', '18765862122', '哈尔滨佛学院', '3', '2'),
        ('1', '44', 'ss', '18765862122', '港沟镇建筑施工学院', '3', '1'),
        ('1', '55', 'ww', '18765862122', '南望山男子技术学院', '3', '1'),
        ('1', '66', 'rr', '18765862122', '南望山男子技术学院', '3', '-2'),
    ]

    for enroll_info in enrolls:
        enroll = Enroll()
        enroll.organization_id = enroll_info[0]
        enroll.student_uid = enroll_info[1]
        enroll.student_name = enroll_info[2]
        enroll.phone_num = enroll_info[3]
        enroll.student_university = enroll_info[4]
        enroll.course_id = enroll_info[5]
        enroll.status = enroll_info[6]
        db.session.add(enroll)
    db.session.commit()

    sign = [
        ('1', '1', '2015-12-01'),
        ('1', '1', '2015-12-03'),
        ('1', '1', '2015-12-05'),
        ('1', '1', '2015-12-07'),
        ('1', '1', '2015-12-09'),
    ]

    for signin in sign:
        ssign = StudentSignIn()
        ssign.uid = signin[0]
        ssign.organization_id = signin[1]
        ssign.date = signin[2]
        db.session.add(ssign)
    db.session.commit()




