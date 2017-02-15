# 创建函数
def hello(name):
    return 'Hello, ' + name + '!'


def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result


# 给函数添加文档
def square(x):
    """Calculates the square of the number x."""
    return x*x
# 打印函数文档
print(square.__doc__)

