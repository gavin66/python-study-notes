def process(string):
    print('Processing:', string)

f = open('hello.txt')
while True:
    char = f.read(1)
    if not char:
        break
    process(char)
f.close()
