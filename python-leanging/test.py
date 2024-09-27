# print("hello world")
# # print("hello")
# # print(11)
#
# # print("hlle")
# # 萨达
# # 阿斯顿
# # ad
# # 阿迪斯
# """jjjj
#
# """
# money = 50
# a = 10
# print("钱包有：",money,a)
# money = money - a
# print(money)
# money =50
#
# ice = 10
# coco = 3
# print("当前余额：",money)
# print("买完冰淇淋：",money - ice)
# money = money - ice
# print("买完可乐：",money - coco)
# print(type(money))

# money = 50
# print(float(money)) # int类型转float浮点型
# print(type(str(money))) # int类型转str字符串
#
# print(int(5/3)
# name = '黑马程序员'
# name = "黑马程序员"
# name1 = """黑马程序员"""
# print(type(name1))

# # 用双引号包裹单引号字符串
# name = "'刘凯'"
# print(name)
#
# # 用单引号包裹双引号字符串
# name1 = '"刘凯"'
# print(name1)
#
# # 用（\）转义字符来将引号解除效用变成普通字符串
# name2 = '\"刘凯\''
# print(name2)

# name = "刘凯"
# gender = "男"
# university = "南京信息工程大学"
# print("我叫"+name+",性别"+gender+",就读于"+university)

# name = "刘凯"
# age = 18
# weight = 75.5
# message = "我叫%s，今年%d岁，体重%3.2f公斤" % (name,age,weight)
# print(message)

# name = "刘凯"
# age = 18
# weight = 75.5
# message = f"我叫{name},今年{age}岁,体重{weight}"
# print(message)

# print("2*8的结果是：%d" % (2*8))
# print(f"4*5的结果是：{4*5}")
# print("字符串在python的数据类型是：%s" % (type("python")))

# name = "传智博客"
# stock_price = 19.99
# stock_code = "003032" # 股票代码
# stock_price_daily_growth_factor = 1.2 # 股票每日增长系数
# growth_day = 7
# print("公司：%s，股票代码：%s，当前股价：%d" % (name,stock_code,stock_price))
# print(f"每日增长系数{stock_price_daily_growth_factor}，经过{growth_day}天的增长后，股票达到了：{stock_price*stock_price_daily_growth_factor**growth_day}")
# print("股票价格保留两位小数为：%.2f" % (stock_price*stock_price_daily_growth_factor**growth_day))
#

# # 输入input
# print("请输入你的名字")
# name = input()
# # 以上两行等价于 name = input("请输入你的名字")
# print("所以你是%s" % (name))


# 将input输入的数据转换成数字类型
# num = int(input())
# print(type(num))

# if语句
# age = 10
# if age>20:
#     print("你已经成年了")
#
# print("哈哈哈，真快啊") # 未进入if判断语句

# age = int(input("请输入你的年龄"))
# if age >=18:
#     print("你成年了请付款50元")
# if age <18:
#     print("免费游玩")
# print("祝您游玩愉快")

# age = int(input("请输入你的年龄"))
# if age >=18:
#     print("你成年了请付款50元")
# else:
#     print("免费游玩")
# print("祝您游玩愉快")

# height = int(input("请输入您的身高"))
# if height >=130:
#     print("您的身高超过130，请买票")
# else:
#     print("您的身高未超过130，免费游玩")

# height = int(input("请输入您的身高："))
# vip = int(input("请输入您的vip："))
# if height <130:
#     print("您的身高未超过130，免费游玩")
# elif vip >=3:
#     print("您的是高贵的VIP客户免费游玩")
# else:
#     print("请付款50元")

# age = int(input("年龄"))
# if age >=18:
#     if age <=50:
#         print("50元")
#     else:
#         print("超过50岁可以免费")
# else:
#     print("年龄小于18可以免费玩")
#
# import random
# num = random.randint(1,10)
# game_num = int(input("1~10猜一个数字"))
# if game_num == num:
#     print(f"猜对了，它是{num}")
# else:
#     if game_num > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#
#     game_num = int(input("1~10再猜一个数字"))
#
#     if game_num == num:
#         print(f"猜对了，它是{num}")
#     else:
#         if game_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#
#         game_num = int(input("1~10第三次猜一个数字"))
#
#         if game_num == num:
#                 print(f"猜对了，它是{num}")
#         else:
#                 print("没有猜对")


