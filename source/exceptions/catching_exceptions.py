try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x/y)
except ZeroDivisionError:
    print("The second number can't be zero!")


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

# 捕获多异常
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x/y)
except ZeroDivisionError:
    print("The second number can't be zero!")
except TypeError:
    print("That wasn't a number, was it?")

# 用一个块捕获两个异常
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(x/y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus...')


# 捕获对象
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x/y)
except (ZeroDivisionError, TypeError) as e:
    print(e)


# 捕获所有异常
try:
    x = input('Enter the first number: ')
    y = input('Enter the second number: ')
    print(int(x)/int(y))
except:
    print('Something wrong happened...')

# else 语句
try:
    print('A simple task')
except:
    print('What? Something went wrong?')
else:
    print('Ah... It went as planned.')

# 循环
while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = int(x)/int(y)
        print('x/y is', value)
    except:
        print('Invalid input. Please try again.')
    else:
        break

# finally 语句
x = None
try:
    x = 1/0
finally:
    print('Cleaning up...')
    del x

try:
    1/0
except NameError:
    print("Unknown variable")
else:
    print("That went well!")
finally:
    print("Cleaning up.")