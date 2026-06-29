x=10
y=3
z=x/y   #   在执行除法运算的时候，将运算的结果赋值给z
print(z,type(z))    #   隐式转换，通过运算隐式的转了结果的类型

#flloat类型转换成int类型，只保留整数部分
print('float类型转成int类型：',int(3.4))
print('float类型转成int类型：',int(-3.4))

#   将int转换成Float类型
print('int类型转成float类型：',float(-3))
#   将str转换成int类型
print(int('100')+int('100'))

#将字符串转成int或float时报错的情况
#print(int('18a'))   #ValueError: invalid literal for int() with base 10: '18a'
#print(int('3.14'))  # ValueError: invalid literal for int() with base 10: '3.14'
#print(float('45a233'))  # ValueError: could not convert string to float: '45a233'

#chr()ord()一对
print(ord('杨'))     #杨在unicode表中对应的整数值
print(chr(26472))   #  26472整数在Unicode表中表示对应的字符是什么

#进制之间的转换操作，十进制与其他进制的转换
print('十进制转成十六进制',hex(24672))
print('十进制转成八进制',oct(24672))
print('十进制转成二进制',bin(24672))