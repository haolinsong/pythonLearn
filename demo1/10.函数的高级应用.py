import time
import random

# 装饰器：record_time函数最终会返回这个带有装饰功能的函数wrapper并通过它替代原函数func，
# 当原函数func被record_time函数装饰后，我们调用它时其实调用的是wrapper函数，所以才获得了额外的能力。
# wrapper函数的参数比较特殊，由于我们要用wrapper替代原函数func，但是我们又不清楚原函数func会接受哪些参数，
# 所以我们就通过可变参数和关键字参数照单全收，然后在调用func的时候，原封不动的全部给它。
# 这里还要强调一下，Python 语言支持函数的嵌套定义，
def record_time(func):
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return result

    return wrapper

def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')
download1 = record_time(download)
download1('MySQL从删库到跑路.avi')


#如下是装饰器函数语法糖 ： 用@装饰器函数将装饰器函数直接放在被装饰的函数上
def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

download('MySQL从删库到跑路.avi')

# 递归调用
def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)

# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
print(fac(5))    # 120