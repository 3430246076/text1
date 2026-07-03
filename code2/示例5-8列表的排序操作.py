lst=[1,12,43,4,55,96]
print('原列表',lst)

#排序，默认是升序
lst.sort() # 排序是在原列表的基础上进行的，不会产生新的制表对象
print('升序：',lst)

#排序，降序
lst.sort(reverse=True)
print('降序',lst)

lst2=['banann','apple','Cat',"Orange"]
print('原列表',lst2)
#升序排序，先排大写，在排小写
lst2.sort()
print('升序:',lst2)
#降序，先排小写，在排大写
lst2.sort(reverse=True)
print('降序',lst2)

#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)