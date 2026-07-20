#{}直接创建集合
s={10,20,30,40,5}
print(s)

# 集合只能存储不可变数据类型
# s={[110,129,22,2,3],[232,23,23,2,43]} #  TypeError: cannot use 'list' as a set element (unhashable type: 'list')
print(s)

# 使用set()创建集合
s=set() # 创建了一个空集合，空集合的布尔值是False
print(s)

s={}
print(s,type(s)) #dict

s=set('helloword')
print(s,type(s))

s3=set(range(1,10))
print(s3)

#集合属于序列的一种
print('max:',max(s3))
print('min:',min(s3))
print('len',len(s3))

print('9在集合中存在吗',9 in s3)
print('9在集合中不存在吗',9 not in s3)


#集合的删除
 #del s3
# print(s3) #NameError: name 's3' is not defined. Did you mean: 's'?