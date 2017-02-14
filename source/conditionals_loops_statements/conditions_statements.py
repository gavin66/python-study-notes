
name = input('What is your name? ')
# if 语句
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')
# else 语句
else:
    print('Hello, stranger')

# else if 子句
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

# 嵌套代码块
name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello, Gumby')
else:
    print('Hello, stranger')

# 比较运算符