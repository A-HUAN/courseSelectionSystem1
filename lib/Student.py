# Student类
import os
import pickle
from interface import get_object


class Student(object):
    def __init__(self, name, number, password):
        self.studentName = name   # 学生姓名
        self.studentId = number   # 学生学号
        self.password = password  # 学生登录密码
        self.address = '暂未分配地址'  # 学生区块链地址，初始为无地址
        self.credit = 0           # 学生学分，初始为0
        self.courseDict = {}      # 学生所修课程及成绩（字典）
        return

    def store(self):              # 学生对象存储函数
        top_file = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\student\%s' % (top_file, self.studentName), 'wb') as fd:
            pickle.dump(self, fd)
        with open('%s\dumpfile\student\%s' % (top_file, self.studentId), 'wb') as fd:
            pickle.dump(self, fd)
        return

    def add_course(self):                              # 选课函数
        admin = get_object.get_admin()
        if admin.courseList:
            print("目前已开设以下课程：")              # 输出学校已开设的所有课程（课程名 学分 授课教师）
            for c in admin.courseList:
                print('课程名：%s (%d学分)  授课教师：%s' % (c.courseName, c.courseCredit, c.teacherName))
            choose_course = input("输入你要上的课程名字：\n")
            self.courseDict[choose_course] = '-1'      # 初始化所选课程成绩为“暂无成绩”
            cou_obj = get_object.get_course_obj(choose_course)
            cou_obj.studentList.append(self)           # 选课后在课程对象的学生列表中插入登录学生对象
            cou_obj.store()
            print("选课成功！\n")
            self.store()                               # 存储（更新）登录对象所有相关信息
        else:
            print("暂无课程开设\n")
        return self

    def check_score(self):                             # 查询成绩函数
        if self.courseDict.items():
            for cn, sc in self.courseDict.items():
                if sc == '-1':
                    print("%s 暂无成绩\n" % cn)        # 直接输出登录对象的已选课程字典信息（课程名：成绩）
                else:
                    print(cn, sc)
        else:
            print("你暂未选择任何课程\n")
        return self

    def update(self):                                  # 学分数据更新函数
        for i in self.courseDict.items():
            if i[1] >= '60':                           # 教师给出成绩大于60分时 即算获得该课程相应学分的分值
                c_name = i[0]
                cou_obj = get_object.get_course_obj(c_name)
                self.credit += cou_obj.courseCredit    # 计算所有及格课程学分总值
            else:
                continue
        self.store()
        return self

    def check_credit(self):                            # 查询学分函数
        print("请前往区块链浏览器 http://52.83.95.44:8082/，输入你以下的区块链地址进行查询。")
        print("区块链地址：%s\n" % self.address)
        return self
