# -*- coding: utf-8 -*-
"""
主视图模块

提供主页路由和示例 API 接口
"""

from typing import Any, Tuple
from flask import Blueprint, render_template, jsonify

# 创建蓝图
main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index() -> str:
    """
    主页路由
    
    Returns:
        渲染的 HTML 模板
    """
    return render_template('index.html')


@main_bp.route('/api/example')
def get_example_data() -> Tuple[Any, int]:
    """
    示例 API 接口
    
    Returns:
        JSON 响应和状态码
    """
    data = {
        'status': 'success',
        'message': '这是一个示例 API 响应',
        'data': {
            'id': 1,
            'name': 'Example',
            'items': ['item1', 'item2', 'item3']
        }
    }
    return jsonify(data), 200


@main_bp.route('/api/health')
def health_check() -> Tuple[Any, int]:
    """
    健康检查接口
    
    Returns:
        健康状态 JSON 响应
    """
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    }), 200


def init_routes(app: Any) -> None:
    """
    注册路由蓝图
    
    Args:
        app: Flask 应用实例
    """
    app.register_blueprint(main_bp)
