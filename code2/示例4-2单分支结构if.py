number=eval(input('请输入你的六位中奖号码：'))
#使用if语句
if number==888888:
    print('恭喜中奖')

if number!=888888:
    print('本期未中奖')
#以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值类型
n=98
if n%2: #98%2的余数是0，0的布尔值类型是False,not False的结果是True
    print(n,'n是奇数')

if not n%2:
    print(n,'n是奇数')

#判断一个字符串是否是空字符串
x=input('请输入一个字符串：')
if x:   #   在python中一切皆对象，每个对象都有一个布尔值，而非空字符串的布尔值为True,空字符串的布尔值为False
    print('x是一个非空字符串')

if not x:
    print('x是一个空字符串')

#使用if语句时，如果语句块中只有一个代码，可以将语句块直接写在冒号的后面
a=10
b=5
if  a>b:max=a   #   语句快只有一句，赋最大值
print('a和b的最大值为',max)
