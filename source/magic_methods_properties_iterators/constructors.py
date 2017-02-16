# 简单的构造方法
class FooBar:
    def __init__(self):
        self.somevar = 42

f = FooBar()
print(f.somevar)


# 使用 super 调用父类方法
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')


class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()
sb.eat()
sb.eat()
