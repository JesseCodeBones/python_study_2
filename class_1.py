class student:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score
    def print(self)->None:
        print('name:', self.name, '\nscore:', self.score)
 
s = student('jesse', 99)
s.print()


class Animal(object):
    name="Animal"
    def run(self):
        print('animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running')

D = Dog()
D.run()
print(dir(D))


# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
S = Student()
#S.score=22 #Error

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# __str__ print self
# __repr__ print in debugger
# __iter__ & __next__ iterator
# __getitem__ []get value
# __call__ directly call

class ForIn(object):
    def __getitem__(self, n):
        return n
F = ForIn()
print(F[10])

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):#get score
        if attr=='score':
            return 99

#dynamic class
Hello = type('Hello', (object,), dict(hello=lambda self: print("hello from dynamic")))
H = Hello()
H.hello()


def errorFoo():
    raise RuntimeError("I am wrong")

try:
    errorFoo()
except RuntimeError as e:
    print('error happenned:', e)
