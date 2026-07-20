"""
===== 记账小程序 =====
1. 添加收入
2. 添加支出
3. 查看记录
4. 查看统计
5. 退出

请选择: 1

请输入金额: 5000
请输入类型: 工资
请输入备注: 月薪
✓ 添加成功！

请选择: 4

【财务统计】
总收入: 5000元
总支出: 0元
当前余额: 5000元
"""

class  accounts:
    def __init__(self,income = 0,outcome = 0,lable = "工资",eg="月薪"):
        self.income = income
        self.outcome = outcome
        self.lable = lable
        self.eg = eg

    # def __str__(self):
    #     """
    #     【财务统计】
    #     总收入: 5000元
    #     总支出: 0元
    #     当前余额: 5000元
    #     """
    #     return f"总收入:{self.income}元\n 总支出:{self.outcome}元\n 当前余额:{self.income-self.outcome}"


class money:
    #设置一个空列表,存储数据
    def __init__(self):
        self.money_list = [] # 列表,记录的记账本的数据

    # 1.添加收入
    def accounts_add(self):
        total_income = 0 #初始化收入
        income = int(input("请输入金额"))
        lable = input("请输入类型")
        eg = input("请输入备注")
        # 判断金额大于等于0
        if income >= 0:
            inc = accounts(income=income,lable=lable,eg=eg)
            self.money_list.append(inc)
            # 收入累加
            for s in self.money_list:
               total_income += s.income
            print("✓添加成功")
            return
        print("添加失败")

    #2.添加支出
    def  accounts_lest(self):
        total_outcome = 0
        outcome = int(input("请输入当月支出"))
        # 判断支出大于等于0
        if outcome >= 0:
            outc = accounts(outcome=outcome)
            self.money_list.append(outc)
            #支出累加
            for s in self.money_list:
                total_outcome += s.outcome
            print(f"当月支出为{total_outcome}")
            return
        print("添加失败")

    # 3.查看记录
    def accounts_look(self):
        if len(self.money_list) == 0:
            print("暂无记录！")
            return
        print("===== 记账记录 =====")
        for i, s in enumerate(self.money_list, 1):
            if s.income > 0:
                print(f"{i}. [收入] 金额:{s.income}元 类型:{s.lable} 备注:{s.eg}")
            elif s.outcome > 0:
                print(f"{i}. [支出] 金额:{s.outcome}元 类型:{s.lable} 备注:{s.eg}")
        print(f"共 {len(self.money_list)} 条记录")

    #4.查看统计
    def accounts_every(self):
        total_income = total_outcome =0
        for s in self.money_list:
            total_income += s.income
            total_outcome += s.outcome
        print("[财务统计]")
        print(f"总收入: {total_income}元")
        print(f"总支出: {total_outcome}元")
        print(f"当前余额: {total_income - total_outcome}元")



    #运行系统
    def run(self):
        while True:
            print()

            print("===== 记账小程序 =====\n")
            print("1.添加收入")
            print("2.添加支出")
            print("3.查看记录")
            print("4.查看统计\n")
            chioce = input("请选泽:")
            print()
            match chioce:
                case "1": #1.添加收入
                    self.accounts_add()
                case "2": # 2.添加支出
                    self.accounts_lest()
                case "3":
                    self.accounts_look()
                case "4":
                    self.accounts_every()
                case "5":
                    print("退出")
                    break
                case _:
                    print("输入错误,请选泽1-4之间的菜单功能!")

#测试
if __name__ == "__main__":
    money_count = money()
    money_count.run()
