xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方'
}
print(xinhua)

# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '123456'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'} 舍弃了6
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

#字典的运算
person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 成员运算
print('name' in person)  # True
print('tel' in person)   # False

# 索引运算
print(person['name'])
person['age'] = 25
print(person)

# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')

# 字典的方法
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.get('name'))       # 王大锤
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())  # dict_values(['王大锤', 25, 178])
print(person.items())   # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
for key, value in person.items():
    print(f'{key}:\t{value}')
print(person.pop('name')) # 如果指定的键不存在， 报错KeyError错误
print(person.popitem())  # 删除最后一个
person.clear()  #清空

