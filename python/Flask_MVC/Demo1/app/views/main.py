# -*- coding: utf-8 -*-
# @Time : {{current_time}}
# @Author : {{author}}
# @File : view_template.py
# @Software : {{IDE}}

from flask import render_template, jsonify

def init_routes(app):
    """初始化路由"""

    @app.route('/')
    def index():
        """主页"""
        return render_template('index.html')

    @app.route('/api/example', methods=['GET'])
    def get_example_data():
        """获取示例数据的 API"""
        example_data = {
            'message': 'Hello, this is example data!',
            'status': 'success'
        }
        return jsonify(example_data)