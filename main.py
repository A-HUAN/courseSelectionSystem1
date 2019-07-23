# main.py
from interface import teacher_end, student_end, admin_end


def main():
    main_menu = {'1': teacher_end.teacher_control,       # 进入教师接口终端
                 '2': student_end.student_control,       # 进入学生接口终端
                 '3': admin_end.admin_control,           # 进入管理员终端
                 '4': exit}
    while True:
        print("**欢迎进入学分管理系统**")
        main_choice = input("** 1: 教师端登录      **\n"
                            "** 2: 学生端登录      **\n"
                            "** 3: 管理员登录      **\n"
                            "** 4: 退出            **\n")
        if main_choice in main_menu.keys():
            while True:
                main_menu[main_choice]()
        else:
            print("输入错误，请重新输入")


while True:
    main()

