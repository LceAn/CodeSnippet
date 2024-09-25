# -*- coding: utf-8 -*-
# @Time : {{current_time}}
# @Author : {{author}}
# @File : __init__.py
# @Software : {{IDE}}

from flask import Flask, jsonify
from app.views import init_routes
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')  # 使用配置文件中的配置

    # 初始化日志
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    app.logger = logger

    # 全局错误处理
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f'Server Error: {error}')
        return jsonify({'error': 'Server Error'}), 500

    init_routes(app)    # 初始化路由
    return app