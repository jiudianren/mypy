# 连接


https://mp.weixin.qq.com/s?__biz=MzAwOTc3Mzg2Nw==&mid=2651699063&idx=1&sn=2b879e022d91500f9957b10bac5bb129&chksm=80a36133b7d4e82575b017d2f7c0ce1737db8c55b254ed78937834e168798352b288bd124aac&mpshare=1&scene=24&srcid=&sharer_sharetime=1574947013886&sharer_shareid=00ed5b8dbb28e97d794a35ab3c50f7f4&ascene=14&devicetype=iOS13.2.3&version=17000831&nettype=WIFI&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&fontScale=100&pass_ticket=fcL%2BUfcVDqZ%2BXT2Rqv%2BXVvzKW1%2BPbRt3WqLNYkHdSqYg9AEt7sphE4W6Y0HX%2FmqC&wx_header=1

## threading模块

threading 模块建立在 _thread 模块之上。thread 模块以低级、原始的方式来处理和控制线程，
而 threading 模块通过对 thread 进行二次封装，提供了更方便的 api 来处理线程。


 

Thread方法说明

t.start() : 激活线程，
t.getName() : 获取线程的名称
t.setName() ：设置线程的名称 
t.name : 获取或设置线程的名称
t.is_alive() ：判断线程是否为激活状态
t.isAlive() ：判断线程是否为激活状态
t.setDaemon() 设置为后台线程或前台线程（默认：False）;通过一个布尔值设置线程是否为守护线程，必须在执行start()方法之后才可以使用。如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，均停止；如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
t.isDaemon() ：判断是否为守护线程
t.ident ：获取线程的标识符。线程标识符是一个非零整数，只有在调用了start()方法之后该属性才有效，否则它只返回None。
t.join() ：逐个执行每个线程，执行完毕后继续往下执行，该方法使得多线程变得无意义
t.run() ：线程被cpu调度后自动执行线程对象的run方法

2、线程锁threading.RLock和threading.Lock

由于线程之间是进行随机调度，并且每个线程可能只执行n条执行之后，CPU接着执行其他线程。
为了保证数据的准确性，引入了锁的概念。所以，可能出现如下问题：

例：假设列表A的所有元素就为0，当一个线程从前向后打印列表的所有元素，
另外一个线程则从后向前修改列表的元素为1,那么输出的时候，列表的元素就会一部分为0，一部分为1,这就导致了数据的不一致。锁的出现解决了这个问题。

 



import threading
import time
 
globals_num = 0
 
lock = threading.RLock()
 
def Func():
    lock.acquire()  # 获得锁
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num)
    lock.release()  # 释放锁
 
for i in range(10):
    t = threading.Thread(target=Func)
    t.start()


 

3、threading.RLock和threading.Lock 的区别

RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。

 



import threading
lock = threading.Lock()    #Lock对象
lock.acquire()
lock.acquire()  #产生了死琐。
lock.release()
lock.release()　

import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire()    #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()


 

4、threading.Event

python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。

事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。

clear：将“Flag”设置为False

set：将“Flag”设置为True

Event.isSet() ：判断标识位是否为Ture。

 



import threading
 
def do(event):
    print('start')
    event.wait()
    print('execute')
 
event_obj = threading.Event()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()
 
event_obj.clear()
inp = input('input:')
if inp == 'true':
    event_obj.set()


 

当线程执行的时候，如果flag为False，则线程会阻塞，当flag为True的时候，线程不会阻塞。它提供了本地和远程的并发性。

5、threading.Condition

一个condition变量总是与某些类型的锁相联系，这个可以使用默认的情况或创建一个，当几个condition变量必须共享和同一个锁的时候，是很有用的。锁是conditon对象的一部分：没有必要分别跟踪。

condition变量服从上下文管理协议：with语句块封闭之前可以获取与锁的联系。acquire() 和 release() 会调用与锁相关联的相应的方法。

