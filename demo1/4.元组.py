# 元组也是多个元素按照一定顺序构成的序列。元组和列表的不同之处在于，元组是不可变类型
# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('浩霖', 30, True, '河南永城')

# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3

# 索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 河南永城

# 切片运算
print(t2[:2])   # ('浩霖', 30)
print(t2[::3])  # ('浩霖', '河南永城')

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '浩霖', 30, True, '河南永城')

# 比较运算
print(t1 == t3)            # False

# 打包和解包
# 多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；
# 把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100

# 当变量数量小于元素个数时时，可以使用星号表达式
# 注意： 用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；在解包语法中，星号表达式只能出现一次。
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000

i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []

# 解包语法对所有的序列都成立
a, b, *c = range(1, 10)
print(a, b, c) #1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)  #h ['e', 'l', 'l'] o

# 列表和元组的转换
infos = ('浩霖', 30, True, '西安')
# 将元组转换成列表
print(list(infos))

frts = ['apple', 'banana', 'orange']
# 将列表转换成元组
print(tuple(frts))

import timeit
print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))