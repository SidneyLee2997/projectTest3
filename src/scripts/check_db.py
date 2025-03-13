"""
查看数据库内容
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from config import Config
from models import db, Course, Chapter

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app

def check_database(app):
    """查看数据库内容"""
    with app.app_context():
        print("\n=== 课程信息 ===")
        courses = Course.query.all()
        for course in courses:
            print(f"\nID: {course.id}")
            print(f"标题: {course.title}")
            print(f"描述: {course.description}")
            print(f"类别: {course.category}")
            
            print("\n章节列表:")
            chapters = Chapter.query.filter_by(course_id=course.id).order_by(Chapter.order).all()
            for chapter in chapters:
                print(f"\n  章节ID: {chapter.id}")
                print(f"  标题: {chapter.title}")
                print(f"  顺序: {chapter.order}")
                print(f"  内容预览: {chapter.content[:100]}...")

if __name__ == '__main__':
    app = create_app()
    check_database(app) 