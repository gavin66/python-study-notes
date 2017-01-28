> 本项目为本人的 Python 自学笔记。根据《Python 基础教程（第二版 修订版）》所得总结。所使用的 Python 版本为 `3.5.1`



## 基础

### 安装 Python

### 交互式解释器

启动 Python 的时候，有如下提示：

![](res/python_console.png)

写下第一个程序（或者执行`$ python source/base/hello.py `）：

```python
>>> print("Hello, world!")
Hello, world!
```

`print`(objects, sep=' ', end='\n', file=sys.stdout, flush=False)

将 object 打印到文本流 file，由 sep分隔，尾部接 end。sep, end 和 file，如果提供这三个参数的话，必须以关键参数的形式。
如果没有打印对象, `print()` 只打印一个 结束符号 end.
文件参数必须是具有`write(string)`方法的对象；如果不存在或`None`，将使用`sys.stdout`。由于打印的参数被转换为文本字符串，因此`print()`不能与二进制模式文件对象一起使用。对于这些，请改用`file.write(...)`。
尽管通常是由 file 参数来决定输出流是否缓存，但是如果 flush 参数为ture，那么输出流将会被强制刷新。
在版本3.3中已更改：添加了 flush 关键字参数。

> 行尾不需添加分号，这点不同于其他语言。如果一行有更多语句，需分号，但不建议这样的编程习惯。



### 数字和表达式

示例：`$ python source/base/numeral.py `



## 列表和元组



## 使用字符串



##  字典



## 条件、循环和其他语句



## 抽象



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



