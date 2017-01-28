# 导入模块
from math import floor
from math import sqrt
import cmath

# 导入模块
# 加法
print('123 + 234 = ' + str(123 + 234))

# 减法
print('111 - 11 = ' + str(111 - 11))

# 除法
print('10 / 3 = ' + str(10 / 3))

# 向下取整
print('10 // 3 = ' + str(10 // 3))

print('1.0 / 2.0 = ' + str(1.0 / 2.0))
print('1.0 // 2.0 = ' + str(1.0 // 2.0))

# 取余
print('1 % 2 = ' + str(1 % 2))

# 幂运算
print('2^3 = ' + str(2 ** 3))

# 十六进制
print(0xAF)

# 八进制
print(0o20)

# 变量 赋值
x = 10
# 获取用户输入
# y = input('输入一个整数数字 y = ')
y = 11
print('10 * y = ' + str(x * int(y)))

# 函数
print('-100的绝对值：' + str(abs(-100)))
print('3.0 / 2.0 浮点数四舍五入：' + str(round(3.0 / 2.0)))
print('2^3 = pow(2, 3)：' + str(pow(2, 3)))
print('1.8向下取整：' + str(floor(1.8)))
print('4的平方根：' + str(sqrt(4)))
print('-1的平方根：' + str(cmath.sqrt(-1)))

# 字符串前加上 r ，不转义
print('转义，hello, \nworld')
print(r'原始字符串，hello, \nworld')
