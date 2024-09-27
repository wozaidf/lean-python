# 打印文件内容函数
def print_file_info(file_name):
    try:
        f = open(file_name, "r", encoding="UTF-8")
    except Exception as e:
        print(f"文件不存在{e}")
    else:
        print(f.read())
    finally:
        if f:              # 如果上诉文件不存在就会导致f不存在，所有要用if判断一下
            f.close()

# 追加信息到文件的函数
def appen_to_file(file_name,data):
    try:
        f = open(file_name, "a", encoding="UTF-8")
    except Exception as e:
        print(f"文件不存在{e}")
    else:
        f.write(str(data))
    finally:
        if f:
            f.close()
