#输入分数，输出对应等级
score=eval(input("请输入您的分数"))
if 0<=score<=60:
        print("E")
elif 60<=score<=70:
        print("D")
elif 80<=score<=90:
        print("C")
elif 90<=score<=95:
        print("B")
elif 95<=score<=100:
        print("A")
else:
        print("输入的成绩有误")

#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end='\t')
    print()

#实现猜数字游戏
import random
rand=random.randint(1,100) #产生1-100之间的随机数
count=1 #记录猜数的次数
while count<=10:
    num = eval(input("在我心中有个1-100之间的随机数字，你猜一猜"))
    if rand==num :
        print("猜对了")
        break
    elif rand < num:
        print("猜大了")
    else:
        print("小了")
    count=count+1
#判断次数
if count<=3:
    print("真棒，一共猜了",count,"次")
elif count<=6:
    print("还可以，一共猜了",count,"次")
else:
    print("猜的次数有点多，一共猜了",count,"次")
