# 为多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)

# 交换两个变量
x, y = y, x
print(x, y, z)

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print('key: ' + key + '\nvalue: ' + value)

# 链式赋值
# x = y = somefunction()
# y = somefunction() x =y

# 增量赋值
x = 2
x += 1
x *= 2
print(x)
