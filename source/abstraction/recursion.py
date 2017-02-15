# 阶乘：循环
def factorial_for(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

print(factorial_for(3))


# 阶乘：递归
def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial_rec(n-1)

print(factorial_rec(3))


# 二分查找：递归
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print(search(seq, 34))
