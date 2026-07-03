lst=[1,12,43,4,55,96]
print('原列表',lst)
#排序
new_lst=sorted(lst)
print('原列表',lst)
print('升序',new_lst)
#降序
new_lst=sorted(lst,reverse=True)
print('原列表',lst)
print('降序',new_lst)

lst2=['banann','apple','Cat',"Orange"]
print('原列表',lst2)

#忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表',lst2)
print('排序后的列表',new_lst2)