# import random
# t = 0;
# num = random.randint(1, 10)
# flag = False
# while  flag:
#     game_num = int(input(f"1~10第{t}次猜一个数字"))
#     if game_num == num:
#         print(f"猜对了，它是{num}")
#
#     else:
#         if game_num > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#     t+=1


# print("hello\tworld")
# print("welcome\tworld")
# print("你好",end="")
# print("hello")

# i = 1
# while i<=9:
#     j = 1
#     while j<=i:
#         print(f"{j}*{i}={i*j}\t",end="")
#         j+=1
#     print()
#     i+=1

# name = "itheima"
# for x in name:
#     print(x)

# name = "itheima is a brand of itcast"
# count = 0 # 计算name中有多少个a
# for x in name:
#     if x=="a":
#         count+=1
# print(f"name中一共有{count}个a")

# for x in range(10):
#     print(x)

# for x in range(5,10):
#     print(x)
#
# for x in range(5,10,2):
#     print(x)

# num = 100
# count = 0
# for x in range(1,num+1):
#     if x%2==0:
#         count+=1
# print(count)
# x = 0
# for x in range(10):
#     print(x)
# print(x)

# i = 1
# for i in range(1,10):
#     j = 1
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end="")
#         j+=1
#     print()
#     i+=1

# import random
# sum = 10000
# for x in range(1,21):
#     num = random.randint(1, 10)
#     if  num < 5:
#         print(f"员工{x}，绩效{num}，低于5，不发工资，下一位")
#         continue
#     elif sum == 0:
#         print("工资发完了")
#         break
#     else:
#         sum = sum - 1000
#         print(f"向员工{x}发放工资1000，账户余额{sum}元")

# str1 = "itheima"
# str2 = "helloworld"
# str3 = "liukai"
#
# def my_len(data):
#     count = 0
#     for i in data:
#         count+=1
#     print(f"字符串{data}共有{count}")
#
# my_len(str1)
# my_len(str2)
# my_len(str3)

# def check():
#     print("欢迎来道南京信息工程大学")
# check()

# def add(x,y):
#     result = x+y
#     return result
#
# a = 10
# b = 20
# sum = add(a,b)
# print(sum)

# def get(tem):
#     if tem > 37.5:
#         print(f"{tem}您需要隔离")
#     elif tem < 35:
#         print(f"温度{tem}过低请保暖")
#     else:
#         print(f"体温{tem}正常请进")
#
# import random
#
# for x in range(1,20):
#     tem1 = random.randint(30, 40)
#     get(tem1)
#
# def ten():
#     print("hello")
#
# a = ten()
# print(a)

# def check(age):
#     if age>18:
#         return "success"
#     else:
#         return None
#
# result = check(16)
# if not result:
#     print(result)

# def fun():
#     """
#
#     :return:
#     """

# money = 5000000
# name = ""
# def check_balance():
#     #     查看余额函数
#     print(f"{name}你好，当前您的余额是{money}")
#
# def deposit():
#     # 存款函数
#     print("请输入您要存款的数额")
#     d_money = int(input())
#     global money  # 声明money是全局变量
#     money += d_money # 余额加上存款
#     check_balance()
#
# def withdraw_money():
#     # 取款函数
#     print("请输入您要取款的数额")
#     w_money = int(input())
#     global money  # 声明money是全局变量
#     money -= w_money  # 余额加上存款
#     check_balance()
#
# def ATM_fun():
#     global name
#     name = input("请输入您的姓名")
#     num = 0
#     while True:
#         print("输入1查询余额")
#         print("输入2存款")
#         print("输入3取款")
#         num = int(input())
#         if num == 1:
#             check_balance()
#         elif num == 2:
#             deposit()
#         elif num == 3:
#             withdraw_money()
#         else:
#             break
#
# ATM_fun()


