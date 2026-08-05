# -*- coding: utf-8 -*-
"""
Flask 应用工厂模块

提供应用实例创建、配置加载、日志初始化、错误处理等功能
"""

from typing import Any
from flask import Flask, jsonify, Response
from app.views import init_routes
import logging
from logging.handlers import RotatingFileHandler
import os
from werkzeug.utils import import_string


def create_app(config_object: str = 'app.config.Config') -> Flask:
    """
    创建并配置 Flask 应用实例
    
    Args:
        config_object: 配置对象路径，默认使用 app.config.Config
        
    Returns:
        配置好的 Flask 应用实例
    """
    app = Flask(__name__)
    config_class = import_string(config_object) if isinstance(config_object, str) else config_object
    app.config.from_object(config_class)
    config_class.init_app(app)
    
    # 初始化日志
    _init_logging(app)
    
    # 注册扩展
    _register_extensions(app)
    
    # 全局错误处理
    _register_error_handlers(app)
    
    # 初始化路由
    init_routes(app)
    
    app.logger.info(f"Flask 应用已启动，环境：{app.config.get('ENV', 'development')}")
    
    return app


def _init_logging(app: Flask) -> None:
    """
    初始化日志配置
    
    Args:
        app: Flask 应用实例
    """
    app.logger.handlers.clear()

    # 创建日志目录
    log_dir = app.config.get('LOG_DIR', 'logs')
    file_handler = None
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        file_handler = RotatingFileHandler(
            os.path.join(log_dir, 'app.log'),
            maxBytes=10 * 1024 * 1024,
            backupCount=10,
            encoding='utf-8',
        )
        file_handler.setLevel(app.config.get('LOG_LEVEL', logging.INFO))
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if app.debug else logging.INFO)
    
    # 格式化器
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    if file_handler:
        file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # 添加处理器
    if file_handler:
        app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(app.config.get('LOG_LEVEL', logging.INFO))


def _register_extensions(app: Flask) -> None:
    """
    注册 Flask 扩展
    
    Args:
        app: Flask 应用实例
    """
    # 此处可添加 SQLAlchemy、LoginManager 等扩展初始化
    # 例如：
    # from flask_sqlalchemy import SQLAlchemy
    # db.init_app(app)
    pass


def _register_error_handlers(app: Flask) -> None:
    """
    注册全局错误处理器
    
    Args:
        app: Flask 应用实例
    """
    
    @app.errorhandler(400)
    def bad_request(error: Any) -> tuple[Response, int]:
        app.logger.warning(f"Bad Request: {error}")
        return jsonify({'error': 'Bad Request', 'message': str(error)}), 400
    
    @app.errorhandler(404)
    def not_found(error: Any) -> tuple[Response, int]:
        app.logger.warning(f"Resource not found: {error}")
        return jsonify({'error': 'Not Found', 'message': 'Resource not found'}), 404
    
    @app.errorhandler(405)
    def method_not_allowed(error: Any) -> tuple[Response, int]:
        app.logger.warning(f"Method not allowed: {error}")
        return jsonify({'error': 'Method Not Allowed', 'message': str(error)}), 405
    
    @app.errorhandler(500)
    def internal_error(error: Any) -> tuple[Response, int]:
        app.logger.error(f"Server Error: {error}", exc_info=True)
        return jsonify({'error': 'Server Error', 'message': 'Internal server error'}), 500
