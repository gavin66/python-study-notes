fmt = "Hello, %s, %s enough for ya ?"
values = ('world', 'Hot')
print(fmt % values)

# 格式化浮点数，可以使用f说明转换说明符的类型，同时提供所需要的精度，句号加上希望保留的小数位数。
from math import pi
fmt = "Pi with three decimals: %.3f"
print(fmt % pi)

# 模板字符串
from string import Template
s = Template('$x, glorious $x!')
print(s.substitute(x='slurm'))
# 如果替换字段是单词的一部分，那么参数名就必须用括号括起来。
s = Template("It's ${x}tastic!")
print(s.substitute(x='slurm'))
# 使用$$插入美元符号
s = Template("Make $$ selling $x!")
print(s.substitute(x='slurm'))
# 除了使用关键字参数之外，还可以使用字典变量提供值/名称对
s = Template('A $thing must never $action.')
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
print(s.substitute(d))