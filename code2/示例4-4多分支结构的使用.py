score=eval(input('请输入你的成绩'))
#   多分支结构
if score<0 or score>100:
    print('成绩有误')
elif 0<=score<60:
    print('e')
elif 60<=score<70:
    print('d')
elif 70<=score<80:
    print('c')
elif 80<=score<90:
    print('b')
else:
    print('a')