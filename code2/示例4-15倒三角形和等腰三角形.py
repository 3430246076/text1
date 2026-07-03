#倒三角形
#1--->5 range(1,6)  , 2--->4 range(1,5) , 3-->3range(1,4)....5-->range(1,2)
for i in range(1,6):    # i表示的是行号，第一行
    for j in range(1,7-i):# 内层循环
        print("*",end=" ")
    print() #空的print语句，作用是换行
    print("-" * 20)
    #等腰三角形
''''
????*
???***
??*****
?********
**********
'''
for i in range(1,6):  #外层循环五行
    #倒三角行
    for j in range(1,7-i):
        print(" ",end=" ")
        #1，3，5，7。。。等腰三角形range(1,2),range(1,4),range(1,6),range(1,8)...
    for k in range(1,2*i):
        print("*",end=" ")
    print() #当两个并列的for循环执行完毕时，在换行