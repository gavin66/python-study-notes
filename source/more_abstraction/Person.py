class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello, world! I'm %s." % self.name)

foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')
foo.greet()
bar.greet()
