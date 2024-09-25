# -*- coding: utf-8 -*-
# @Time : {{current_time}}
# @Author : {{author}}
# @File : manager.py
# @Software : {{IDE}}

import argparse
from flask import Flask
from app import create_app

# 创建解析器对象
parser = argparse.ArgumentParser(description="Flask 管理脚本")

# 添加参数
parser.add_argument(
    "--port",
    type=int,
    default=5000,
    help="指定运行的端口号 (默认: 5000)"
)

parser.add_argument(
    "--host",
    type=str,
    default="127.0.0.1",
    help="指定运行的主机地址 (默认: 127.0.0.1)"
)

parser.add_argument(
    "--debug",
    action="store_true",
    help="启用调试模式 (默认: 关闭)"
)

parser.add_argument(
    "--env",
    type=str,
    choices=["development", "production"],
    default="development",
    help="选择运行环境 (默认: development)"
)

# 解析命令行参数
args = parser.parse_args()

# 创建 Flask 应用实例
app = create_app()

# 根据选择的环境应用不同的配置
if args.env == "production":
    app.config.from_object("app.config.ProductionConfig")
else:
    app.config.from_object("app.config.DevelopmentConfig")

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(host=args.host, port=args.port, debug=args.debug)