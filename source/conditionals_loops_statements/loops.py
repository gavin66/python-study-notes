# while 循环
x = 1
while x <= 100:
    print(x)
    x += 1

# for 循环
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

for number in range(1, 101):
    print(number)

# 循环遍历字典元素
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
# 使用序列解包
for key, value in d.items():
    print(key, 'corresponds to', value)

# 迭代工具
# 并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

# 跳出循环
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break

# 循环中的else 没有break跳出才执行else
from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it!")

# 列表推导式
print([x*x for x in range(10)])
# 增加if语句
print([x*x for x in range(10) if x % 3 == 0])
# 增加更多for循环
print([(x, y) for x in range(3) for y in range(3)])


# pass 语法  不进行任何操作
# 下面如果不加入pass语句就会报错
name = 'Enid'
if name == 'Ralph Auldus Melish':
    print('Welcome!')
elif name == 'Enid':
    # Not finished yet...
    pass
elif name == 'Bill Gates':
    print('Access Denied')

# del 删除
x = 1
del x

# exec 使字符串作为代码执行
exec("print('Hello, world!')")

# 与 exec 类似，它会计算python表达式，并且返回结果值
print(eval(input("Enter an arithmetic expression: ")))