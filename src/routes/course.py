"""
课程相关路由
"""
from flask import Blueprint, render_template, current_app
from models import Course, Chapter

course_bp = Blueprint('course', __name__)

@course_bp.route('/list/<category>')
def list_courses(category):
    """课程列表页面"""
    current_app.logger.info(f'正在获取 {category} 类别的课程')
    courses = Course.query.filter_by(category=category).all()
    current_app.logger.info(f'找到 {len(courses)} 个课程')
    return render_template('course/list.html', courses=courses, category=category)

@course_bp.route('/linear-algebra')
def linear_algebra():
    """线性代数课程页面"""
    current_app.logger.info('正在获取线性代数课程')
    course = Course.query.filter_by(category='linear-algebra').first()
    if not course:
        current_app.logger.error('未找到线性代数课程')
        return render_template('errors/404.html'), 404
    
    current_app.logger.info(f'找到课程：{course.title}')
    chapters = Chapter.query.filter_by(course_id=course.id).order_by(Chapter.order).all()
    current_app.logger.info(f'找到 {len(chapters)} 个章节')
    
    for chapter in chapters:
        current_app.logger.info(f'章节：{chapter.title}')
    
    return render_template('course/course_detail.html', course=course, chapters=chapters)

@course_bp.route('/chapter/<int:chapter_id>')
def chapter_detail(chapter_id):
    """章节详情页面"""
    chapter = Chapter.query.get_or_404(chapter_id)
    return render_template('course/chapter_detail.html', chapter=chapter) 