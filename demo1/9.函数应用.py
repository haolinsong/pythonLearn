#标注参数类型 & 返回值类型
def gcd(x: int, y: int) -> int:
    """求最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x

# sorted函数
old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
new_strings = sorted(old_strings)
new_strings = sorted(old_strings, key=len)  # 按长度排序

# 自定义二元运算
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5, key=2))  # 17

# filter可以实现对序列中元素的过滤
# map可以实现对序列中元素的映射
# 去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表
def is_even(num):
    """判断num是不是偶数"""
    return num % 2 == 0
def square(num):
    """求平方"""
    return num ** 2
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(square, filter(is_even, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

#如上代码可以使用列表生成式
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = [num ** 2 for num in old_nums if num % 2 == 0]
print(new_nums)  # [144, 64, 3600, 2704]

#上述代码用lambda实现
old_nums = [35, 12, 8, 99, 60, 52]
new_nums = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(new_nums)  # [144, 64, 3600, 2704]

# reduce 函数实现规约：第一个参数是代表运算的函数，第二个参数是运算的数据，第三个参数是运算的初始值
import functools
import operator
# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)
# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(1))        # 1
print(is_prime(37))  # True

print(*range(2,2))
