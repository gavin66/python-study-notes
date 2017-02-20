f = open('hello.txt', 'w')
f.write('hello,')
f.write('world!')
f.close()


f = open('hello.txt', 'r')
print(f.read(4))
print(f.read())
f.close()
