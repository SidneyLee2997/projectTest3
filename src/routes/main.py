"""
主页路由
"""
from flask import Blueprint, render_template
from models import Course

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """主页"""
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@main_bp.route('/about')
def about():
    """关于页面"""
    return render_template('about.html') 