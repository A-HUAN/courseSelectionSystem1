# CourseList类
import os
import pickle
from interface import get_object


class Admin(object):
    def __init__(self):
        self.password = 'admin'
        self.accountAlias = 'admin'            # 区块链账户别名
        self.accountID = '0SHDEG5400A02'       # 区块链账户ID
        self.accountAddress = 'tm1qrnmwxz664xga08um7j2jescgxpsckp7gqcjtxg'  # 区块链账户主地址
        self.courseList = []                   # 所有课程对象列表
        self.studentList = []                  # 所有学生对象列表
        return

    def store(self):                           # 存储函数
        top_file = os.path.dirname(os.path.dirname(__file__))
        with open('%s\dumpfile\\admin\\administrators' % top_file, 'wb') as fd:
            pickle.dump(self, fd)
        return

    def change(self):                          # 修改密码函数
        password1 = input("请输入你的新密码：\n")
        password2 = input("请再次输入你的新密码：\n")
        if password1 == password2:
            self.password = password2
        self.store()
        print("密码修改成功！\n")
        return self

    def reg(self):                             # 学分信息上链函数
        if self.studentList:
            for s in self.studentList:
                s_name = s.studentName
                stu_obj = get_object.get_student_obj(s_name, '')
                stu_obj.update()
                print("学号：%s,姓名：%s,学分：%s,地址：%s \n"
                      % (stu_obj.studentId, stu_obj.studentName, stu_obj.credit, stu_obj.address))
        else:
            print("暂无学生信息\n")
        return self

    def assigned(self):                        # 学生区块链地址分配函数
        for s in self.studentList:
            s_name = s.studentName
            stu_obj = get_object.get_student_obj(s_name, '')
            if stu_obj.address == '暂未分配地址':
                print("学号：%s,姓名：%s  暂未分配地址" % (stu_obj.studentId, stu_obj.studentName))
                stu_obj.address = input("请输入该学生区块链地址：")
                stu_obj.store()
            else:
                continue
        print("所有学生均已分配区块链地址！\n")
        return self