其他和锁关联的方法必须被调用，wait()方法会释放锁，当另外一个线程使用 notify() or notify_all()唤醒它之前会一直阻塞。一旦被唤醒，wait()会重新获得锁并返回，

Condition类实现了一个conditon变量。这个conditiaon变量允许一个或多个线程等待，直到他们被另一个线程通知。如果lock参数，被给定一个非空的值，，那么他必须是一个lock或者Rlock对象，它用来做底层锁。否则，会创建一个新的Rlock对象，用来做底层锁。

wait(timeout=None) ：等待通知，或者等到设定的超时时间。当调用这wait()方法时，如果调用它的线程没有得到锁，那么会抛出一个RuntimeError 异常。wati()释放锁以后，在被调用相同条件的另一个进程用notify() or notify_all() 叫醒之前 会一直阻塞。wait() 还可以指定一个超时时间。

如果有等待的线程，notify()方法会唤醒一个在等待conditon变量的线程。notify_all() 则会唤醒所有在等待conditon变量的线程。

注意：notify()和notify_all()不会释放锁，也就是说，线程被唤醒后不会立刻返回他们的wait() 调用。除非线程调用notify()和notify_all()之后放弃了锁的所有权。

 

在典型的设计风格里，利用condition变量用锁去通许访问一些共享状态，线程在获取到它想得到的状态前，会反复调用wait()。修改状态的线程在他们状态改变时调用 notify() or notify_all()，用这种方式，线程会尽可能的获取到想要的一个等待者状态。例子：生产者-消费者模型，

 



import threading
import time
def consumer(cond):
    with cond:
        print("consumer before wait")
        cond.wait()
        print("consumer after wait")
 
def producer(cond):
    with cond:
        print("producer before notifyAll")
        cond.notifyAll()
        print("producer after notifyAll")
 
condition = threading.Condition()
c1 = threading.Thread(name="c1", target=consumer, args=(condition,))
c2 = threading.Thread(name="c2", target=consumer, args=(condition,))
 
p = threading.Thread(name="p", target=producer, args=(condition,))
 
c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()


 

6、queue模块

Queue 就是对队列，它是线程安全的

举例来说，我们去麦当劳吃饭。饭店里面有厨师职位，前台负责把厨房做好的饭卖给顾客，顾客则去前台领取做好的饭。这里的前台就相当于我们的队列。形成管道样，厨师做好饭通过前台传送给顾客，所谓单向队列

这个模型也叫生产者-消费者模型。

 



import queue

q = queue.Queue(maxsize=0)  # 构造一个先进显出队列，maxsize指定队列长度，为0 时，表示队列长度无限制。

q.join()    # 等到队列为kong的时候，在执行别的操作
q.qsize()   # 返回队列的大小 （不可靠）
q.empty()   # 当队列为空的时候，返回True 否则返回False （不可靠）
q.full()    # 当队列满的时候，返回True，否则返回False （不可靠）
q.put(item, block=True, timeout=None) #  将item放入Queue尾部，item必须存在，可以参数block默认为True,表示当队列满时，会等待队列给出可用位置，
　　　　　　　　　　　　　　　　　　　　　　　　 为False时为非阻塞，此时如果队列已满，会引发queue.Full 异常。可选参数timeout，表示 会阻塞设置的时间，过后，
　　　　　　　　　　　　　　　　　　　　　　　　  如果队列无法给出放入item的位置，则引发 queue.Full 异常
q.get(block=True, timeout=None) #   移除并返回队列头部的一个值，可选参数block默认为True，表示获取值的时候，如果队列为空，则阻塞，为False时，不阻塞，
　　　　　　　　　　　　　　　　　　　　　　若此时队列为空，则引发 queue.Empty异常。可选参数timeout，表示会阻塞设置的时候，过后，如果队列为空，则引发Empty异常。
q.put_nowait(item) #   等效于 put(item,block=False)
q.get_nowait() #    等效于 get(item,block=False)


 

代码如下：

 