# name_list1 = [['lk','zy'],[666],True]
# # print(name_list1)
# # print(type(name_list1))
#
# print(name_list1[0][0])


# my_list = [['lk','zy'],[666],True,'itheima']
# my_list[0] = 'hello' # 可以直接修改列表元素
# print(my_list)

# mylist = ['itcast','itcast','itheima','python',['lk','zy']]
# my_len = len(mylist)
# print(my_len)

# ages = [21,25,21,23,22,20] #1
# ages.append(31)            #2
# ages.extend([29,33,30])    #3
# ages.pop(0)                #4
# del ages[-1]               #5
# index = ages.index(31)     #6
# print(index)
# print(ages)


# index = 0
# ages = [21,25,21,23,22,20]
# # while index < len(ages):
# #     ages[index] += 1
# #     index += 1
#
# # 注意这两种x值的区别
# for x in range(len(ages)):
#     print(x)
#
# for x in ages:
#     x +=1
#     print(x)
# print(ages)

# t1 = (1)
# t4 = ('hello')
# print(type(t4))
# print(type(t1))

# t1 = (['1'],[2],('hello'))
# print(type(t1))

# index = t2.index('itheima')
# count = t2.count('黑马程序员')
# my_len = len(t2)
# print(count)
# print(index)
# print(my_len)

# t2 = ('itheima','船只教育','黑马程序员','黑马程序员')
# index = 0
# while   index < len(t2):
#    print(t2[index])
#    index +=1
#
# for element in t2:
#     print(element)


# t2[0] = '1'
# print(t2)

# t3 = (1,'lk',['hello','zy'],('a','b'))
# print(t3)
# # 修改元组中列表元素内的内容
# t3[2][0] = 'j'
# t3[2][1] = 'k'
# print(t3)

# str1 = "itheima"
# print(str1[1])
# str[2] = '12'

# my_str = "lkzytxhtys"
# newstr = my_str.replace("zy","LwY")
# print(my_str)   # lkzytxhtys
# print(newstr)   # lkLwYtxhtys

# my_str = "lk zy txh tys"
# newstr = my_str.split(" ") # 这里以空格切分，会返回切分猴的列表
# print(newstr)

# my_str = "  lk zy txh tys  "
# newstr1 = my_str.strip()  # 去除空格
# print(newstr1)
#
# newstr2 = newstr1.strip('ys')  # 去除newstr1最后的s字符
# print(newstr2)

# my_str = "lk zy txh tys lk"
# count = my_str.count("t")
# mylen = len(my_str)
# index = my_str.index("k")   # 查目标的下标
# print(count)
# print(mylen)
# print(index)

# mystr = "itheima itcast boxuegu"
# count = mystr.count("it")
# newstr1 = mystr.replace(" ","|")
# newstr2 = newstr1.split("|")
# print(count)
# print(newstr1)
# print(newstr2)

# # 对mylist进行切片，从1开始，4结束，步长1
# mylist = [0,1,2,3,4,5,6]
# result1 = mylist[1:4]  # 默认是1步长
# print(result1)
#
# # 对mytuple进行切片，从头开始，到结束，步长1
# mytuple = (0,1,2,3,4,5,6)
# result2 = mytuple[:]   # 起始和结束留空表示从头到尾切片
# print(result2)
#
# # 对mystr进行切片，从头开始，到尾结束，步长2
# mystr = "0123456"
# result3 = mystr[::2]
# print(result3)

# # 对mylist进行切片，从3开始，1结束，步长-1
# mylist = [0,1,2,3,4,5,6]
# result1 = mylist[3:1:-1]  # 默认是1步长
# print(result1)
#
# # 对mytuple进行切片，从头开始，到尾结束，步长-2
# mytuple = (0,1,2,3,4,5,6)
# result2 = mytuple[::-2]   # 起始和结束留空表示从头到尾切片
# print(result2)
#
# # 对mystr进行切片，从头开始，到尾结束，步长-1(将字符串反转)
# mystr = "0123456"
# result3 = mystr[::-1]
# print(result3)

