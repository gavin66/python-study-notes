class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter 是 Filter 的子类
    def init(self): # 重写 Filter 超类中的 init 方法
        self.blocked = ['SPAM']


f = Filter()
f.init()
print(f.filter([1, 2, 3]))

s = SPAMFilter()
s.init()
print(s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))

# 检测是否是子类
print(issubclass(SPAMFilter, Filter))

# 查看一个类的基类
print(SPAMFilter.__bases__)

# 检测一个对象是否是一个类的实例
s = SPAMFilter()
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter))

# 查看对象属于哪个类
print(s.__class__)