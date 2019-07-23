from lib import Teacher
from interface import get_object
login_flag = False


def register():                                          # 教师注册函数
    name = input("请输入您的姓名：\n")
    number = input("请输入您的工号：\n")
    while True:
        password_1 = input("请输入您的密码：\n")
        password_2 = input("请再次输入您的密码：\n")
        if password_1 == password_2:                     # 校对两次输入密码是否一致
            new_teacher = Teacher.Teacher(name, number, password_1)
            new_teacher.store()                          # 注册成功，储存对象信息
            print("注册成功！\n")
            break
        else:
            print("两次密码不一致！\n")
    return teacher_control()


def login():                                             # 教师登录函数
    number = input("请输入您的工号：\n")
    password = input("请输入您的密码：\n")
    global tea_obj
    tea_obj = get_object.get_teacher_obj('', number)
    global login_flag
    while not login_flag:
        if tea_obj.password == password:                 # 校对密码
            print("登录成功！\n")
            login_flag = True
        else:
            password = input("密码错误！\n请重新输入：\n")
    return


def teacher_control():                                   # 教师菜单函数
    menu_1 = {'1': login, '2': register}
    while not login_flag:
        choice_1 = input("** 1：登录            **\n"    # 登录/注册界面 登录成功后才可进行后续操作
                         "** 2：注册            **\n")
        if choice_1 in menu_1.keys():
            menu_1[choice_1]()
        else:
            print("输入有误，请重新输入\n")
    while True:
        menu_2 = {'1': tea_obj.set_course, '2': tea_obj.reg_score, '3': exit}
        choice_2 = input("** 1：开设课程        **\n"
                         "** 2：登记学生成绩    **\n"
                         "** 3:退出             **\n")
        if choice_2 in menu_2.keys():                    # 登录成功后，选择相应操作
            menu_2[choice_2]()
        else:
            print("输入有误，请重新输入\n")
