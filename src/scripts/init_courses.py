"""
初始化课程数据
"""
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from config import Config
from models import db, Course, Chapter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # 打印数据库路径
    logger.info(f"数据库路径: {app.config['SQLALCHEMY_DATABASE_URI']}")
    db.init_app(app)
    return app

def init_database(app):
    """创建数据库表"""
    with app.app_context():
        # 确保instance文件夹存在
        os.makedirs('instance', exist_ok=True)
        db.drop_all()  # 删除所有表
        db.create_all()  # 重新创建表
        logger.info("数据库表创建完成！")

def init_linear_algebra(app):
    """初始化线性代数课程"""
    with app.app_context():
        try:
            # 创建线性代数课程
            course = Course(
                title="线性代数基础",
                description="本课程将带您深入理解线性代数的核心概念，包括矩阵运算、行列式、向量空间和线性变换等。",
                slug="linear-algebra"
            )
            db.session.add(course)
            db.session.flush()
            logger.info(f"创建课程: {course.title}")
            
            # 创建章节
            chapters = [
                Chapter(
                    title="矩阵基础",
                    content="""
# 矩阵基础

## 什么是矩阵？
矩阵是一个按照长方形阵列排列的复数或实数集合。在线性代数中，矩阵是最基本和最重要的概念之一。

### 零矩阵
所有元素都为0的矩阵称为零矩阵：
![零矩阵示例](/static/images/linear-algebra/zero_matrix.svg)

### 单位矩阵
主对角线上的元素为1，其他元素为0的方阵称为单位矩阵：
![单位矩阵示例](/static/images/linear-algebra/identity_matrix.svg)

## 矩阵运算

### 矩阵加法
矩阵加法是将两个相同维度的矩阵对应位置的元素相加：
![矩阵加法](/static/images/linear-algebra/matrix_addition.svg)

### 矩阵乘法
矩阵乘法遵循特定的规则，结果矩阵中的每个元素都是第一个矩阵的行与第二个矩阵的列的点积：
![矩阵乘法](/static/images/linear-algebra/matrix_multiplication.svg)

## 实际应用
在计算机图形学中，我们经常使用矩阵来表示和计算物体的变换。例如，旋转、缩放和平移都可以用矩阵来表示。
""",
                    course=course,
                    order=1
                ),
                Chapter(
                    title="向量空间",
                    content="""
# 向量空间

## 向量的基本概念
向量是具有大小和方向的量。在几何上，我们可以用箭头来表示向量：
![向量表示](/static/images/linear-algebra/vector_representation.svg)

## 向量运算
- 向量加法：头尾相连法
- 向量数乘：改变向量的大小或方向

## 向量空间的性质
1. 封闭性
2. 结合律
3. 交换律
4. 零向量
5. 负向量
""",
                    course=course,
                    order=2
                )
            ]
            
            for chapter in chapters:
                db.session.add(chapter)
                logger.info(f"创建章节: {chapter.title}")
            
            db.session.commit()
            logger.info("线性代数课程初始化完成！")
            
        except Exception as e:
            db.session.rollback()
            logger.error(f"初始化过程中出错: {str(e)}")
            raise

if __name__ == '__main__':
    app = create_app()
    init_database(app)
    init_linear_algebra(app) 