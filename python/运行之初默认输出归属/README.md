## StartMessage.py 说明文档

### 概述
`StartMessage.py` 是一个用于展示脚本启动信息的模板文件，包括版本检查、作者信息和功能描述。该脚本模板设计用于便捷地展示启动信息，并通过 GitHub API 自动检查是否有新版本可用。此模板旨在为开发者提供一个易于使用的基础框架，便于在每个 Python 项目中统一显示和管理脚本信息。

### 功能概述
- **脚本标题信息展示**：包括功能描述、作者信息、版本信息等，便于识别脚本用途。
- **颜色输出**：通过 `colorama` 库实现跨平台的彩色输出，增强可读性。
- **版本检查**：通过 GitHub API 获取最新版本信息，与本地版本进行对比，并提示是否需要更新。

### 代码结构

#### 1. 导入库
```python
import requests
from colorama import Fore, Style, init
```
- `requests`：用于通过 GitHub API 获取最新版本信息。
- `colorama`：提供跨平台的终端颜色支持。

#### 2. 初始化 colorama
```python
init(autoreset=True)
```
在 Windows 系统上，`init()` 用于初始化 `colorama`，使得终端支持 ANSI 转义字符，`autoreset=True` 保证每次输出后自动重置颜色。

#### 3. Config 类
`Config` 类用于存储配置和管理脚本信息的显示逻辑。

**类属性：**
- `yellow`, `white`, `green`, `blue`, `red`, `end`：定义了不同颜色的终端输出。
- `local_version`：本地版本号，用于与 GitHub 最新版本号进行对比。
- `version_info`：显示版本信息的格式化字符串。
- `repo_api_url`：GitHub API 的请求地址，用于获取最新版本信息。

**类方法：**

1. **`generate_titles(script_function, script_name, author)`**:
    - 生成脚本启动时的标题信息，包括功能描述、脚本名称和作者信息。
    - 使用 ASCII 艺术字符展示标题框架。

2. **`print_status(message, status_type='info')`**:
    - 打印带有颜色和状态符号的消息信息。根据 `status_type` 参数控制不同的信息类型和颜色。
    - `status_type` 可以为：
        - `'info'`：正常信息，前缀 `[ + ]`，绿色。
        - `'warning'`：警告信息，前缀 `[ ! ]`，黄色。
        - `'error'`：错误信息，前缀 `[ - ]`，红色。

3. **`get_latest_version()`**:
    - 从 GitHub 仓库的 Releases 中获取最新版本号。
    - 如果请求成功，返回最新版本号；如果失败，打印警告信息。

4. **`check_for_updates()`**:
    - 获取最新版本号，并与本地版本号进行对比。
    - 如果本地版本号低于最新版本号，提示有新版本可用；否则提示当前已是最新版本。

#### 4. 主函数 `main()`
```python
def main():
    """主函数：替换此处为具体的业务逻辑"""
    Config.print_status("脚本运行中，请稍候...", 'info')
    Config.check_for_updates()
    Config.print_status("脚本运行结束。", 'info')
```
- 在主函数中：
    - 首先显示脚本开始运行的状态信息。
    - 调用 `check_for_updates()` 检查是否有新版本。
    - 最后显示脚本运行结束的状态信息。

#### 5. 主程序入口
```python
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
```
- 设置 `script_function`、`script_name` 和 `author` 的占位符信息。
- 调用 `Config.generate_titles()` 生成并打印脚本启动信息。
- 调用 `main()` 运行主逻辑。
- 捕获异常并打印错误信息。

### ASCII 艺术生成
该脚本的 ASCII 艺术图形部分由 [https://tools.kalvinbg.cn/txt/ascii](https://tools.kalvinbg.cn/txt/ascii) 生成。你可以在该网站上输入自定义文字，并选择合适的字体风格生成对应的 ASCII 艺术图形。

### 使用说明
1. **修改版本号、功能说明等占位符信息**：
   - 打开 `StartMessage.py`，在 `if __name__ == "__main__"` 部分修改 `script_function`、`script_name` 和 `author` 变量为实际内容。

2. **配置 GitHub API 地址**：
   - 替换 `repo_api_url` 中的 `你的用户名` 和 `你的仓库名` 为实际的 GitHub 用户名和仓库名。

3. **运行脚本**：
   - 运行脚本时，终端会显示带颜色的启动信息，并检查是否有新版本可用。

### 注意事项
- 确保安装了 `requests` 和 `colorama` 库：
    ```bash
    pip install requests colorama
    ```
- 如果要在 Windows 系统中使用颜色显示，确保 `colorama` 库被正确初始化。
