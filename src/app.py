"""
主应用文件
"""
import logging
from flask import Flask, render_template
from config import Config
from models import db
from routes.course import course_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    
    # 配置日志
    logging.basicConfig(level=logging.INFO)
    app.logger.setLevel(logging.INFO)
    
    # 加载配置
    app.config.from_object(config_class)

    # 初始化数据库
    db.init_app(app)

    # 注册蓝图
    app.register_blueprint(course_bp, url_prefix='/course')

    # 创建数据库表
    with app.app_context():
        try:
            db.create_all()
            app.logger.info('数据库表已创建')
        except Exception as e:
            app.logger.error(f'创建数据库表时出错: {str(e)}')

    # 首页路由
    @app.route('/')
    def index():
        app.logger.info('访问网站首页')
        return render_template('index.html')

    # 注册错误处理
    @app.errorhandler(404)
    def page_not_found(e):
        app.logger.error(f'页面未找到: {str(e)}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        app.logger.error(f'服务器内部错误: {str(e)}')
        return render_template('errors/500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 