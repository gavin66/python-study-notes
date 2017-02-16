# 普通生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)


# 递归生成器
def flatten2(nested):
    try:
        for sublist in nested:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested

print(list(flatten2([[[1], 2], 3, 4, [5, [6, 7]], 8])))
