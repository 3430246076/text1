# #函数-变量的作用域
# #全局变量
# num = 100
#
# #定义函数
# def circle_area(r):
#     #局部变量：只能在函数内部使用
#     pi=3.14
#     area=pi*r*r
#
#     global num
#     num=10000
#     return area
#
# #调用函数
# c_area=circle_area(10)
# print(c_area)
#
# print("num=",num) #10000

#函数——传参方式
#定义函数
# def reg_stu(name,age,gender,city):
#     print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# #传参方式一：位置参数
# stu = reg_stu("张三",18,"男","深圳")
# print(stu)
#
# #传参方式二：关键字参数
# stu=reg_stu(name="王林",age=18,gender="男",city="深圳")
# print(stu)
#
# stu=reg_stu(age=20,gender="女",city="深圳",name="李牧玩",)
# print(stu)
#
#
# #传参方式三：位置参数 + 关键字参数 --->位置参数在前，关键字参数在后
# stu=reg_stu("李牧玩",20,gender="女",city="深圳")
# print(stu)


#函数---默认参数
#定义函数
# def reg_stu(name,age,gender="男",city="上海"):
#     print(f"注册成功，姓名：{name},年龄：{age},性别：{gender},城市：{city}")
#     return {"name":name,"age":age,"gender":gender,"city":city}
#
# #调用函数
# stu=reg_stu("晓燕",20)
# print(stu)
#
# stu=reg_stu("王林",20,"女")
# print(stu)
#
# stu=reg_stu("诸葛亮",45,city="蜀国")

#函数-不定长参数（位置参数 *args --> 元组  ）(关键字参数 **kwargs-->字典)
def calc_date(*args,**kwargs):
    """
    根据传入的这批数据，计算这批数据的最小值，最大值，平均值
    :param args: 不定长位置参数，需要计算的这批数据
    :param kwargs: 不定长关键字参数
            round:保留的小数位个数
            print:是否打印输出
  :return:最小值，最大值，平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    if kwargs.get("round")is not None:
        avg_data = round(avg_data,kwargs.get("round"))
    if kwargs.get("print"):
        print(f"计算出来的最小值{min_data},最大值{max_data},平均值{avg_data}")
    return min_data, max_data, avg_data
#调用函数
print(calc_date(1, 2.3232, 3,3233,2243,434,34,round=3,print=True))