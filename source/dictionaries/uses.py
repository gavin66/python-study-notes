# 创建字典
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# dict 函数
# 通过其他映射（比如其他字典）或者（键，值）这样的序列对建立字典
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)

# 基本字典操作
# 返回d中项（键值对）的数量
len(d)
# 返回关联到键k的值
print(d['name'])
# 将值v关联到键k上
d['name'] = 'name2'
# 删除键为k的项
del d['name']
# 检查d中是否含有键k的项
print('name' in d)

# 字典格式化字符串
print("Cecil's phone number is %(Cecil)s." % phonebook)

template = '''<html>
    <head><title>%(title)s</title></head>
    <body>
    <h1>%(title)s</h1>
    <p>%(text)s</p>
    </body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template % data)
