d={1001:"泡芙",1002:"木马",1003:"泡面",1004:"随便"}
print(d)

#向字典中添加元素
d[1005]="芒果" # 直接使用赋值运算符向字典中添加元素
print(d)

#获取字典中所有的key
keys=d.keys()
print(keys)#对性 dict_keys([1001, 1002, 1003, 1004, 1005])
print(list(keys))
print(tuple(keys))

#获取字典中所有的value
values=d.values()
print(values)
print(list(values))
print(tuple(values))

#如果将字典中的数据转成key-value的形式，以元组的方式进行展示
lst=list(d.items())
print(lst)

d=dict(lst) #转成字典类型
print(d)

#使用pop函数
print(d.pop(1001))
print(d)

print(d.pop(1001,'不存在'))

#随机删除
print(d.popitem())
print(d)

#清空字典中所有元素
d.clear()
print(d)
#Python中一切皆对象，每个对象都有一个布尔值
print(bool(d)) #空字典的布尔值为False