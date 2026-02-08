# 如果字符串本身包含了'、"、\这些特殊的字符，必须要通过\进行转义处理
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1)  # 'hello, world!'
print(s2)  # \hello, world!\

# 原始字符串：以r或R开头的字符串， 不存在转义字符一说
s1 = '\it \is \time \to \read \now'
s1 = r'\it \is \time \to \read \now'
print(s1)  #\t是制表符（table），\n是换行符（new line），\r是回车符（carriage return）
print(s2)

# 拼接和重复
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!

# 成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('wo' not in s2)  # False
print(s2 in s1)        # False

# 索引和切片
s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba

# 大小写： 由于字符串是不可变类型，使用字符串的方法对字符串进行操作会产生新的字符串，但是原来变量的值并没有发生变化
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE

# 查找操作
s = 'hello, world!'
print(s.find('or'))      # 8
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 8
print(s.index('or', 9))  # ValueError: substring not found
# 说明：find方法找不到指定的字符串会返回-1，index方法找不到指定的字符串会引发ValueError错误。

# 性质判断
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False  是不是完全由数字构成的
print(s2.isalpha())  # False  是不是完全由字母构成的
print(s2.isalnum())  # True   不是由字母和数字构成的

# 格式化字符串
a = 321
b = 123
print(f'{a} * {b} = {a * b}')

# 修剪操作
s1 = '   jackfrued@126.com  '
print(s1.strip())      # jackfrued@126.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  # 你好，世界~
print(s2.rstrip('~'))  # ~你好，世界

# 替换操作： 第三个参数是指定替换的次数
s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))  # hell@, good world

# 拆分与合并
s = 'I love you'
words = s.split()
print(words)            # ['I', 'love', 'you']
print('~'.join(words))  # I~love~you

s = 'I#love#you#so#much'
words = s.split('#')  #指定其他字符串拆分
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)  # 指定最大拆分次数
print(words)  # ['I', 'love', 'you#so#much']