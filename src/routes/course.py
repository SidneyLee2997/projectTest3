"""
课程相关路由
"""
from flask import Blueprint, render_template, current_app
from models import Course, Chapter
import traceback

course_bp = Blueprint('course', __name__)

@course_bp.route('/')
def index():
    """课程首页"""
    try:
        current_app.logger.info('访问课程首页')
        courses = Course.query.all()
        current_app.logger.info(f'找到 {len(courses)} 个课程')
        return render_template('course/index.html', courses=courses)
    except Exception as e:
        current_app.logger.error(f'访问课程首页出错: {str(e)}')
        current_app.logger.error(traceback.format_exc())
        return render_template('errors/500.html'), 500

@course_bp.route('/list/<category>')
def list_courses(category):
    """课程列表页面"""
    try:
        current_app.logger.info(f'访问课程列表页面，类别: {category}')
        courses = Course.query.filter_by(category=category).all()
        current_app.logger.info(f'找到 {len(courses)} 个{category}类别的课程')
        for course in courses:
            current_app.logger.info(f'课程信息 - ID: {course.id}, 标题: {course.title}')
        return render_template('course/list.html', courses=courses, category=category)
    except Exception as e:
        current_app.logger.error(f'访问课程列表页面出错: {str(e)}')
        current_app.logger.error(traceback.format_exc())
        return render_template('errors/500.html'), 500

@course_bp.route('/linear-algebra')
def linear_algebra():
    """线性代数课程页面"""
    try:
        current_app.logger.info('访问线性代数课程页面')
        course = Course.query.filter_by(category='linear-algebra').first()
        
        if not course:
            current_app.logger.error('未找到线性代数课程')
            return render_template('errors/404.html'), 404
        
        current_app.logger.info(f'找到课程 - ID: {course.id}, 标题: {course.title}')
        chapters = Chapter.query.filter_by(course_id=course.id).order_by(Chapter.order).all()
        current_app.logger.info(f'找到 {len(chapters)} 个章节')
        
        for chapter in chapters:
            current_app.logger.info(f'章节信息 - ID: {chapter.id}, 标题: {chapter.title}, 顺序: {chapter.order}')
            current_app.logger.info(f'章节内容预览: {chapter.content[:100]}...')
        
        return render_template('course/course_detail.html', course=course, chapters=chapters)
    except Exception as e:
        current_app.logger.error(f'访问线性代数课程页面出错: {str(e)}')
        current_app.logger.error(traceback.format_exc())
        return render_template('errors/500.html'), 500

@course_bp.route('/chapter/<int:chapter_id>')
def chapter_detail(chapter_id):
    """章节详情页面"""
    try:
        current_app.logger.info(f'访问章节详情页面，章节ID: {chapter_id}')
        chapter = Chapter.query.get_or_404(chapter_id)
        current_app.logger.info(f'找到章节 - ID: {chapter.id}, 标题: {chapter.title}')
        return render_template('course/chapter_detail.html', chapter=chapter)
    except Exception as e:
        current_app.logger.error(f'访问章节详情页面出错: {str(e)}')
        current_app.logger.error(traceback.format_exc())
        return render_template('errors/500.html'), 500 