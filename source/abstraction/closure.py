# 闭包示例
def func(name):
    def inner_func(age):
        print('name:', name, 'age:', age)
    return inner_func

bb = func('the5fire')
bb(26)


# 在 python 的函数内，可以直接引用外部变量，但不能改写外部变量，因此如果在闭包中直接改写父函数的变量，就会发生错误
# nonlocal 语句会去搜寻本地变量与全局变量之间的变量，其会优先寻找层级关系与闭包作用域最近的外部变量
def cnt(param):
    count = 0

    def counter():
        nonlocal count
        count += 1
        print("I'm,", param, 'No.', str(count))

    return counter

gavin = cnt('gavin')
gavin()
gavin()
gavin()
