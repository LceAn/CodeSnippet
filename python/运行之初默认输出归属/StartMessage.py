# -*- coding: utf-8 -*-
"""
脚本启动信息模板

提供统一的脚本启动界面、版本检查、彩色输出等功能
可作为所有 Python 脚本的启动模板
"""

import sys
import re
import requests
from typing import Optional
from colorama import Fore, Style, init

# 初始化 colorama（跨平台颜色支持）
init(autoreset=True)


class Colors:
    """颜色工具类"""
    
    YELLOW = Fore.YELLOW
    WHITE = Fore.WHITE
    GREEN = Fore.GREEN
    BLUE = Fore.BLUE
    RED = Fore.RED
    CYAN = Fore.CYAN
    MAGENTA = Fore.MAGENTA
    RESET = Style.RESET_ALL
    
    @staticmethod
    def info(text: str) -> str:
        return f"{Fore.GREEN}[ + ] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def warning(text: str) -> str:
        return f"{Fore.YELLOW}[ ! ] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def error(text: str) -> str:
        return f"{Fore.RED}[ - ] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def success(text: str) -> str:
        return f"{Fore.GREEN}[ ✔ ] {text}{Style.RESET_ALL}"
    
    @staticmethod
    def info_msg(text: str) -> str:
        return f"{Fore.CYAN}[ ℹ ] {text}{Style.RESET_ALL}"


class ScriptConfig:
    """脚本配置类"""
    
    # 版本信息
    LOCAL_VERSION: str = 'v0.0.2'
    REPO_OWNER: str = '你的用户名'
    REPO_NAME: str = '你的仓库名'
    REPO_API_URL: str = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'
    
    # 脚本元数据
    SCRIPT_FUNCTION: str = '--修改此处进行设定功能说明--'
    SCRIPT_NAME: str = '--修改此处为脚本名称--'
    AUTHOR: str = '--修改此处为作者名称--'
    
    @staticmethod
    def generate_banner(function: str, name: str, author: str, version: str) -> str:
        """
        生成脚本启动横幅
        
        Args:
            function: 功能描述
            name: 脚本名称
            author: 作者
            version: 版本号
            
        Returns:
            格式化的横幅字符串
        """
        return f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════╗
║  {function:<50} ║
╠══════════════════════════════════════════════════════════╣
║  脚本：{name:<44} ║
║  作者：{author:<44} ║
║  版本：{Colors.RED}{version}{Colors.WHITE}{Colors.RESET}{Colors.WHITE:<40} ║
╚══════════════════════════════════════════════════════════╝
{Colors.RESET}"""
    
    @staticmethod
    def get_latest_version(timeout: int = 5) -> Optional[str]:
        """
        从 GitHub 获取最新版本号
        
        Args:
            timeout: 请求超时时间（秒）
            
        Returns:
            最新版本号，失败返回 None
        """
        if ScriptConfig.REPO_OWNER.startswith('你的') or ScriptConfig.REPO_NAME.startswith('你的'):
            return None

        try:
            response = requests.get(ScriptConfig.REPO_API_URL, timeout=timeout)
            if response.status_code == 200:
                return response.json().get('tag_name')
            else:
                print(Colors.warning(f"获取版本信息失败：HTTP {response.status_code}"))
                return None
        except requests.exceptions.RequestException as e:
            print(Colors.warning(f"网络请求失败：{e}"))
            return None
    
    @staticmethod
    def check_for_updates() -> bool:
        """
        检查是否有新版本
        
        Returns:
            是否有新版本
        """
        latest_version = ScriptConfig.get_latest_version()
        if latest_version:
            current = tuple(int(part) for part in re.findall(r'\d+', ScriptConfig.LOCAL_VERSION))
            latest = tuple(int(part) for part in re.findall(r'\d+', latest_version))
            if latest > current:
                print(Colors.warning(f"发现新版本：{latest_version}，当前版本：{ScriptConfig.LOCAL_VERSION}"))
                print(Colors.info_msg("请及时更新！"))
                return True
            else:
                print(Colors.success(f"当前已是最新版本 ({ScriptConfig.LOCAL_VERSION})"))
                return False
        return False


def print_banner() -> None:
    """打印启动横幅"""
    banner = ScriptConfig.generate_banner(
        ScriptConfig.SCRIPT_FUNCTION,
        ScriptConfig.SCRIPT_NAME,
        ScriptConfig.AUTHOR,
        ScriptConfig.LOCAL_VERSION
    )
    print(banner)


def main() -> int:
    """
    主函数 - 业务逻辑入口
    
    Returns:
        退出码
    """
    # 示例业务逻辑
    print(Colors.info_msg("脚本运行中，请稍候..."))
    
    # 检查更新
    ScriptConfig.check_for_updates()
    
    # 此处替换为实际业务逻辑
    # ...
    
    print(Colors.success("脚本运行结束"))
    return 0


if __name__ == '__main__':
    try:
        # 打印启动横幅
        print_banner()
        
        # 运行主函数
        sys.exit(main())
        
    except KeyboardInterrupt:
        print(f"\n{Colors.warning('用户中断操作')}")
        sys.exit(0)
    except Exception as e:
        print(Colors.error(f"发生严重错误：{e}"))
        sys.exit(1)