# my_str = "万过薪月,员序程马黑来,nohtyP学"
# newstr = my_str[::-1] # 先反转
# newstr1 = newstr.split(",") # 分割出字符串列表
# newstr2 = newstr1[1][1:] # 取出小序列
# print(newstr2)

# myset = {"itheima","lk","zy","txh","lk"}
# myset.add("python") # 在myset添加python
# myset.remove("itheima") # 移除itheima字符串
# pop = myset.pop()      # 在myset中随机取出
# print(myset)
# print(pop)
# myset.clear()       # 清空集合


# myset1 = {"lk","zy","txh","lk"}
# myset2 = {"tys","ly","lk"}
# myset3 = myset1.difference(myset2) # 取差集，myset1中有而myset2没有的
# print(myset3)


# myset1 = {"lk","zy","txh","lk"}
# myset2 = {"tys","ly","lk"}
# myset3 = myset1.difference_update(myset2)
# print(myset1) # 取差集，myset1中有而myset2没有的，并且消除myset1中的相同的元素


# myset2 = {"tys","ly","lk"}
# myset3 = myset1.union(myset2)
# print(myset3)


# myset1 = {"lk","zy","txh","lk"}
# print(len(myset1))  # 算出集合中的元素个数，不包含重复的


# set1 = {1,2,3,4,5}
# for element in set1:
#     print(element)

# my_list = ['黑马程序员',"传智博客",'黑马程序员',"传智博客","itheima","itcast","itheima"]
# myset = set()
# for element in my_list:
#     myset.add(element)
# print(myset)



# 定义字典
# mydict = {"lk":99,"zy":97,"tys":90}
# score = mydict["lk"]
# print(score)

# mydict = {(1,2):1,98:["lk","zy"],2:"lk",
#           "姓名":{
#               "语文":97,
#               "数学":98
#                 }}
# print(mydict)


# mydict = {
#     "lk":{
#         "语文":98,
#         "数学":96
#     },"zy":{
#         "语文": 44,
#         "数学": 100
#     },"ly":{
#         "语文": 49,
#         "数学": 120
#     }
# }
# # 通过索引找出目标value
# score = mydict['ly']["语文"] # 找出ly的语文成绩是49
# print(score)

# mydict = {
#     "lk":{
#         "语文":98,
#         "数学":96
#     },"zy":{
#         "语文": 44,
#         "数学": 100
#     },"ly":{
#         "语文": 49,
#         "数学": 120
#     }
# }



# # 新增字典中没有的元素
# mydict["tys"] = {"语文":99,"数学":87}
#
# # 更新元素
# mydict["zy"] = {"语文":93,"数学":90}
#
# # 获取全部的key
# keys = mydict.keys()
# print(keys)
#
# # 遍历字典，其中key是字典元素的字符串，再通过字典的字符串索引遍历对应的value
# for key in keys:
#     print(key)
#     print(mydict[key])
#
# # 简单遍历，可以直接对字典进行for循环，第一次循环是直接得到key
# for key in mydict:
#     print(key)
#     print(mydict[key])
#
# # 统计字典的元素数量
# num = len(mydict)
# print(num)
#
# # 删除元素
# mydict.pop("ly")
#
# # 清空元素
# mydict.clear()
#
# print(mydict)



# 升职加薪案例
# 所有级别为1的员工，级别加1，薪水加1000，
# company_dict = {
#     "王力宏":{
#         "部门":"科技部",
#         "工资":3000,
#         "级别":1
#     },    "周杰伦":{
#         "部门":"市场部",
#         "工资":5000,
#         "级别":2
#     },    "林俊杰":{
#         "部门":"市场部",
#         "工资":7000,
#         "级别":3
#     },    "张学友":{
#         "部门":"科技部",
#         "工资":4000,
#         "级别":1
#     },    "刘德华":{
#         "部门":"市场部",
#         "工资":6000,
#         "级别":2
#     },
# }
#
# # for循环遍历字典
# for key in company_dict:
#     # 找出级别为1的员工
#     if  company_dict[key]['级别'] == 1:
#         company_dict[key]['级别'] += 1
#         company_dict[key]['工资'] += 1000
#         company_dict[key]['坤'] = 20 # 小黑子
#
# for key in company_dict:
#     print(company_dict[key])
"""
{'部门': '科技部', '工资': 4000, '级别': 2, '坤': 20}
{'部门': '市场部', '工资': 5000, '级别': 2}
{'部门': '市场部', '工资': 7000, '级别': 3}
{'部门': '科技部', '工资': 5000, '级别': 2, '坤': 20}
{'部门': '市场部', '工资': 6000, '级别': 2}
"""

