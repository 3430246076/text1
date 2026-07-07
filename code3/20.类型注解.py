# #变量定义 - 未指定类型注解 ---> 类型推断
#
# a = 590
# score = 232.23
# hobby = "Python"
# flag = True
#
# name=["A","B","C","D","E","F","G","H","I","J"]
# phones = {"1291039203","1327387483","3232321232"}
# options = {"count":2,"total":10}
#
# name.append("P")
# name.append(10010)
# name.append(12120.21)
#
# print(name)
#
#
# #变量定义 - 指定类型注解
# a:  int= 590
# score: float = 232.23
# hobby: str = "Python"
# flag: bool = True
#
# name:list[str | int]=["A","B","C","D","E","F","G","H","I","J"]
# phones: set[str] = {"1291039203","1327387483","3232321232"}
# options: dict[str,int] = {"count":2,"total":10}

#函数类型注解
def circle_area_len(r: float) ->tuple[float,float]:
    return round(3.14 * r * 1,1),round(2*3.14*r,1)

al = circle_area_len(10)
print(al)

def caic_order_cost(*args: tuple[str,int,int],coupon: int=0,score: int   =0,express: float=0.0) -> float:
    """
    根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数
    :param args:商品信息(商品名、价格、数量)  ---->  eg:("鼠标",188,2),("键盘",288,2)
    :param coupon:优惠卷
    :param score:积分
    :param express: 运费
    :return: 订单的总金额
    """
#订单的总金额  = 商品总金额 - 优惠卷  - 积分抵扣 + 运费
# 1. 计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
#2.扣减优惠卷
    if total_cost >= 5000 and total_cost <= coupon:
        total_cost -= coupon
#  3. 扣减积分抵扣
    if total_cost >= 5000 and score//100 <= coupon:
        total_cost -= score//100
# 4. 添加运费
    total_cost +=express
    return total_cost

#测试

# total=caic_order_cost(("鼠标",188,2),("键盘",288,2),("电脑",199,2),coupon=10,score=100,express=9.9)
# print(total)

# total=caic_order_cost(("鼠标",188,2),("键盘",288,2),("电脑",19429,2),coupon=10,score=100,express=9.9)
# print(total)

total=caic_order_cost(("鼠标",188,2),("键盘",288,2),("电脑",199,2),express=9.9)
print(total)