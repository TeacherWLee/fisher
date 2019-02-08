#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'Wei Li (liw@sicnu.edu.cn)'
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# ---------------- Flask App 创建与配置 ---------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:wlee0721@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# ---------------- SQLAlchemy 创建并配置 ----------------
db = SQLAlchemy(app=app)
db.init_app(app=app)


# ---------------- 模型创建 ----------------
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    author_detail_id = db.Column(db.Integer, db.ForeignKey('author_detail.id'))
    author_detail = db.relationship('AuthorDetail', backref='author', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


class AuthorDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    qq = db.Column(db.String(50))


article_tag = db.Table('art_tag',
                       db.Column('art_id', db.Integer, db.ForeignKey('article.id')),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                       )


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    author = db.relationship('Author', backref='article')
    tags = db.relationship('Tag', backref='article', secondary=article_tag)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_title = db.Column(db.String(20), nullable=False)


# ---------------- 删除所有数据表，清理数据 ----------------
db.drop_all()


# ---------------- 创建所有模型的数据表 ----------------
db.create_all()


# ---------------- 插入记录 ----------------
def insert_record():
    author1 = Author(name='author1')
    author2 = Author(name='author2')
    author3 = Author(name='author3')
    author_detail1 = AuthorDetail(email='author1@example.com', qq='10001')
    author_detail2 = AuthorDetail(email='author2@example.com', qq='10002')
    author_detail3 = AuthorDetail(email='author3@example.com', qq='10003')
    article1 = Article(title='title1')
    article2 = Article(title='title2')
    article_delete = Article(title='title_delete')
    tag1 = Tag(tag_title='tag1')
    tag2 = Tag(tag_title='tag2')
    tag_useless = Tag(tag_title='tag_useless')
    tag_delete1 = Tag(tag_title='tag_delete1')
    tag_delete2 = Tag(tag_title='tag_delete2')

    article1.tags = [tag1, tag2]
    article2.tags = [tag1]
    article_delete.tags = [tag_delete1, tag_delete2]

    db.session.add(author1)
    db.session.add(author2)
    db.session.add(author3)
    db.session.add(author_detail1)
    db.session.add(author_detail2)
    db.session.add(author_detail3)
    db.session.add(article1)
    db.session.add(article2)
    db.session.add(article_delete)
    db.session.add(tag1)
    db.session.add(tag2)
    db.session.add(tag_useless)
    db.session.add(tag_delete1)
    db.session.add(tag_delete2)

    db.session.commit()


insert_record()


# ---------------- 更新记录 ----------------
authors = Author.query.order_by(Author.id).all()
authors_details = AuthorDetail.query.order_by(AuthorDetail.id).all()
for i in range(0, len(authors)):
    authors[i].author_detail_id = authors_details[i].id
    db.session.add(authors[i])
db.session.commit()


# ---------------- 查询记录 ----------------
# 通过指定字段查询
query_author1 = Author.query.filter_by(name='author1').first()
print(query_author1)
query_miss = Author.query.filter_by(name='miss').first()
print(query_miss)

# 通过主键查询
query_author1 = Author.query.get(1)
print(query_author1)

# 按某种规则对用户排序:
query_author_by_order = Author.query.order_by(Author.name).all()
print(query_author_by_order)

# 正向查询
author1_obj = Author.query.filter_by(name='author1').first()
print(author1_obj.author_detail.email)
article1_obj = Article.query.get(1)
print(article1_obj.tags)

# 反向查询
author_detail1_obj = AuthorDetail.query.filter_by(email='author1@example.com').first()
print(author_detail1_obj.author[0].name)


# ---------------- 删除记录 ----------------
query_tag_useless = Tag.query.filter_by(tag_title='tag_useless').first()
db.session.delete(query_tag_useless)
db.session.commit()

query_article_delete = Article.query.filter_by(title='title_delete').first()
query_tag_delete = Tag.query.filter_by(tag_title='tag_delete1').first()
print(query_article_delete.tags)
query_article_delete.tags.remove(query_tag_delete)
print(query_article_delete.tags)
db.session.commit
query_article_delete = Article.query.filter_by(title='title_delete').first()
print(query_article_delete.tags)


db.session.delete(query_article_delete)
db.session.commit()