# my_tuple = ('a','c','g','b','d','e')
# result = sorted(my_tuple,reverse=True)
# print(result)


# def test_fun():
#     return   1,"lk",{'a'},["zy",2],("12")
#
# x,y,z,u,o = test_fun()
# print(x)
# print(y)
# print(z)
# print(u)
# print(o)

# def fun(name = "lk",age=11,gender):
#     print(f"你的名字是{name}，今年{age}岁，性别{gender}")
#
# fun(name="lk",gender = "女")

# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入(通常使用*args来表示不定长参数)
# def test_fun(*args):
#     print(f"args的类型是{type(args)}，内容是{args}")
#
# test_fun(1,2,"da",{"qwe"},{"key":"value"})


# def test_fun(**kwargs):
#     print(f"args的类型是{type(kwargs)}，内容是{kwargs}")
#
# test_fun(name = "lk",age = 18, gender = "男")
#
# def fun():
#     print("1")
#     return 1
#
# print(type(fun()))

# def test_fun(coumpute):
#     result = coumpute(1,2)
#     return  result
#
# def test_coumpute(x,y):
#     return  x + y
#
# print(test_fun(test_coumpute)) # 函数test_coumpute作为参数传递到test_fun函数中


# def test_fun(coumpute):
#     result = coumpute(1,2)
#     return  result
#
# # lambda将匿名函数功能返回给test_fun函数，让coumpute函数形参得到改匿名函数的功能
# print(test_fun(lambda x,y: x+y)) # lambda匿名函数不用写return直接返回


# f = open("D:/test/test.txt","r",encoding="UTF-8")  # 因为encoding不是第三个参数，所以不能用位置参数
# # 其中的f只是文件对象
# print(f.read(10))
# print(f.read(12))  # 如果同时对一个文件两次read，会接着上次第一次read的内容往后读取
# print(f.read(12))


# f = open("D:/test/test.txt","r",encoding="UTF-8")  # 因为encoding不是第三个参数，所以不能用位置参数
# print(f.read())
# print(f.readlines())  # readlines读取文件所有行
# print(f.readline())
# print(f.readline())


# f = open("D:/test/test.txt","r",encoding="UTF-8")  # 因为encoding不是第三个参数，所以不能用位置参数
# for line in f:
#     print(f"读取文件的每一行：{line}")
#
# # 文件关闭
# f.close()
#
# # 让程序睡眠一段时间（让程序持续执行一段时间）
# time.sleep(500)


# with open() 语法操作，with open在读取文件后会自动关闭文件，不需要使用close关闭
# with open("D:/test/test.txt","r",encoding="UTF-8") as f:
#     print(f.read(2))
#
# time.sleep(200000)

# 1、使用read，字符串匹配统计算法直接统计出itheima的数量
# f = open("D:/test/work.txt","r",encoding="UTF-8")
# txt = f.read()
# count = txt.count("itheima")
# print(count)

# 2、一行一行读取，需要先去除每一行的回车符号，再按空格切分成列表，最后叠itheima的数量
# count = 0
# with open("D:/test/work.txt","r",encoding="UTF-8") as f:
#     for line in f:
#         txtList = line.strip("\n").split(" ")
#         print(txtList)
#         count +=txtList.count("itheima")
# print(count)

