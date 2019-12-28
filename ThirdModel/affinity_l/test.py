
import multiprocessing, time, signal  
import affinity

p = multiprocessing.Process(target=time.sleep, args=(1000,))  
p.start()  
pid=p.pid  
print(pid)
affinity.get_process_affinity_mask(pid)  
#affinity.set_process_affinity_mask(pid, 2L)  
affinity.get_process_affinity_mask(pid)  
