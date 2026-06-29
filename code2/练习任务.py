#任务一 让程序打印出问候语
print("hello world")

#任务二 用变量存储姓名和年龄，然后输出
name=input('请输入你的姓名')
age=input('请输入你的年龄')
print('你的姓名是',name)
print('你的年龄是',name)
print('你的姓名是',name,'你的年龄是',age)
print('你的姓名是'+name+'你的年龄是'+age)

#任务三 交换两个变量的值并输出交换前后的结果
num1=input('请输入变量一的值')
num2=input('请输入变量二的值')
# x=num1
# y=num2
# num1=y
#  num2=x
print("交换前变量1和2的值",num1,num2)
num1,num2=num2,num1
print("交换后变量1和2的值",num1,num2)

#任务四     输入两个数字，输出四则运算结果
number1=int(input('请输入第一个数字的值'))
number2=int(input('请输入第二个数字的值'))
print("数字相加的结果是",number1+number2)
print("数字相减的结果是",number1-number2)
print("数字相乘的结果是",number1*number2)
print("数字相除的结果是",number1/number2)
