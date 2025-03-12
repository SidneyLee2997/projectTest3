"""
初始化课程数据
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

def init_database(app):
    """创建数据库表"""
    with app.app_context():
        db.drop_all()  # 删除所有表
        db.create_all()  # 重新创建表
        print("数据库表创建完成！")

def init_linear_algebra(app):
    """初始化线性代数课程"""
    with app.app_context():
        # 创建线性代数课程
        course = Course(
            title='线性代数基础',
            description='本课程涵盖线性代数的基本概念和应用，包括矩阵运算、向量空间、线性变换等内容。通过本课程的学习，你将掌握解决实际问题所需的线性代数知识。',
            category='linear-algebra'
        )
        db.session.add(course)
        db.session.flush()  # 获取course.id

        # 创建章节
        chapters = [
            {
                'title': '第1章 矩阵基础',
                'content': '''
# 矩阵基础

## 1.1 矩阵的概念与表示

矩阵是一个按照矩形阵列排列的数字集合。一个 m×n 的矩阵有 m 行和 n 列。

### 矩阵的表示方法

一般用大写字母表示矩阵，例如：

\\[
A = \\begin{pmatrix} 
1 & 2 & 3 \\\\
4 & 5 & 6
\\end{pmatrix}
\\]

这是一个2×3矩阵，表示有2行3列。

### 特殊矩阵

1. **零矩阵**: 所有元素都是0的矩阵
\\[
O = \\begin{pmatrix}
0 & 0 \\\\
0 & 0
\\end{pmatrix}
\\]

2. **单位矩阵**: 主对角线上的元素都是1，其他元素都是0的方阵
\\[
I = \\begin{pmatrix}
1 & 0 \\\\
0 & 1
\\end{pmatrix}
\\]

## 1.2 矩阵的基本运算

### 矩阵加法
两个相同维度的矩阵可以相加，结果是对应位置的元素相加。

\\[
\\begin{pmatrix} 
a & b \\\\
c & d
\\end{pmatrix} +
\\begin{pmatrix}
e & f \\\\
g & h
\\end{pmatrix} =
\\begin{pmatrix}
a+e & b+f \\\\
c+g & d+h
\\end{pmatrix}
\\]

### 矩阵数乘
矩阵与标量相乘，结果是矩阵的每个元素都乘以该标量。

\\[
k\\begin{pmatrix}
a & b \\\\
c & d
\\end{pmatrix} =
\\begin{pmatrix}
ka & kb \\\\
kc & kd
\\end{pmatrix}
\\]

### 矩阵乘法
两个矩阵相乘，第一个矩阵的列数必须等于第二个矩阵的行数。

\\[
\\begin{pmatrix}
a & b \\\\
c & d
\\end{pmatrix}
\\begin{pmatrix}
e & f \\\\
g & h
\\end{pmatrix} =
\\begin{pmatrix}
ae+bg & af+bh \\\\
ce+dg & cf+dh
\\end{pmatrix}
\\]

## 1.3 矩阵的转置

矩阵的转置是将矩阵的行和列互换。用 A^T 表示矩阵 A 的转置。

\\[
A = \\begin{pmatrix}
1 & 2 & 3 \\\\
4 & 5 & 6
\\end{pmatrix}
\\]

\\[
A^T = \\begin{pmatrix}
1 & 4 \\\\
2 & 5 \\\\
3 & 6
\\end{pmatrix}
\\]
''',
                'order': 1
            },
            {
                'title': '第2章 行列式',
                'content': '''
# 行列式

## 2.1 行列式的概念

行列式是与方阵相关的一个数值，它反映了矩阵的一些重要特性。行列式用 det(A) 或 |A| 表示。

### 2×2矩阵的行列式

对于2×2矩阵：
\\[
A = \\begin{pmatrix}
a & b \\\\
c & d
\\end{pmatrix}
\\]

其行列式为：
\\[
\\det(A) = \\begin{vmatrix}
a & b \\\\
c & d
\\end{vmatrix} = ad - bc
\\]

### 3×3矩阵的行列式

对于3×3矩阵：
\\[
A = \\begin{pmatrix}
a & b & c \\\\
d & e & f \\\\
g & h & i
\\end{pmatrix}
\\]

其行列式为：
\\[
\\det(A) = a(ei-fh) - b(di-fg) + c(dh-eg)
\\]

## 2.2 行列式的性质

1. **转置不变性**：矩阵与其转置的行列式相等
   \\[\\det(A) = \\det(A^T)\\]

2. **乘法性质**：两个方阵的行列式的乘积等于它们的行列式的乘积
   \\[\\det(AB) = \\det(A)\\det(B)\\]

3. **数乘性质**：标量乘以矩阵的行列式等于标量的n次方乘以原行列式（n为矩阵的阶数）
   \\[\\det(kA) = k^n\\det(A)\\]

## 2.3 行列式的应用

### 求解线性方程组
使用克莱姆法则求解线性方程组：

\\[
\\begin{cases}
ax + by = e \\\\
cx + dy = f
\\end{cases}
\\]

解为：
\\[
x = \\frac{\\begin{vmatrix}
e & b \\\\
f & d
\\end{vmatrix}}{\\begin{vmatrix}
a & b \\\\
c & d
\\end{vmatrix}}, \\quad
y = \\frac{\\begin{vmatrix}
a & e \\\\
c & f
\\end{vmatrix}}{\\begin{vmatrix}
a & b \\\\
c & d
\\end{vmatrix}}
\\]

### 判断矩阵是否可逆
矩阵可逆的充要条件是其行列式不等于0。
''',
                'order': 2
            },
            {
                'title': '第3章 向量空间',
                'content': '''
# 向量空间

## 3.1 向量的基本概念

向量是具有大小和方向的量。在线性代数中，我们通常用有序数组来表示向量。

### 向量的表示方法

n维向量可以写作：

\\[
\\vec{v} = (v_1, v_2, ..., v_n)
\\]

或者用列向量表示：

\\[
\\vec{v} = \\begin{pmatrix}
v_1 \\\\
v_2 \\\\
\\vdots \\\\
v_n
\\end{pmatrix}
\\]

## 3.2 向量的运算

### 向量加法
\\[
\\vec{a} + \\vec{b} = (a_1+b_1, a_2+b_2, ..., a_n+b_n)
\\]

### 标量乘法
\\[
k\\vec{a} = (ka_1, ka_2, ..., ka_n)
\\]

### 点积（内积）
\\[
\\vec{a} \\cdot \\vec{b} = a_1b_1 + a_2b_2 + ... + a_nb_n
\\]

### 叉积（外积，仅适用于三维向量）
\\[
\\vec{a} \\times \\vec{b} = \\begin{pmatrix}
a_2b_3 - a_3b_2 \\\\
a_3b_1 - a_1b_3 \\\\
a_1b_2 - a_2b_1
\\end{pmatrix}
\\]

## 3.3 向量空间的基本性质

1. 加法交换律：\\(\\vec{u} + \\vec{v} = \\vec{v} + \\vec{u}\\)
2. 加法结合律：\\((\\vec{u} + \\vec{v}) + \\vec{w} = \\vec{u} + (\\vec{v} + \\vec{w})\\)
3. 零向量：存在零向量 \\(\\vec{0}\\)，使得 \\(\\vec{v} + \\vec{0} = \\vec{v}\\)
4. 加法逆元：对每个向量 \\(\\vec{v}\\)，存在逆向量 \\(-\\vec{v}\\)
5. 标量乘法的分配律：\\(k(\\vec{u} + \\vec{v}) = k\\vec{u} + k\\vec{v}\\)

## 3.4 线性相关与线性无关

### 线性相关
如果存在不全为零的数字 \\(c_1, c_2, ..., c_n\\)，使得：
\\[
c_1\\vec{v_1} + c_2\\vec{v_2} + ... + c_n\\vec{v_n} = \\vec{0}
\\]
则称向量组 \\(\\vec{v_1}, \\vec{v_2}, ..., \\vec{v_n}\\) 线性相关。

### 线性无关
如果仅当所有系数都为零时，上述等式才成立，则称向量组线性无关。
''',
                'order': 3
            },
            {
                'title': '第4章 线性变换',
                'content': '''
# 线性变换

## 4.1 线性变换的定义

线性变换是保持向量加法和标量乘法的函数 T：V→W，其中V和W是向量空间。

### 线性变换的性质

对于所有的向量 u,v ∈ V 和标量 c，线性变换需满足：

1. 加法保持性：T(u + v) = T(u) + T(v)
2. 标量乘法保持性：T(cu) = cT(u)

## 4.2 线性变换的矩阵表示

每个线性变换都可以用矩阵来表示。对于一个从 \\(\\mathbb{R}^n\\) 到 \\(\\mathbb{R}^m\\) 的线性变换，可以用一个 m×n 的矩阵来表示。

### 常见的线性变换

1. **旋转变换**（二维平面上旋转θ角）：
\\[
\\begin{pmatrix}
\\cos \\theta & -\\sin \\theta \\\\
\\sin \\theta & \\cos \\theta
\\end{pmatrix}
\\]

2. **缩放变换**：
\\[
\\begin{pmatrix}
k & 0 \\\\
0 & k
\\end{pmatrix}
\\]

3. **镜像变换**（关于y轴）：
\\[
\\begin{pmatrix}
-1 & 0 \\\\
0 & 1
\\end{pmatrix}
\\]

## 4.3 特征值和特征向量

### 定义
如果存在非零向量 v 和标量 λ，使得：

\\[
Av = \\lambda v
\\]

则称 λ 是矩阵 A 的特征值，v 是对应的特征向量。

### 特征值的计算

对于矩阵 A，其特征值是特征方程的解：

\\[
\\det(A - \\lambda I) = 0
\\]

### 特征向量的计算

对于每个特征值 λ，求解线性方程组：
\\[
(A - \\lambda I)v = 0
\\]

## 4.4 对角化

如果矩阵 A 有 n 个线性无关的特征向量，则 A 可对角化。

设 P 是由特征向量组成的矩阵，D 是由特征值组成的对角矩阵，则：
\\[
A = PDP^{-1}
\\]

对角化的应用：
1. 计算矩阵的幂
2. 解耦联系统
3. 简化计算
''',
                'order': 4
            }
        ]

        for chapter_data in chapters:
            chapter = Chapter(
                title=chapter_data['title'],
                content=chapter_data['content'],
                order=chapter_data['order'],
                course_id=course.id
            )
            db.session.add(chapter)

        db.session.commit()
        print("线性代数课程初始化完成！")

if __name__ == '__main__':
    app = create_app()
    init_database(app)
    init_linear_algebra(app) 