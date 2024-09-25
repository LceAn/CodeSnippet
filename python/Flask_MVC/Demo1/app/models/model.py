# -*- coding: utf-8 -*-
# @Time : {{current_time}}
# @Author : {{author}}
# @File : model_template.py
# @Software : {{IDE}}

from flask_sqlalchemy import SQLAlchemy

# 初始化数据库对象
db = SQLAlchemy()

class ExampleModel(db.Model):
    """示例数据模型"""
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<ExampleModel {self.name}>'