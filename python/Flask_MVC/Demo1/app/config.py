# -*- coding: utf-8 -*-
"""
Flask 应用配置模块

提供通用配置、开发环境配置、生产环境配置
支持从环境变量加载敏感信息
"""

import os
from typing import Any, Dict


class Config:
    """通用配置基类"""
    
    # 安全密钥（生产环境应从环境变量加载）
    SECRET_KEY: str = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # SQLAlchemy 配置
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    
    # 日志配置
    LOG_DIR: str = os.environ.get('LOG_DIR', 'logs')
    
    # 应用配置
    ENV: str = 'default'
    DEBUG: bool = False
    TESTING: bool = False
    
    # 额外配置项
    MAX_CONTENT_LENGTH: int = 16 * 1024 * 1024  # 最大上传 16MB
    
    @classmethod
    def init_app(cls, app: Any) -> None:
        """应用特定的初始化"""
        pass


class DevelopmentConfig(Config):
    """开发环境配置"""
    
    ENV = 'development'
    DEBUG = True
    
    # 开发环境使用 SQLite
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        'DEV_DATABASE_URL',
        'sqlite:///development.db'
    )
    
    # 开发环境日志级别
    LOG_LEVEL: int = 10  # DEBUG
    
    @classmethod
    def init_app(cls, app: Any) -> None:
        Config.init_app(app)
        app.logger.info('当前为开发环境')


class ProductionConfig(Config):
    """生产环境配置"""
    
    ENV = 'production'
    DEBUG = False
    
    # 生产环境使用 MySQL/PostgreSQL
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://user:password@localhost/production_db'
    )
    
    # 生产环境日志级别
    LOG_LEVEL: int = 20  # INFO
    
    # 生产环境安全配置
    SESSION_COOKIE_SECURE: bool = True
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = 'Lax'
    
    @classmethod
    def init_app(cls, app: Any) -> None:
        Config.init_app(app)
        app.logger.info('当前为生产环境')


class TestingConfig(Config):
    """测试环境配置"""
    
    ENV = 'testing'
    TESTING = True
    
    # 测试环境使用内存数据库
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///:memory:'
    
    # 禁用 CSRF 保护便于测试
    WTF_CSRF_ENABLED: bool = False
    
    @classmethod
    def init_app(cls, app: Any) -> None:
        Config.init_app(app)
        app.logger.info('当前为测试环境')


# 配置字典，用于环境切换
config: Dict[str, type] = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
