# 相加函数
def add(x,y):
    return x+y

# 相乘函数
def chengfa(x,y):
    return x*y

# 模块内部测试函数
def test(x,y):
    print(x-y)
# 直接这样写，调用该模块的文件也会执行这段测试代码
# test(7,2)
# 解决该问题需要使用__name__来判断模块是不是主函数运行
if __name__ == '__main__':
    test(7,2)

# 自定义暴露出去的所有功能（test使用不了）
__all__ = ['add','chengfa']  # 模块import  *来源于__all__