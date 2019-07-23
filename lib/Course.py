# Course类
import os
import pickle


class Course(object):
    def __init__(self, name, credit, tea_name):
        self.courseName = name             # 课程名称
        self.courseCredit = credit         # 课程学分
        self.studentList = []              # 选择该课程的学生列表（列表）
        self.teacherName = tea_name        # 创建该课程的教师姓名
        return

    def store(self):                       # 存储函数
        top_file = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\course\%s' % (top_file, self.courseName), 'wb') as fd:
            pickle.dump(self, fd)
        return
