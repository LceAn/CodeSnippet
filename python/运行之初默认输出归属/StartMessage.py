# -*-  coding : utf-8 -*-
# @Time : 2024/9/23 下午4:52
# @Autor : LceAn
# @File : StartMessage.py
# @Software : PyCharm

import requests
from colorama import Fore, Style, init

# 初始化 colorama（只在 Windows 上需要）
init(autoreset=True)


class Config:
    # 颜色和版本信息（使用 colorama 提供的颜色定义）
    yellow = Fore.YELLOW
    white = Fore.WHITE
    green = Fore.GREEN
    blue = Fore.BLUE
    red = Fore.RED
    end = Style.RESET_ALL

    # 本地版本信息
    local_version = 'v0.0.2'
    version_info = f"{white}{{{red}{local_version} #dev{white}}}"
    repo_api_url = "https://api.github.com/repos/你的用户名/你的仓库名/releases/latest"

    @staticmethod
    def generate_titles(script_function, script_name, author):
        """生成标题信息"""
        return f"""
        功能：{script_function}
{Config.yellow}
 ____             _ __        ___ _   _         ___ ____      
|  _ \  ___  __ _| |\ \      / (_) |_| |__     |_ _|  _ \ ___ 
| | | |/ _ \/ _` | | \ \ /\ / /| | __| '_ \     | || |_) / __|{Config.green}
| |_| |  __/ (_| | |  \ V  V / | | |_| | | |    | ||  __/\__ \\
|____/ \___|\__,_|_|___\_/\_/  |_|\__|_| |_|___|___|_|   |___/{Config.white}
                  |_____|                 |_____|     By {Config.version_info}
    作者：{author}
    脚本名称：{script_name}
    内部版本，请勿泄漏
    {Config.red}本脚本正在开发中，请在每次使用前更新！{Config.end}
    """

    @staticmethod
    def print_status(message, status_type='info'):
        """打印带颜色和状态的消息信息"""
        if status_type == 'info':
            prefix = '[ + ]'
            color = Config.green
        elif status_type == 'warning':
            prefix = '[ ! ]'
            color = Config.yellow
        elif status_type == 'error':
            prefix = '[ - ]'
            color = Config.red
        else:
            prefix = '[ * ]'
            color = Config.white

        print(f"{color}{prefix} {message}{Config.end}")

    @staticmethod
    def get_latest_version():
        """从GitHub获取最新版本号"""
        try:
            response = requests.get(Config.repo_api_url)
            if response.status_code == 200:
                latest_version = response.json()["tag_name"]
                return latest_version
            else:
                Config.print_status("无法从GitHub获取版本信息", "warning")
                return None
        except requests.exceptions.RequestException as e:
            Config.print_status(f"请求失败: {e}", "error")
            return None

    @staticmethod
    def check_for_updates():
        """检查是否有新版本"""
        latest_version = Config.get_latest_version()
        if latest_version:
            if Config.local_version < latest_version:
                Config.print_status(f"有新版本可用: {latest_version}，请及时更新！", "warning")
            else:
                Config.print_status("当前版本已是最新版本。", "info")


def main():
    """主函数：替换此处为具体的业务逻辑"""
    # 示例打印状态信息
    Config.print_status("脚本运行中，请稍候...", 'info')
    # 检查更新
    Config.check_for_updates()
    # 业务逻辑结束
    Config.print_status("脚本运行结束。", 'info')


if __name__ == "__main__":
    try:
        # 初始化占位符内容
        script_function = "--修改此处进行设定功能说明--"
        script_name = "--修改此处为脚本名称--"
        author = "--修改此处为作者名称--"

        # 打印脚本标题信息，传递三个参数
        print(Config.generate_titles(script_function, script_name, author))

        # 运行主函数
        main()
    except Exception as e:
        Config.print_status(f"发生严重错误，程序终止: {e}", 'error')
        # 可以选择在此记录日志
        # log_entries.append(f"发生严重错误，程序终止: {e}")