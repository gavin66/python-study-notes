# 关键字参数
def hello_1(greeting, name):
    print('%s, %s!' % (greeting, name))
hello_1(name='t', greeting='h')


# 默认值
def hello_3(greeting='Hello', name='world'):
    print('%s, %s!' % (greeting, name))

hello_3()


# 收集参数
def print_params_2(title, *params):
    print(title)
    print(params)
print_params_2('Params:', 1, 2, 3)


def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)


# 反转过程
def add(x, y): return x + y
params = (1, 2)
add(*params)

params = {'name': 'Sir Robin', 'greeting': 'Well met'}
hello_3(**params)