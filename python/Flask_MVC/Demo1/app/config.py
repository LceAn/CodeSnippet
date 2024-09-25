# -*- coding: utf-8 -*-
# @Time : {{current_time}}
# @Author : {{author}}
# @File : config.py
# @Software : {{IDE}}

class Config:
    """通用配置"""
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'  # 使用 SQLite 数据库

class ProductionConfig(Config):
    """生产环境配置"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/production_db'  # 使用 MySQL 数据库

# 配置字典，用于环境切换
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}