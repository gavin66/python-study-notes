class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


sec = Secretive()
# 这样会报错
sec.__inaccessible()
# 虽说它是私有属性 但可以使用下划线加类名来访问
sec._Secretive__inaccessible()