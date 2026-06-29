from sys import prefix

height=187.6    #         身高
print(height)
print(type(height)) #   type()查看height这个变量的数据类型

x=10
y=10.0
print('x的数据类型是',type(x))#int
print('y的数据类型是',type(y))#float

x=1.99E1212
print('科学计数法',x,'x的数据类型是',type(x))

print(0.1+0.2)     #    不确定的尾数问题    0.30000000000000004

print(round(0.1+0.2,1))     #   0.3    round函数保留函数