from lib import *
from interface import get_object
login_flag = False


def register():                                               # 学生注册函数
    name = input("请输入您的姓名：\n")
    number = input("请输入您的学号：\n")
    while True:
        password_1 = input("请输入您的密码：\n")
        password_2 = input("请再次输入您的密码：\n")
        if password_1 == password_2:                          # 检验两次输入密码是否一致
            new_student = Student.Student(name, number, password_1)
            new_student.store()                               # 注册成功，储存对象信息
            print("注册成功！\n")
            admin = get_object.get_admin()
            admin.studentList.append(new_student)
            admin.store()                                     # 将新注册学生对象存入管理员学生列表中
            break
        else:
            print("两次密码不一致！\n")
    return student_control()


def login():                                                  # 学生登陆函数
    number = input("请输入您的学号：\n")
    password = input("请输入您的密码：\n")
    global stu_obj
    stu_obj = get_object.get_student_obj('', number)
    global login_flag
    while not login_flag:
        if stu_obj.password == password:                       # 校验密码
            print("登录成功\n")
            login_flag = True
        else:
            password = input("密码错误！\n请重新输入：\n")
    return


def student_control():                                         # 学生菜单函数
    menu_1 = {'1': login, '2': register}
    while not login_flag:
        choice_1 = input("** 1：登录            **\n"                        # 登录/注册界面，登录成功后才可进行后续操作
                         "** 2：注册            **\n")
        if choice_1 in menu_1.keys():
            menu_1[choice_1]()
        else:
            print("输入有误，请重新输入\n")
    while True:
        menu_2 = {'1': stu_obj.add_course, '2': stu_obj.check_score, '3': stu_obj.check_credit, '4': exit}
        choice_2 = input("** 1：选课            **\n"
                         "** 2：查询成绩        **\n"
                         "** 3：查询学分        **\n"
                         "** 4：退出            **\n")
        if choice_2 in menu_2.keys():                          # 登录成功后，选择相应操作
            menu_2[choice_2]()
        else:
            print("输入有误，请重新输入\n")
