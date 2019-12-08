print("计算a到n之内的所有整数的和")

a = input("请输入第一个数：")

n = input("请输入第二个数：")

a = int(a)
n = int(n)

S = (a + n) * (n - a + 1) / 2;

print("求得的和为：",S)


d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
print(d['Michael'])

key = [1, 2, 3]

s = set([1, 2, 3])
print(s)
     
s.add(5)
print(s)

print(max(1,6,9,11))  # 求最大值

print(abs(-199))  #abs 绝对值

#函数

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-9))


def nop():  #空函数
    pass


import math   #导入函数

def move(x, y, step, angle = 0):

    nx = x + step * math.cos(angle)

    ny = y - step * math.sin(angle)

    return nx, ny               #可以返回多个值！  也可以不写，，默认返回零

r = move(100, 60, 60)
print(r)


#定义一个函数，接受三个参数，返回一元二次方程的两个解
print("解一元二次方程组")
import math

def quadratic(a, b, c):

    delat = b * b - 4 * a * c;

    if delat > 0:

        x1 = (- b + math.sqrt(delat)) / (2 * a)
        x2 = (- b - math.sqrt(delat)) / (2 * a)

        return x1, x2

    elif delat == 0:
        
        x1 = x2 = (-b) / (2 * a)
        
        return x1

    else:
        return ("无解")

a = input("请输入a:")
b = input("请输入b:")
c = input('请输入c:')

a = int(a)
b = int(b) 
c = int(c)

print(quadratic(a, b, c))


print("计算一个数n次方")
#计算一个数的n次方
def power(x, n):

    s = 1

    while n > 0:

        n = n - 1

        s = s * x

    return s

print(power(2,10))



def calc(*numbers):

    sum = 0

    for n in numbers:

        sum = sum + n * n

    return sum




# 列表生成式

l = list(range(1,11))

for i in l:

    print(i)

L1  = []

for x in range(1,11):

    L1.append(x * x)

print(L1)



L2 = [x * x for x in range(1,11)]

print(L2)

L3 = [x * x for x in range(1,11) if x % 2 == 0]

print(L3)

L4 = [m + n for m in 'ABC' for n in 'XYZ']   #双重循环，形成全排列

print(L4)



d = {'x':'A', 'Y' : 'B', 'Z' : 'C'}   #字典

for k, v in d.items():     #for循环使用两个变量

    print(k, '=', v)

L5 = [k + '=' + v for k, v in d.items()]

print(L5)



L = ['Hello', 'World', 'IBM', 'Apple']

m = [s.lower() for s in L]     #把list（L）中的字符串变成小写

print(m)


#生成器(generator)     配next

L = [x * x for x in range(1, 11)]

print(L)

g = (x * x for x in range(1, 11))    #把列表生成式中的[]改为(),就创建了一个generator


for n in g:

    print(n)


print(abs(-10))

f = abs       #变量指向函数，可以通过变量来调用这个函数
              #abs 其实就是一个指向函数的变量  即函数名就是一个变量
print(f(-10))


# 高阶函数(函数作为参数传入）

def add(x, y, f):

    return f(x) + f(y)

x = -5

y = 6

f = abs

print(add(-5, 6, f))




#filter 函数(可以对列表进行处理）  与列表在一起使用

def is_odd(n):

    return n %2

L = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 9, 10, 15]))   #从列表里刷选出偶数

print(L)

def not_empty(s):

    return s and s.strip()

L=list(filter(not_empty, ['A', '', 'B', None, 'C', ' ']))   #去掉列表里的空字符

print(L)



# 用filter求素数(1 到 1000 内的素数）  

def _odd_iter():

    n = 1

    while True:                      

        n = n + 2

        yield n      #生成器   类似于return   迭代一次遇到yield时就返回yield后面的值    使用yield时，对应的函数就是一个生成器
                    
                     #这是一个无线序列

def _not_divisible(n):            #筛选函数

    return lambda x: x % n > 0       #lambda 匿名函数  主体是一个表达式   起函数速写的作用

def primes():

    yield 2

    it = _odd_iter()  #初始序列

    while True:

        n = next(it)

        yield n

        it = filter(_not_divisible(n), it)  #构造新序列

for n in primes():

    if n < 1000:

        print(n)

    else:

        break


# 排序算法  Sorted

print(sorted([36, 5, -12, 9, -21]))    #从小到大

L = ['bob', 'about', 'Zoo', 'Credit']

L1 = sorted(L, key = str.lower)

print(L1)

L2 = sorted(L, key = str.lower, reverse = True)

print(L2)


# 匿名函数
# 不用写返回值， 与map函数配

m = list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))     #map 函数  迭代对象上映射函数

print(m)




n = int ('12345')

print(n)

# int()  函数提供额外的base函数  int(x, base = N)  可以做N进制的转换  把N进制转换成10进制

m = int ('12345', base = 16)

print(m)

# 二进制转换

def int2 (x, base = 2):

    return int (x, base)

print(int2('10000'))


# 模块   （一个 .py 文件就称为一个模块（Module））

# 一个abc.py 的文件就是一个名字叫abc的模块


# 作用域

#def _private_1(name):

#    return 'Hello, %s' % name

#def _private_2(name):

#    return 'Hi, %s' % name

#def greeting(name):

#    if len(name) > 1:

#        return _private_1(name)

#    else:

#        return _private_2(name)




# 面向对象  &  面向过程

std1 = {'name' : 'Michael', 'score' : 98}

std2 = {'name' : 'Bob', 'score' : 81}


# 打印学生的成绩


def print_score(std):                                                   #面向过程

    print('%s : %s' % (std['name'], std['score']))

print_score(std1)

print_score(std2)


class Student(object):                                                  #面向对象
                                                                        # class 类

    def _init_(self, name, score):

        self.name = name                                                #面向对象三大特点： 数据封装  继承  多态

        self.score = score


    def print_score(self):

        print('%s %s' % (self.name, self.score))

print_score(std1)

print_score(std2)



# 类对象

class Turtle:

    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    def run(self):
        print("跑！")

    def climb(self):
        print('爬！')

    def bite(self):
        print('咬！')

    def sleep(self):
        print('睡觉！')

tt = Turtle()
print(tt.climb())