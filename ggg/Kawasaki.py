#写入 w (清空写入) a （文件末尾追加内容） b
#encoding="utf-8" 解决文件内写入中文时乱码问题
#f = open("D:\\softwaredata\\gy-motuoche666\\moto.txt","w",encoding="utf-8")
#写入内容 参数为字符串类型
#f.write("kawasaki")
#写入内容，参数为list类型
#f.writelines(["123\n","456\n","789\n"])
#f.close()

#读取内容 r 读取模式
#encoding="utf-8" 解决读取文件内容时，中文乱码问题
#f = open ("moto.txt",'r',encoding="utf-8")
#c = f.read()
#print(c)
#f.close()

#读取内容 r 读取模式
#encoding="utf-8" 解决读取文件内容时，中文乱码问题
#f = open ("moto.txt","r",encoding="utf-8")
#读取文件全部内容
'''c = f.read()
print(c)
按行读取文件全部内容
lines = f.readlines()
print(lines)
一次性读取一行内容
line = f.readline()
print(line)
f.close()

# with 是一个上下文管理器,with内的代码块在执行结束或者是执行出错的时候，
# 都会自动执行释放系统资源的操作。
with open ("moto.txt",'r',encoding="utf-8")as f:
    c = f.read()
    print(c)

#类 相当于一个模板，没有实体
class ClassA1():
    a1=10
    def print_a(self):
        print(self.a1)
# 类的实例化
c = ClassA1()
c.print_a()
#项目->包(packae)->模块（module）->类（class）->方法（function）、变量（attribute）

#把kawasaki的代码导入到当前模块
from venv.kawasaki import Product （* 所有）

#产品 手机
class Product():
    size="6寸"
    def __init__(self,color):

        self.color=color
    def call(self):
        print("hello")
    def send_message(self):
        print("你有一个快递！")
#实例化
phone1=Product("土豪金")
#获取属性
print(phone1.color)
print(phone1.size)
#调用方法
phone1.call()
'''
import json

#json转字典
#j = '''
#{"name":"小明",
#"sex":"不详"
#}
#'''
#d =json.loads(j)
#d["sex"]="男"
#print(d)
# 字典转json
#j = json.dumps(d,ensure_ascii=False)
#print(j)

#import random

#获取随机数字
#a = random.randint(10,50)
#3print(a)

#有序的可迭代对象 str list tuple
#c=random.choice([1,2,3,4,5,6,7,8,9])
#print(c)


import os

# 获取文件的绝对路径
#p = os.path.abspath("moto.txt")
#print(p)

# 获取文件夹路径
#d = os.path.dirname(p)
#print(d)

# 获取文件名
#f = os.path.basename(p)
#print(f)

# 连接文件和文件夹
#path = os.path.join(d,f)
#print(path)

# 创建文件夹
#os.mkdir("motoc")

import os

try:
    os.mkdir("gy_C")
except FileExistsError:
    print("文件已存在")
else:
    print("文件夹创建成功")
finally:
    print("创建文件夹结束")
print("sdfsdf")

import os

try:
    os.mkdir("gy_C")
except FileExistsError:
    print("文件已存在")
else:
    print("文件夹创建成功")
finally:
    print("创建文件夹结束")
print("sdfsdf")

