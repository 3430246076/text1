for i in "hello":
    if i=="e":
        break
    print(i)
print("-----------")
for i in range(3):
    # 3.语句块
    user_name = input("请输入你的用户名：")
    pwd = input("请输入您的密码：")
    # 登录操作  if...else..
    if user_name == "paofu" and pwd == "666":
        print("正在登录中。。。")
        break  # 4.改变变量
    else:
        if i < 2:
            print("用户名或密码不正确，您还有", 2 - i, "次机会")
    i += 1  # 改变变量
else:  # while..else
    print("对不起，三次均输错")