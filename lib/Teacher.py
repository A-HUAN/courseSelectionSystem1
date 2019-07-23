# Teacher类
import os
import pickle
from interface import get_object
from lib import Course


class Teacher(object):
    def __init__(self, name, number, password):
        self.teacherName = name         # 教师姓名
        self.teacherId = number         # 教师工号
        self.password = password        # 登录密码
        self.courseList = []            # 存放对象创建的course对象
        return

    def store(self):                    # 存储函数
        top_file = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\\teacher\%s' % (top_file, self.teacherName), 'wb') as fd:
            pickle.dump(self, fd)
        with open('%s\dumpfile\\teacher\%s' % (top_file, self.teacherId), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def set_course(self):                # 开设课程函数
        print("** 开设课程 **")
        name = input("请输入课程名称：\n")
        credit = int(input("请输入课程学分：\n"))
        new_course = Course.Course(name, credit, self.teacherName)
        print("开设成功！\n")
        # 存储创建课程对象(按文件名为课程名称存储在dumpfile\course中)
        new_course.store()
        # 将创建课程对象存入教师自身课程列表(Teacher.courseList[])
        self.courseList.append(new_course)
        self.store()
        # 将创建课程存入系统课程列表
        admin = get_object.get_admin()
        admin.courseList.append(new_course)
        admin.store()
        return self

    def reg_score(self):                 # 登记成绩函数
        if self.courseList:
            print("您已开设以下课程：")
            for c in self.courseList:
                print(c.courseName, '  ')    # 输出登录教师对象已创建课程列表
            c_name = input("请输入要登记成绩的课程名字：\n")
            for c in self.courseList:        # 在自身创建课程列表中查找输入课程对象
                if c_name == c.courseName:
                    flag = True              # 若查找成功 查找标志变量为真
                    cou_obj = get_object.get_course_obj(c_name)           # 重构出该课程对象
                    while flag:
                        if cou_obj.studentList:
                            print("该课程有以下学生：")                       # 输出该课程对象下的学生列表
                            for j in cou_obj.studentList:
                                print(j.studentId, ' ', j.studentName, '  ')
                            s_id = input("请输入要登记的学生学号：\n")
                            stu_obj = get_object.get_student_obj('', s_id)  # 查找登记学生学号
                            find_flag = False
                            for j in cou_obj.studentList:
                                if s_id == j.studentId:                   # 查找成功 登记成绩
                                    score = input("请输入学生成绩：\n")
                                    stu_obj.courseDict[c_name] = score
                                    stu_obj.store()
                                    find_flag = True
                                    break
                                else:
                                    find_flag = False                         # 查找失败 输出提示
                            if not find_flag:
                                print("没有这个学生。\n")
                            else:
                                cont = input("继续登记吗？y/n\n")
                                if cont == 'n':
                                    break
                        else:
                            print("暂无学生选择该课程\n")
                            break
        else:
            print("您暂未开设课程\n")
        return self
