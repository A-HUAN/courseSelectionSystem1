import os
import pickle
from lib import Admin


def get_course_obj(c_name):                                # 课程对象反序列化函数
    top_file = os.path.dirname(os.path.dirname(__file__))
    with open('%s\dumpfile\course\%s' % (top_file, c_name), 'rb') as fd:
        cou_obj = pickle.load(fd)
    return cou_obj


def get_student_obj(s_name, s_id):                         # 学生对象反序列化函数
    top_file = os.path.dirname(os.path.dirname(__file__))
    try:
        with open('%s\dumpfile\student\%s' % (top_file, s_name), 'rb') as fd:
            stu_obj = pickle.load(fd)
    except FileNotFoundError:
        with open('%s\dumpfile\student\%s' % (top_file, s_id), 'rb') as fd:
            stu_obj = pickle.load(fd)
    return stu_obj


def get_teacher_obj(t_name, t_id):                         # 教师对象反序列化函数
    top_file = os.path.dirname(os.path.dirname(__file__))
    try:
        with open('%s\dumpfile\\teacher\%s' % (top_file, t_name), 'rb') as fd:
            tea_obj = pickle.load(fd)
    except FileNotFoundError:
        with open('%s\dumpfile\\teacher\%s' % (top_file, t_id), 'rb') as fd:
            tea_obj = pickle.load(fd)
    return tea_obj


def get_admin():                                           # 管理员对象反序列化函数
    try:
        top_file = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\\admin\\administrators' % top_file, 'rb') as fd:
            admin = pickle.load(fd)
    except FileNotFoundError:
        admin = Admin.Admin()
        admin.store()
    return admin