# f = open("D:/test/write.txt","w",encoding="UTF-8")
# f.write("hello") # 并没有真正的写入磁盘，而是暂时写在python的内存
# f.flush()  # 将内存中积累的数据存到硬盘
#
# f2 = open("D:/test/dy.txt","w",encoding="UTF-8")
# f2.write("yyyy-m-d")
#
# time.sleep(10)

# f3 = open("D:/test/dy.txt","a",encoding="UTF-8")
# f3.write("\n111")    # 对文件进行追加内容，不会覆盖之前内容
# f3.flush()
# time.sleep(20)


# 将bill.txt文件的内容复制到bill.txt.bak中，并将测试人员去除
# f_bak = open("D:/test/bill.txt.bak","a",encoding="UTF-8")
# f = open("D:/test/bill.txt","r",encoding="UTF-8")
# for line in f:
#     tap = line.strip("\n").split(",")[-1]  # 每行去除回车字符串再以逗号分割成列表，最后取出想要数据
#     # print(tap)
#     if tap != "测试":
#         f_bak.write(line)
# f_bak.close()
# f.close()
# f_bak = open("D:/test/bill.txt.bak","r",encoding="UTF-8")
# print(f_bak.read())

# try:
#     f = open("D:/test/yuas.txt","r",encoding="UTF-8")
# except:
#     print("文件不存在，换一种方式打开")
#     f = open("D:/test/yuas.txt","w",encoding="UTF-8")



# try:
#     print("hello")
#     # print(name)
#     # 1/0
#     # open("D:/test/yu完全as.txt", "r", encoding="UTF-8")
# except Exception as e:      # 或者写成except:
#     print("捕获全部异常")
# else:                       # 没有异常时执行代码
#     print("没有异常")



# try:
#     print("hello")
#     print(name)
#     open("D:/test/yu完全as.txt", "r", encoding="UTF-8")
#     1/0
# except Exception as e:
#     print("捕获全部异常")
# else:
#     print("没有异常")
# finally:                    # 在这里执行必须要执行的代码，如关闭文件等等
#     print("有没有异常都执行")


# import time  # 引入time模块（全部引入）
# time.sleep(2)    # 使用模块的类，函数，变量
#
# # 局部引用，只能使用指定的功能
# from time import sleep
# sleep(10)
# print("我出来了")

# from time import *        # *表示将所有功能引用，并且可以不用写time
# sleep(5)
# print("你好")

# import time as t  # 给time模块改别名t
# t.sleep(3)
# print("hello")

# from time import sleep as s   # 将sleep改别名s
# s(2)
# print("1")


# 从module_test引入两个函数
# from test_package.module_test import *
# num = add(1,2)
# num2 = chengfa(2,3)
# print(num)
# print(num2)
# test(3,2)


# # 引入包内的模块(多个模块可以用元组包裹)
# from test_package import (module_test,my_module)
# module_test.chengfa(2,3)
# my_module.info_print()
#
# # 引入包内模块的所有功能
# from test_package.module_test import *
# add(1,2)
#
# # 引入包内的所有模块
# from  test_package import *
# module_test.add(2,3)
# my_module.info_print()
#
# # 引入包内模块的具体功能(函数)
# from test_package.module_test import (test,chengfa)
# test(2,3)
# chengfa(2,3)


# __init__ = ['module_test']
# from  test_package import *
# module_test.add(2,3)
# my_module.info_print()

# 测试自制工具包作用
# from my_utils import *
# newstr = str_util.str_reverse(123123)
# print(newstr)
# newstr1 = str_util.substr(1234567,2,5)
# print(newstr1)
#
# file_util.appen_to_file("d:/test/hello.txt",5201314)
# # hello.txt内文件原内容是“hello world我草泥马”
# file_util.print_file_info("d:/test/hello.txt")

import json
data = [{"name":"刘凯","age":19},{"name":"只有","age":12}]
newDum = json.dumps(data,ensure_ascii=False)  # ensure_ascii=False显示中文代码
print(newDum)
print(type(newDum))  # 将字典转化为JSON格式
l = json.loads(newDum)   # JSON格式转换回去
print(type(l))