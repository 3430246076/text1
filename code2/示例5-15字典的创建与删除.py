#1，创建字典
d={10:"cat",20:"dog",20:"zoo"}
print(d) # key相同时，value值进行了覆盖

#2，zip函数
lst1=[10,20,30,40]
lst2=["cat","dog","zoo","car"]
zipobj=zip(lst1,lst2)
print(zipobj)
d=tuple(zipobj)
print(d)

# 使用参数创建字典
d=dict(cat=10,dog=29) #左侧cat是键 ，右侧的是value
print(d)

t=(10,20,30)
print({t:10})#   t是key,10是value,元组是可以作为字典中的key

# lst=[10,20,30]
# print({lst:10}) #TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

#字典属于序列
print("max:",max(t))
print("min:",min(t))
print("len:",len(t))
#字典的删除
# del d
# print(d)



