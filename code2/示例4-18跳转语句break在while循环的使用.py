s=0  #存储累加和
i=1  #1.初始化变量
while i<11: #2。条件判断
    #3.语句块    s=s+i
    s+=i
    if s>20:
        print("累加和大于20的当前数是",i)
        break
    i+=1  #4.改变变量


i=0 #统计登录次数
while i<3:  #   2.条件判断
    #3.语句块
    user_name=input("请输入你的用户名：")
    pwd=input("请输入您的密码：")
    #登录操作  if...else..
    if user_name=="paofu"  and pwd=="666":
        print("正在登录中。。。")
        break #  4.改变变量
    else:
        if i<2:
            print("用户名或密码不正确，您还有",2-i,"次机会")
    i+=1  #   改变变量
else: #while..else
    print("对不起，三次均输错")
