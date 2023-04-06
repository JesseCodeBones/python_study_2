import threading
def loop():
    n=0
    while n < 5:
        n =  n + 1
        print(threading.current_thread().name, ", ", n)
t = threading.Thread(target=loop, name='childThread')
t.start()
t.join()
print('parent thread=', threading.current_thread().name)

glb = {}
glb['number'] = 0
mLock = threading.Lock()

def fun():
    n = 0
    while n < 900000:
        n = n + 1
        mLock.acquire()
        glb['number'] = glb['number'] + 1
        mLock.release()
t1 = threading.Thread(target=fun, name="t1")
t2 = threading.Thread(target=fun, name='t2')
t1.start()
t2.start()
t1.join()
t2.join()
print(glb)