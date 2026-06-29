from unittest import result

number=eval(input('请输入你的六位中奖号码：'))
if number==888888:
    print('恭喜中奖')
else:
    print('你没中奖，睡觉吧！')

print('--------以上代码可以使用条件表达式进行简化---------')

result='恭喜中奖'   if  number==888888  else"你没中奖，睡觉吧"
print(result)

print('恭喜中奖'  if number==888888  else '你没中奖，睡觉吧')