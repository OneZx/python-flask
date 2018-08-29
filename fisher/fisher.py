# Create Time : 2018/8/29 22:31 
# Author : doyou

from flask import Flask

__author__ = 'doyou'

app = Flask(__name__)  # 实例化Flask对象


@app.route('/hello')   # hello后面加斜杠 ,让用户不输斜杠 或输入都可以访问到
def hello():           # 视图函数 类比 Controller
    # 基于类的视图(即插视图)
    return 'Hello, doyou'

def world():
    return 'world hahahaha'

# app.add_url_rule('/world',view_func=world) 另一种注册路由的方式 大多数使用上一种,
# 但是使用基于类的视图时 使用add_url_rule方式

app.run(host='0.0.0.0', debug=True,port= '81') # 打开调试模式,可热重启 但是只能127端口访问,可指定ip地址
# 0.0.0.0 表示可以接收外网的访问  # port 也可以设置