# -*- coding: utf-8 -*-
"""
数据模型模块

提供示例数据模型类
"""

from typing import Any


class ExampleModel:
    """
    示例数据模型类
    
    用于演示模型的基本结构和用法
    实际项目中可替换为 SQLAlchemy 模型
    """
    
    def __init__(self, id: int, name: str) -> None:
        """
        初始化模型实例
        
        Args:
            id: 唯一标识符
            name: 名称
        """
        self.id = id
        self.name = name
    
    def __repr__(self) -> str:
        """
        返回对象的字符串表示
        
        Returns:
            格式化的字符串
        """
        return f'<ExampleModel(id={self.id}, name={self.name})>'
    
    def to_dict(self) -> dict:
        """
        转换为字典
        
        Returns:
            包含模型属性的字典
        """
        return {
            'id': self.id,
            'name': self.name
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ExampleModel':
        """
        从字典创建模型实例
        
        Args:
            data: 包含模型属性的字典
            
        Returns:
            模型实例
        """
        return cls(
            id=data.get('id', 0),
            name=data.get('name', '')
        )
