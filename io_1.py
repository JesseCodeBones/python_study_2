try:
    f = open('class_1.py', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('class_1.py', 'r') as f:
    for line in f.readlines():
        print(line)

with open('test.txt', 'w') as f:
    f.write('hello world')

# StringIO 操作内存
# BytesIO 二进制的形式操作内存
import os
print(os.path.abspath('.'))
print(os.path.join('/', 'home'))
os.path.split('/Users/michael/testdir/file.txt')
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')