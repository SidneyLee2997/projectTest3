"""
配置文件
"""
import os

class Config:
    """基础配置类"""
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'sqlite:///math_learning.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 安全配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    
    # 应用配置
    DEBUG = True 