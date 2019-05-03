Flasky
======

This repository contains the source code examples for the second edition of my O'Reilly book [Flask Web Development](http://www.flaskbook.com).

The commits and tags in this repository were carefully created to match the sequence in which concepts are presented in the book. Please read the section titled "How to Work with the Example Code" in the book's preface for instructions.

For Readers of the First Edition of the Book
--------------------------------------------

The code examples for the first edition of the book were moved to a different repository: [https://github.com/miguelgrinberg/flasky-first-edition](https://github.com/miguelgrinberg/flasky-first-edition).

---
# 更新
## 首次启动流程
- virtualenv venv #安装venv
- source venv/bin/activate #进入venv环境
- pip install -r requirements.txt #安装依赖包
- export FLASK_APP=flasky.py #设置flask环境变量（也可通过dotenv的.env文件设置）
- export FLASK_DEBUG=1 #设置flask环境变量（也可通过dotenv的.env文件设置）
- flask deploy #DB升级+系统初始化数据
- flask profile #启动server


# 变动记录
1. 增加log相关调试(自定义日志Formatter，TimedRotatingFileHandler)
2. 增加全局异常捕捉调试(@app.app_errorhandler(err_code_or_exception)全局异常捕捉)
3. 测试路由的两种定义方式(@app.route()、app.add_url_rule())

根据表反向生成
sudo sqlacodegen  sqlite:///path > modle.py
