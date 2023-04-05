L = list(range(100))
print(L[:10])
print(L[-2:])
print(L[::5]) # every 5 pick up 1

# loop with index
M = [1,3,5]
for index, item in enumerate(M):
    print('index:', index, ", value:", item)

def printList(L):
    for item in L:
        print(item)

F = (x*x for x in range(1,10))
printList(F)

def odd(): #generator function
    print('process 1')
    yield 1
    print('process 2')
    yield 3
    print('process 3')
    yield 5
o = odd()
printList([next(o),next(o),next(o)])
p = odd()
for n in odd():
    print(n)

# map function

def addOne(x):
    return x+1

r = map(addOne, (1,3,5))
printList(r)

# reduce function
def addTwo(x,y):
    return x+y

from functools import reduce

r = reduce(addTwo, (1,3,4))
print(r)


print('filter')
T = filter(lambda x: x%2==0, (1,2,3,4))
printList(T)


# decorator

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('executing')
def foo():
    print('I am foo')

foo()


import functools

int2 = functools.partial(int, base=2)
print(int2('10010'))
