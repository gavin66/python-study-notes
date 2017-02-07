import string

# 0 - 9 数字
print(string.digits)
# 所有字母（包括大小写）
print(string.ascii_letters)
# 所有小写字母
print(string.ascii_lowercase)
# 所有可打印字符的字符串
print(string.printable)
# 所有标点
print(string.punctuation)
# 所有大写字母
print(string.ascii_uppercase)

"""
字符串方法
"""
# find
print('With a moo-moo here, and a moo-moo there'.find('moo'))
title = "Monty Python's Flying Circus"
print(title.find('Monty'))
print(title.find('Python'))
print(title.find('Flying'))
print(title.find('Zirquss'))
# 此方法可接受起始点与结束点
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$'))
# 起始点
print(subject.find('$$$', 1))
print(subject.find('!!!'))
# 起始点与结束点
subject.find('!!!', 0, 16)

# join
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

# lower
print('Trondheim Hammer Dance'.lower())

# replace
print('This is a test'.replace('is', 'eez'))

# split
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
# 如果不提供任何分隔符，程序会把所有空格作为分隔符
print('Using   the   default'.split())

# strip
# 去除两侧空格的字符串
print('      internal whitespace is kept      '.strip())
# 指定去除的字符
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))

# translate
# translate 与 replace 方法一样，可以替换字符串的某些部分，但是不同点，translate只处理单个字符。它的优势在于同时进行多个替换,比replace效率高。
table = str.maketrans('cs', 'kz')
print('this is an incredible test'.translate(table))