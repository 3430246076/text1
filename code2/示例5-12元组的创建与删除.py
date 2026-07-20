#使用小括号创建元组
t=('hello','world',[10,20,40],'python')
print(t)

#使用内置函数tupe()创建元组
t=tuple("helloworld")
print(t)

t=tuple([10,20.102])
print(t)

print('10在元组是否存在',(10 in t))
print('10在元组是不存在',(10 not in t))
print("最大值",max(t))
print("最小值",min(t))
print("len:",len(t))
print("t.index",t.index(10))
print("t.count(t)",t.count(10))

#如果元组中只有一个元素
t=(10)
print(t,type(t))  # int

#如果元组只有一个元素，逗号不能省
y=(10,)
print(y,type(y))

#元组的删除
del  t
print(t)