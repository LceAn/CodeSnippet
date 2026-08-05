# Python 启动信息模板

`StartMessage.py` 提供彩色状态输出、启动横幅和可选的 GitHub Release 版本检查。

复制后修改 `ScriptConfig` 中的版本、仓库、脚本名称和作者：

```python
class ScriptConfig:
    LOCAL_VERSION = 'v1.0.0'
    REPO_OWNER = 'your-account'
    REPO_NAME = 'your-repository'
    SCRIPT_FUNCTION = '脚本功能'
    SCRIPT_NAME = 'script.py'
    AUTHOR = 'Your Name'
```

保留默认的中文仓库占位符时，模板会跳过网络版本检查，避免每次运行都请求一个无效 GitHub 地址。

```bash
pip install requests colorama
python StartMessage.py
```

版本标签按数字段比较，因此 `v2.10.0` 会正确识别为高于 `v2.9.0`。这个模板只负责启动信息；异常处理、日志和业务退出码仍应由实际脚本补充。
