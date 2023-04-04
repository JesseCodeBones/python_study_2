def myAdd(x, y):
    if not isinstance(x, (int, float)) and not isinstance(y, (float, int)):
        raise TypeError("error type")
    return x+y

print(myAdd(1,2))

def nop():
    pass

def allAddOne(x, y):
    return x+1, y+1

x, y = allAddOne(1,2)
print(x)
print(y)

def printList(l=[]): # 默认参数必须是不可变参数，因为编译器会指向同一个对象
    l.append("End")
    for i in l:
        print(i)
printList()
printList()

# 要修改上面的例子，我们可以用None这个不变对象来实现：

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def multiParameter(*params):
    for param in params:
        print(param)
multiParameter(1,2,3)

nums = [3,2,1]
multiParameter(*nums)

def keyvalue(name, age, **kw):
    print('name:', name, ',age:', age, ',other:', kw)
    if 'job' in kw:
        print('great, you have a job')

keyvalue('jesse', 32, citi='shanghai', job='software')

# hybrid function
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
