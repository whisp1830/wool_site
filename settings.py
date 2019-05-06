# encoding:utf-8
"""
程序配置文件
"""
import os.path

HOST = '0.0.0.0'
PORT = 8000
SETTINGS = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),  # 模板路径
    static_path=os.path.join(os.path.dirname(__file__), "static"),  # 静态文件路径
)
