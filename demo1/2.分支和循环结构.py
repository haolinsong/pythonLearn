# if分支
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)

# match-case 分支  Python 3.10 中增加
"""
status_code = int(input('响应状态码: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
"""


# for-in 循环
total = 0
for i in range(1, 101):
    total += i
print(total)

# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。

# while循环
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# break和continue
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

# 嵌套的循环结构
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}x{j}={i * j}', end='\t')
    print()