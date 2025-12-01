"""Q18. Write a multithreaded program where multiple threads update a shared counter variable. 
Use Lock to prevent race conditions."""
import threading 
 
class SharedCounter: 
    def __init__(self): 
        self.value = 0 
        self.lock = threading.Lock() 
 
    def increment(self): 
        with self.lock: 
            temp = self.value 
            temp += 1 
            self.value = temp 
 
def worker(counter, increments): 
    for _ in range(increments): 
        counter.increment() 
 
if __name__ == "__main__": 
    counter = SharedCounter() 
    threads = [] 
    num_threads = 5 
    increments_per_thread = 100000 
 
    for _ in range(num_threads): 
        t = threading.Thread(target=worker, args=(counter, increments_per_thread)) 
        threads.append(t) 
        t.start() 
 
    for t in threads: 
        t.join() 
 
    print("Expected:", num_threads * increments_per_thread) 
    print("Actual  :", counter.value) 
