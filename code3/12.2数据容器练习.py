#  字符串案例
# 案例1：邮箱验证格式：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个 . ）,如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"
# email=input("请输入您的邮箱账号")
# c=email.count("@")
# d=email.count(".")
# if c==1 and d>=1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

#方式一：
#1.接受用户输入的邮箱
# mail=input("请输入您的邮箱账号")
#
# # 2 . 判断邮箱的格式
# if mail.count("@")==1 and mail.count(".")>=0:
#     print(f"{mail}是合法邮箱")
# else:
#     print(f"{mail}是非法邮箱")

#方式二：in 运算符 ---> 判断字串是否存在字符串中，存在，返回True;否则，返回False
# 1.接受用户输入的邮箱
mail=input("请输入您的邮箱账号")

# 2 . 判断邮箱的格式
if mail.count("@")==1 and "." in mail:
    print(f"{mail}是合法邮箱")
else:
    print(f"{mail}是非法邮箱")

#练习1，输入一个字符串，判断该字符串是否回文（两边对称）
str=input("请输入一个字符串")
len=len(str)//2
if str[:len]==str[:-(len+1):-1]:
    print(str,"是回文数")
else:
    print(str, "不是回文数")

#练习2，将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来