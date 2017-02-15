> 本项目为本人的 Python 自学笔记。根据《Python 基础教程（第二版 修订版）》所得总结。所使用的 Python 版本为 `3.5.1`



## 基础

### 安装 Python

### 交互式解释器

启动 Python 的时候，有如下提示：

![](res/python_console.png)

写下第一个程序（或者执行`$ python source/basics/hello.py `）：

```python
>>> print("Hello, world!")
Hello, world!
```

> 行尾不需添加分号，这点不同于其他语言。如果一行有更多语句，需分号，但不建议这样的编程习惯。



### 数字和表达式

`source/basics/basics.py `

```python
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
```



## 列表和元组

Python中有6种内建的序列，最常用的两种：列表和元组。其他还有字符串、Unicode字符串、buffer对象和xrange对象。

列表可修改，元组不可修改，这是它们的区别。

* 序列 - `source/lists_tuples/indexing.py `

* 序列示例 - `source/lists_tuples/indexing_example.py`

* 相加 - `source/lists_tuples/adding_sequences.py`

* 乘法 - `source/lists_tuples/multiplication_sequences.py`

* 乘法示例 - `source/lists_tuples/multiplication_sequences.py`

* 分片 - `source/lists_tuples/slicing.py`

  ​

## 使用字符串

所有标准的序列操作（索引、分片、乘法、判断成员资格、求长度、取最小值和最大值）对字符串同样适用。但是，字符串都是不可变的。因此，以下项或分片赋值都是不合法的。

```python
>>> website = 'http://www.python.org'
>>> website[-3:] = 'com'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in ?
    website[-3:] = 'com'
TypeError: object doesn't support slice assignment
```

* 字符串格式化：精简版 - `source/strings/formatting_short.py`

* 字符串格式化：完整版 - `source/strings/formatting_long.py`

* 字符串格式化示例 - `source/strings/formatting_example.py`

* 字符串方法 - `source/strings/string_methods.py`

  ​



##  字典

通过名字引用值的数据结构类型为映射。字典是Python唯一的内建的映射类型。

* 字典的使用 - `source/dictionaries/uses.py`

* 字典使用示例 - `source/dictionaries/example.py`

* 字典方法 - `source/dictionaries/methods.py`

  ​

## 条件、循环和其他语句



### 把某件事作为另一件事导入

```python
import somemodule
# 或者
from somemodule import somefunction
# 或者
from somemodule import somefunction, anotherfunction, yetanotherfunction
# 或者
from somemodule import *
```

只有确定自己想要从给定的模块导入所有功能时，才应该使用最后一个版本。但是如果两个模块都有`open`函数，那又该怎么办？只需使用第一种方式导入，然后像下面这样使用函数：

```python
module1.open(...)
module2.open(...)
```

但还有另外的选择：可以在语句末尾增加一个as字句，在该字句后给出名字，或为整个模块提供别名：

```python
>>> import math as foobar
>>> foobar.sqrt(4)
2.0
```

也可以为函数提供别名：

```python
>>> from math import sqrt as foobar
>>> foobar(4)
2.0
```

对于open函数，可以像下面这样使用：

```python
from module1 import open as open1
from module2 import open as open2
```



* 赋值魔法 - `source/conditionals_loops_statements/assignment_magic.py`
* 条件与条件语句 - `source/conditionals_loops_statements/conditions_statements.py`
*  比较运算符

|    表达式     |         描述          |
| :--------: | :-----------------: |
|   x == y   |       x 等于 y        |
|   x < y    |       x 小于 y        |
|   x > y    |       x 大于 y        |
|   x >= y   |      x 大于等于 y       |
|   x <= y   |      x 小于等于 y       |
|   x != y   |       x 不等于 y       |
|   x is y   |    x 和 y 是同一个对象     |
| x is not y |    x 和 y 是不同的对象     |
|   x in y   | x 是 y 容器（例如，序列）的成员  |
| x not in y | x 不是 y 容器（例如，序列）的成员 |

* 循环 - `source/conditionals_loops_statements/loops.py`



## 抽象

* 创建函数 - `source/abstraction/creating_functions.py`
* 参数魔法 - `source/abstraction/parameters_magic.py`
* 闭包 - `source/abstraction/closure.py`
* 递归 - `source/abstraction/recursion.py`



## 更加抽象

* 一个类实例 - `source/more_abstraction/Person.py`
* 类的命名空间 - `source/more_abstraction/class_namespace.py`
* 类的私有属性 - `source/more_abstraction/privacy.py`
* 超类 - `source/more_abstraction/superclass.py`



## 异常



## 魔术方法、属性和迭代器



## 自带电池



## 文件和流



## 图形用户界面



## 数据库支持



## 网络编程



## Python 和 Web



## 测试



## 扩展 Python



## 程序打包



