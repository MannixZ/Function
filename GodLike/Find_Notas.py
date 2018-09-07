import re

def find_notas(test):
    pattern = re.compile(r"#+.*")
    result = pattern.findall(test)
    if type(result) == list :
        print("匹配成功\n" + "注释内容为：%s" %str(result))
    else:
        print("匹配失败")

def remove_nota(test):
    result = re.sub(r"#+.*", "", test)
    return result

if __name__ == "__main__":
    test = input()
    print("去除注释后：%s" %remove_nota(test))
