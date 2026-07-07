#案例1：定义一个函数：根据函数传入的底和高计算三角形面积的函数（三角形面积+底*高/2）
def triangle_area(d,h):
    """
    根据传入的底和高计算三角形面积的函数
    :param d: 底长
    :param h: 高
    :return: 三角形面积
    """
    return d*h/2

print("底长为30，高度为20的三角形面积：",triangle_area(30,20))

#案例2：定义一个函数：计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU）
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    count = 0
    for w in s:
        if w in 'aeiouAEIOu':
            count+=1
    return count

print(count_aeiou("hello-World"))

#案例3:定义一个函数;计算传入的班级成员高考成绩的最高分、最低分、平均分（保留一位小数），并返回
def calc_score(score_list):
    """
    计算传入的班级成员高考成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分，最低分，平均分
    """
    max_s=max(score_list)
    min_s=min(score_list)
    avg_s=round(sum(score_list)/len(score_list),1)
    return max_s,min_s,avg_s

s_list=[123,324,456,767,878,676]
max_score,min_score,avg_score=calc_score(s_list)
print("最高分",max_score)
print("最低分",min_score)
print("平均分",avg_score)

#练习一：1.定义一个函数，根据传入的分数，计算对应的分数等级并返回。分数>= 90:A 分数>= 75:B 分数>=60:C 分数<60:D
def score(num):
    """
    根据传入的分数，计算对应的分数等级
    :param num: 传入的分数
    :return: 对应分数等级
    """
    if num>=90:
        level="A"
    elif num>=75:
        level="B"
    elif num>=60:
        level="C"
    else:
        level="D"
    return level

print(score(13))