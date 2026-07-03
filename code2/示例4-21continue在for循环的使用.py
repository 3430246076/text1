s=0
i=1
for i in range(1,101):
    if i%2==1:
        i+=1
        continue # 不在执行后面的代码
    s+=i
print("1-100之间的偶数和",s)