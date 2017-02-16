# property 函数
class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    size = property(get_size, set_size)

r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
print(r.width)