#!/usr/bin/env python
import Queue
import threading


message = Queue.Queue(10)


def producer(i):
    while True:
        message.put(i)


def consumer(i):
    while True:
        msg = message.get()


for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()


 

那就自己做个线程池吧：



 方法一



 方法二

 

python 进程
 

multiprocessing是python的多进程管理包，和threading.Thread类似。

1、multiprocessing模块

直接从侧面用subprocesses替换线程使用GIL的方式，由于这一点，multiprocessing模块可以让程序员在给定的机器上充分的利用CPU。在multiprocessing中，通过创建Process对象生成进程，然后调用它的start()方法，

 



from multiprocessing import Process

def func(name):
    print('hello', name)


if __name__ == "__main__":
    p = Process(target=func,args=('zhangyanlin',))
    p.start()
    p.join()  # 等待进程执行完毕


 

在使用并发设计的时候最好尽可能的避免共享数据，尤其是在使用多进程的时候。如果你真有需要 要共享数据， multiprocessing提供了两种方式。

（1）multiprocessing，Array,Value

数据可以用Value或Array存储在一个共享内存地图里，如下：

 



from multiprocessing import Array,Value,Process

def func(a,b):
    a.value = 3.333333333333333
    for i in range(len(b)):
        b[i] = -b[i]


if __name__ == "__main__":
    num = Value('d',0.0)
    arr = Array('i',range(11))


    c = Process(target=func,args=(num,arr))
    d= Process(target=func,args=(num,arr))
    c.start()
    d.start()
    c.join()
    d.join()

    print(num.value)
    for i in arr:
        print(i)
输出：
　　3.1415927
　　[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]


 

创建num和arr时，“d”和“i”参数由Array模块使用的typecodes创建：“d”表示一个双精度的浮点数，“i”表示一个有符号的整数，这些共享对象将被线程安全的处理。

Array(‘i’, range(10))中的‘i’参数：

 

‘c’: ctypes.c_char　　　　 ‘u’: ctypes.c_wchar　　　　‘b’: ctypes.c_byte　　　　 ‘B’: ctypes.c_ubyte
‘h’: ctypes.c_short　　　  ‘H’: ctypes.c_ushort　　  ‘i’: ctypes.c_int　　　　　 ‘I’: ctypes.c_uint
‘l’: ctypes.c_long,　　　　‘L’: ctypes.c_ulong　　　　‘f’: ctypes.c_float　　　　‘d’: ctypes.c_double
 

（2）multiprocessing，Manager

由Manager()返回的manager提供list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Barrier, Queue, Value and Array类型的支持。

 



from multiprocessing import Process,Manager
def f(d,l):
    d["name"] = "zhangyanlin"
    d["age"] = 18
    d["Job"] = "pythoner"
    l.reverse()

if __name__ == "__main__":
    with Manager() as man:
        d = man.dict()
        l = man.list(range(10))

        p = Process(target=f,args=(d,l))
        p.start()
        p.join()

        print(d)
        print(l)

