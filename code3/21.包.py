# 1. 导入模块
# import utils.mu_fun
#
# utils.mu_fun.log_separator1()
# utils.mu_fun.log_separator2()


# from utils import  mu_fun
#
# my_fun.log_separator1()
# my_fun.log_separator2()

#注意：如果要通过from  utils import * 导入包下的所有模块，需要__init__.py 文件中添加__all__=[]
# from  utils import *
#
# my_fun.log_separator2()
# print(my_var.PI)

# 2. 导入模块中的功能
#相对路径：从当前文件夹所在目录开始查找
# from utils.my_fun import log_separator1,log_separator2

#绝对路径：从项目的根目录下开始查找
from code3.utils.my_fun import log_separator1,log_separator2

log_separator1()
log_separator2()