# 将字符串反转函数
def str_reverse(s):
    news = str(s)
    return news[::-1]

# 按照x，y字符位置对字符串s进行切片
def substr(s,x,y):
    news = str(s)
    newx = str(x)
    newy = str(y)
    indexX = news.index(newx)   # 查找到s中x所在的下标
    indexY = news.index(newy)
    return news[indexX:indexY:1]

# 模块内测试
if __name__ == '__main__':
   print(str_reverse("我草泥马"))