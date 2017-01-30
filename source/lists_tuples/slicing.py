"""
序列分片
"""

# 使用分片来访问一定范围内的元素
tag = '<a href="http://www.python.org">Python web site</a>'
print('tag = <a href="http://www.python.org">Python web site</a>')
print('tag[9:30]: ' + tag[9:30])
print('tag[32:-4]: ' + tag[32:-4])

numbers = [1,2,3,4,5,6,7,8,9,10]
print('numbers[3:6]: ' + str(numbers[3:6]))
print('访问最后3个元素numbers[7:10]: ' + str(numbers[7:10]))
print('访问最后3个元素numbers[-3:]: ' + str(numbers[-3:]))
print('访问序列前3个元素numbers[:3]: ' + str(numbers[:3]))

# 步长
print('numbers[0:10:1]: ' + str(numbers[0:10:1]))
print('numbers[0:10:2]: ' + str(numbers[0:10:2]))
print('numbers[3:6:3]: ' + str(numbers[3:6:3]))
print('numbers[::4]: ' + str(numbers[::4]))
# 步长可为负数，表示从右往左取值
print('numbers[8:3:-1]: ' + str(numbers[8:3:-1]))
print('numbers[10:0:-2]: ' + str(numbers[10:0:-2]))
print('numbers[0:10:-2]: ' + str(numbers[0:10:-2]))
print('numbers[::-2]: ' + str(numbers[::-2]))
print('numbers[5::-2]: ' + str(numbers[5::-2]))
print('numbers[:5:-2]: ' + str(numbers[:5:-2]))