输出：
　　{0.25: None, 1: '1', '2': 2}
　　[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


 

Server process manager比 shared memory 更灵活，因为它可以支持任意的对象类型。另外，一个单独的manager可以通过进程在网络上不同的计算机之间共享，不过他比shared memory要慢。

2、进程池（Using a pool of workers）

Pool类描述了一个工作进程池，他有几种不同的方法让任务卸载工作进程。

进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。

我们可以用Pool类创建一个进程池， 展开提交的任务给进程池。例：

 



#apply
from  multiprocessing import Pool
import time

def f1(i):
    time.sleep(0.5)
    print(i)
    return i + 100

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(1,31):
        pool.apply(func=f1,args=(i,))

#apply_async
def f1(i):
    time.sleep(0.5)
    print(i)
    return i + 100
def f2(arg):
    print(arg)

if __name__ == "__main__":
    pool = Pool(5)
    for i in range(1,31):
        pool.apply_async(func=f1,args=(i,),callback=f2)
    pool.close()
    pool.join()


 

一个进程池对象可以控制工作进程池的哪些工作可以被提交，它支持超时和回调的异步结果，有一个类似map的实现。

processes ：使用的工作进程的数量，如果processes是None那么使用 os.cpu_count()返回的数量。

initializer：如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。

maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个心的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。

context: 用在制定工作进程启动时的上下文，一般使用 multiprocessing.Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context

注意：Pool对象的方法只可以被创建pool的进程所调用。

New in version 3.2: maxtasksperchild

New in version 3.4: context

 

进程池的方法

apply(func[, args[, kwds]]) ：使用arg和kwds参数调用func函数，结果返回前会一直阻塞，由于这个原因，apply_async()更适合并发执行，另外，func函数仅被pool中的一个进程运行。

apply_async(func[, args[, kwds[, callback[, error_callback]]]]) ：apply()方法的一个变体，会返回一个结果对象。如果callback被指定，那么callback可以接收一个参数然后被调用，当结果准备好回调时会调用callback，调用失败时，则用error_callback替换callback。Callbacks应被立即完成，否则处理结果的线程会被阻塞。

close() ：阻止更多的任务提交到pool，待任务完成后，工作进程会退出。

terminate() ：不管任务是否完成，立即停止工作进程。在对pool对象进程垃圾回收的时候，会立即调用terminate()。

join() : wait工作线程的退出，在调用join()前，必须调用close() or terminate()。这样是因为被终止的进程需要被父进程调用wait（join等价与wait），否则进程会成为僵尸进程。

map(func, iterable[, chunksize])¶

map_async(func, iterable[, chunksize[, callback[, error_callback]]])¶

imap(func, iterable[, chunksize])¶

imap_unordered(func, iterable[, chunksize])

starmap(func, iterable[, chunksize])¶

starmap_async(func, iterable[, chunksize[, callback[, error_back]]])

python 协程
 

线程和进程的操作是由程序触发系统接口，最后的执行者是系统；协程的操作则是程序员。

协程存在的意义：对于多线程应用，CPU通过切片的方式来切换线程间的执行，线程切换时需要耗时（保存状态，下次继续）。协程，则只使用一个线程，在一个线程中规定某个代码块执行顺序。

协程的适用场景：当程序中存在大量不需要CPU的操作时（IO），适用于协程；

event loop是协程执行的控制点， 如果你希望执行协程， 就需要用到它们。

event loop提供了如下的特性：

注册、执行、取消延时调用(异步函数)

创建用于通信的client和server协议(工具)

创建和别的程序通信的子进程和协议(工具)

把函数调用送入线程池中

协程示例：

 



import asyncio
 
async def cor1():
    print("COR1 start")
    await cor2()
    print("COR1 end")
 
async def cor2():
    print("COR2")
 
loop = asyncio.get_event_loop()
loop.run_until_complete(cor1())
loop.close()


 

最后三行是重点。

asyncio.get_event_loop()  : asyncio启动默认的event loop 

run_until_complete()  :  这个函数是阻塞执行的，知道所有的异步函数执行完成，

close()  :  关闭event loop。

1、greenlet

 



import greenlet


def fun1():
    print("12")
    gr2.switch()
    print("56")
    gr2.switch()

def fun2():
    print("34")
    gr1.switch()
    print("78")


gr1 = greenlet.greenlet(fun1)
gr2 = greenlet.greenlet(fun2)
gr1.switch()


 

2、gevent

gevent属于第三方模块需要下载安装包

pip3 install --upgrade pip3

pip3 install gevent

 



import gevent

def fun1():
    print("www.baidu.com")   # 第一步
    gevent.sleep(0)
    print("end the baidu.com")  # 第三步

def fun2():
    print("www.zhihu.com")   # 第二步
    gevent.sleep(0)
    print("end th zhihu.com")  # 第四步

gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
])


 

遇到IO操作自动切换：



 工作中用到协程的地方