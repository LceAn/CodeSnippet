# Flask MVC 示例

`Demo1` 展示一个小型 Flask 应用的目录边界：应用工厂负责配置、日志和错误处理，蓝图负责页面与 JSON API，模型目录提供不依赖数据库的转换示例。

## 运行

从仓库根目录安装依赖，再进入示例目录：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd python/Flask_MVC/Demo1
python manager.py
```

接口：

| 路径 | 说明 |
| --- | --- |
| `/` | HTML 示例页 |
| `/api/example` | 示例 JSON |
| `/api/health` | 健康检查 |

## 环境

- `development`：默认 SQLite 连接字符串，允许本地开发。
- `testing`：开启 Flask 测试模式，不写日志文件。
- `production`：必须提供 `SECRET_KEY` 和 `DATABASE_URL`，缺失时拒绝启动。

```bash
SECRET_KEY='replace-me' \
DATABASE_URL='postgresql://user:password@host/database' \
python manager.py --env production
```

当前示例没有注册 SQLAlchemy 或其他 ORM，`DATABASE_URL` 只作为扩展点保存在配置中。生产部署还应使用 Gunicorn、uWSGI 等 WSGI 服务器，不要直接使用 Flask 开发服务器。

## 扩展位置

- `app/__init__.py`：在 `_register_extensions` 中初始化扩展。
- `app/config.py`：增加环境配置和失败策略。
- `app/models/`：替换示例模型。
- `app/views/`：增加蓝图和路由。

根目录测试会创建 testing 应用并验证主要接口，不需要数据库和网络。
