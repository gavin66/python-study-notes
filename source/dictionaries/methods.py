from copy import deepcopy

# 字典方法
# clear 清除字典中所有的项
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
d.clear()
print(d)

# copy 浅复制
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

# 深复制
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

# fromkeys
# 使用给定的键建立新的字典，每个键默认的值为None
print({}.fromkeys(['name', 'age']))
# 也可以调用dict
print(dict.fromkeys(['name', 'age']))
# 可提供默认值
print(dict.fromkeys(['name', 'age'], '(unknown)'))

# get
# 更宽松的访问字典项 访问不存在的键时，没有异常，会得到None值。
d = {}
# 会有异常发生
# print(d['name'])
# 不会有异常
print(d.get('name'))

# items
# 返回一个迭代器对象
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())

# keys
# 返回键的迭代器对象
print(d.keys())

# pop
# 返回给定的键的值，然后从字典中移除此项
d = {'x': 1, 'y': 2}
print(d.pop('x'))
print(d)

# popitem
# 弹出随机项，并移除此项
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.popitem())
print(d)

# setdefault
# 某种程度类似于get，可以获取给定键的相关值。除此之外，还能在字典不含有键的情况下设定相关键值
d = {}
d.setdefault('name', 'N/A')
print(d)

# update
# 利用一个字典更新另外一个字典
d = {
       'title': 'Python Web Site',
       'url': 'http://www.python.org',
       'changed': 'Mar 14 22:09:15 MET 2008'
    }
x = {'title': 'Python Language Website'}
d.update(x)
print(d)

# values
# 返回值的迭代对象
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
print(d.values())