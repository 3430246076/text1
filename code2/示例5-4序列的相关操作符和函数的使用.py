
s='HelloWorld!'
print("e在HelloWorld中存在嘛",('e' in s)) #in 的使用
print("v在HelloWorld中存在嘛",('v' in s))


print("e在HelloWorld中不存在嘛",('e' not in s))#inot n 的使用
print("v在HelloWorld中不存在嘛",('v' not in s))

#内置函数的使用
print("len()",len(s))
print("max()",max(s))
print("min()",min(s))

#序列对象的方法，使用序列的名称，打点调用
print('s.index',s.index('o')) # o在s中第一次出现的索引位置4
#print('s.index',s.index('v')) # ValueError: substring not found,报错的原因是v在字符串中不存在，不存在所以找不到
print('s.count()',s.count('o'))#统计o在字符串出现的次数