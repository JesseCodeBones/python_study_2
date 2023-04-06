import os

# pid = os.fork()

# if pid == 0:
#     print("I am from father process")
# else:
#     print("I am from child process")

from multiprocessing import Process, Pool

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    l = Pool(4)
    l.apply_async(run_proc, args=('test',))
    # p = Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    print('Child process end.')
# Python 的 multiprocessing和Queue还支持分布式部署
