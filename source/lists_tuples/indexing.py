"""
序列
"""

# 字符串就是由字符组成的序列
greeting = 'Hello'
print('索引0第一个元素：' + greeting[0])
print('索引-1最后一个元素：' + greeting[-1])

# 成员资格
# 检测一个值是否在序列中，可以使用 in 运算符。
permissions = 'rw'
print('w in permissions: ' + str('w' in permissions))
print('x in permissions: ' + str('x' in permissions))

user = ['mlh', 'foo', 'bar']
print('mlh in user: ' + str('mlh' in user))

# 长度 最大值 最小值
numbers = [100, 34, 678]
print('len(numbers): ' + str(len(numbers)))
print('max(numbers): ' + str(max(numbers)))
print('min(numbers): ' + str(min(numbers)))
print('max(2, 3): ' + str(max(2, 3)))
print('min(9, 3, 2, 5): ' + str(min(9, 3, 2, 5)))


# list 函数
print("list('Hello'): " + str(list('Hello')))

# 元素赋值  不能为不存在的元素赋值
x = [1, 1, 1]
x[1] = 2
print(str(x))

# 元素删除
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print('del names[2]: ' + str(names))

# 分片赋值
name = list('Perl')
name[2:] = list('ar')
print(str(name))

# 不替换原有元素的情况下插入新的元素
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print('numbers: ' + str(numbers))

# 使用分片来删除元素
numbers[1:4] = []
print('numbers: ' + str(numbers))

# 方法
# append 在列表末尾追加新元素
lst = [1, 2, 3]
lst.append(4)
print('lst: ' + str(lst))
# count 统计某元素在列表中出现的次数
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print('x.count(1): ' + str(x.count(1)))
print('x.count([1, 2]): ' + str(x.count([1, 2])))
# extend  在列表的末尾一次性追加另一个序列中的多个值
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print('a: ' + str(a))
# index 从列表中找出某个值第一个匹配项的索引位置
knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print("knights.index('who'): " + str(knights.index('who')))
# insert 将对象插入到列表中
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print('numbers: ' + str(numbers))
# pop 移除列表中的一个元素(默认最后一个)，并且返回该元素的值
x = [1, 2, 3]
x.pop()
print('x:' + str(x))
# remove 移除列表中某个值的第一个匹配项
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print('x: ' + str(x))
# reverse 将列表中的元素反向存放
x = [1, 2, 3]
x.reverse()
print('x: ' + str(x))
# sort 对列表进行排序
x = [4, 6, 2, 1, 7, 9]
x.sort()
print('x: ' + str(x))
# 反向排序
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print('x: ' + str(x))


# 元组
x = 1, 2, 3
print('x:' + str(x))
# tuple 将一个序列作为参数并把它转换为元组
print('tuple([1, 2, 3]): ' + str(tuple([1, 2, 3])))



