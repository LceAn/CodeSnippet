"""
视图模块初始化

导入所有视图蓝图并注册路由
"""

from typing import Any
from app.views.main import main_bp


def init_routes(app: Any) -> None:
    """
    注册所有路由蓝图
    
    Args:
        app: Flask 应用实例
    """
    app.register_blueprint(main_bp)
