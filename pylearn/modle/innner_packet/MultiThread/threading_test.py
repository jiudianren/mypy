import threading
import time
 
def worker(num):
    """
    thread worker function
    :return:
    """
    time.sleep(1)
    print("The num is  %d" % num)
    print()
    return
 
for i in range(10):
    t = threading.Thread(target=worker,args=(i,),name= "t.%d" % i)
    t.start()
    print(f" thead name:{t.getName()}")