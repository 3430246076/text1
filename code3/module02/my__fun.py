# _ _ all_ _指定from ...import * 导入的的是那些功能
__all__ =["PI","log_separator1"]
#常量（不会发生变化的数据；常量的名称为全部大写）
PI = 3.14159
NAME = "泡芙"

#函数
def log_separator1() :
    print("-" * 30)

def log_separator2() :
    print("#" * 30)

def log_separator3() :
    print("_" * 30)


def log_separator4() :
    print("=" * 30)

#测试函数
#_ _name_ _: Python中内置变量，表示的当前模块的名字（直接运行当前模块,_ _name_ _的值为"_ _main_ _";当该模块被导入时，_ _name_ _的值就是模块名称）
#执行当前文件，则回执行如下代码;如果被当做模块导入，如下代码不执行;
if __name__ == '__main__':
    log_separator1()