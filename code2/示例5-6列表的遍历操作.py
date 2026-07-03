lst=['hello','world','python','agent']
# for
for  item in lst:
    print(item)

#使用for循环，range（）函数，len()函数，根据索引进行遍历
for item in range(0,len(lst)):
    print(item,lst[item])

#第三种遍历方式 enumearte()函数
for index,iten in enumerate(lst):
    print(index,iten) #index是序号，不是索引、
# 手动修改序号的起始值
for index,iten in enumerate(lst,start=1):
    print(index,iten)

for index,iten in enumerate(lst,1): #省略startb不写，直接写起始值
    print(index,iten)

