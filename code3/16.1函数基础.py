#注意：函数定义的时候变并不会执行，只有在调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用

#函数调用
# def out_line():
#     print("---------------------------")
#     print("---------------------------")
#
# out_line()
#
# out_line()

#函数的参数与返回值
#函数1：计算圆的面积 --- 半径
# def circle_area(r):
#     area=3.14*r**2
#     return area
#
# area = circle_area(5)
# print(area)

#函数2：计算长方形的面积 --- 长，宽
# def  rectangle_area(l,w):
#     """
#     根据长方形的长度和宽度，计算长方形的面积
#     :param l:长度
#     :param w:宽度
#     :return:长方形的面积
#     """
#     area=l*w
#     return area
#
# # help(rectangle_area)
# print(rectangle_area(10,20))



#函数3：计算圆的面积，周长 -- 半径 --->如果返回值有多个，多个返回值之间逗号分割 --->多个返回值回封装到元组之中
# def circle_area_len(r):
#     """
#     根据圆的半径，计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(3.14 * r * 1,1),round(2*3.14*r,1)
#
# al = circle_area_len(10)
# print(al)
# print(type(al))
#
# area,len=circle_area_len(10) # 解包
# print(area)
# print(len)


#函数的嵌套调用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ... before")

function_a()

print("函数调用完毕")