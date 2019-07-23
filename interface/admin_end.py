from interface import get_object
login_flag = False


def login():                                                 # 管理员登录函数
    password = input("请输入系统密码：\n")
    global admin
    admin = get_object.get_admin()                           # 重构管理员对象
    global login_flag
    while not login_flag:
        if admin.password == password:                       # 校验密码
            print("登录成功\n")
            login_flag = True
        else:
            password = input("密码错误！\n请重新输入：\n")
    return


def admin_control():                                         # 管理员菜单函数
    login()
    while True:
        menu_2 = {'1': admin.assigned, '2': admin.reg, '3': admin.change, '4':exit}
        choice_2 = input("1：分配区块链地址\n2：学分信息上链\n3：修改密码\n4：退出\n")
        if choice_2 in menu_2.keys():                        # 登录成功后，选择相应操作
            menu_2[choice_2]()
        else:
            print("输入有误，请重新输入\n")
