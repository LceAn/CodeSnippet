# -*- coding: utf-8 -*-
"""
Flask 应用管理脚本

支持命令行参数控制应用启动，包括端口、主机、调试模式、环境等
"""

import argparse
import sys
from app import create_app


def valid_port(value: str) -> int:
    port = int(value)
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError('端口必须在 1 到 65535 之间')
    return port


def parse_arguments() -> argparse.Namespace:
    """
    解析命令行参数
    
    Returns:
        解析后的参数对象
    """
    parser = argparse.ArgumentParser(
        description='Flask 应用管理脚本',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python manager.py                          # 开发环境，默认端口 5000
  python manager.py --debug                  # 启用调试模式
  python manager.py --env production         # 生产环境
  python manager.py --port 8080 --host 0.0.0.0  # 自定义端口和主机
        '''
    )
    
    parser.add_argument(
        '--port',
        type=valid_port,
        default=5000,
        help='运行端口 (默认：5000)'
    )
    
    parser.add_argument(
        '--host',
        type=str,
        default='127.0.0.1',
        help='运行主机地址 (默认：127.0.0.1)'
    )
    
    parser.add_argument(
        '--debug',
        action='store_true',
        help='启用调试模式'
    )
    
    parser.add_argument(
        '--env',
        type=str,
        choices=['development', 'production', 'testing'],
        default='development',
        help='运行环境 (默认：development)'
    )
    
    return parser.parse_args()


def main() -> int:
    """
    主函数
    
    Returns:
        退出码
    """
    args = parse_arguments()
    if args.env == 'production' and args.debug:
        print('生产环境不允许启用 Flask 调试器', file=sys.stderr)
        return 2
    
    # 创建应用
    app = create_app(f'app.config.{args.env.capitalize()}Config')
    
    # 输出启动信息
    print(f"""
╔══════════════════════════════════════════════════════════╗
║  Flask 应用启动                                          ║
╠══════════════════════════════════════════════════════════╣
║  环境：{args.env:<10}                                        ║
║  主机：{args.host:<10}                                        ║
║  端口：{args.port:<10}                                        ║
║  调试：{'是' if args.debug else '否':<10}                                        ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    # 启动应用
    try:
        app.run(
            host=args.host,
            port=args.port,
            debug=args.debug,
            threaded=True
        )
        return 0
    except KeyboardInterrupt:
        print('\n应用已停止')
        return 0
    except Exception as e:
        print(f'\n启动失败：{e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
