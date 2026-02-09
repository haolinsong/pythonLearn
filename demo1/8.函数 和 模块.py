"""判断三条边的长度能否构成三角形"""
def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b
print(make_judgement(1,2,3))
print(make_judgement(c=6, b=4, a=5))  # True  使用关键词参数可以不按顺序

# 参数的默认值
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c

# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6
# 注意的是，带默认值的参数必须放在不带默认值的参数之后，否则将产生SyntaxError错误，

# /前面的参数是强制位置参数：调用函数时只能按照参数位置来接收参数值的参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
# print(make_judgement(b=2, c=3, a=1))

# *后面的参数是命名关键字参数： 只能通过“参数名=参数值”的方式来传递和接收参数
def make_judgement1(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement1(1, 2, 3))




# 可变参数
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total

# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45

# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)

# 模块
# import module1
# import module2
#
# import module1 as m1
# import module2 as m2
#
# from module1 import foo
# from module2 import foo
#
# from module1 import foo as f1
# from module2 import foo as f2