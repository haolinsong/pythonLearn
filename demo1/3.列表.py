# 列表中可以有重复元素，列表中可以有不同类型的元素
a = list("abc") # ['a', 'b', 'c']
print(a)

# 列表的运算
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]

print(99 in items6)  # False
print('C++' not in items7)     # True

# 获取元素
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
# 有效的反向索引是-1到-5
print(items8[-5])  # 'apple'

# 切片     开始，终止（不包含），跨度
print(items8[0:3:2])  #['apple', 'pitaya']
items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']

# 对列表进行循环
languages = ['Python', 'Java', 'C++', 'Kotlin']
# 方式一：对索引进行循环
for index in range(len(languages)):
    print(languages[index])

#方式2:直接对列表进行循环
for language in languages:
    print(language)



# 列表方法
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')  #末尾追加
languages.insert(1, 'SQL')  # 插入
languages.remove(languages[0])  #删除列表中的制定元素
languages.pop()  # 默认删除最后一个元素，也可以指定元素，可以有返回值
languages.clear() #清空元素

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
items.sort()  # 排序
items.reverse()  #反转


# 列表生成式
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
    if num > 50:
        nums2.append(num)
print(nums2)
# 可用如下列表生成式代替
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)