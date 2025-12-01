"""Q17. Write a Python program to create two threads- one to print even numbers and an other to 
print odd numbers up to n. Synchronize the threads to alternate properly."""

import threading 
 
def even_printer(n, cond, state): 
    i = 0 
    while i <= n: 
        with cond: 
            while state[0] != 0: 
                cond.wait() 
            print(i, end=" ", flush=True) 
            i += 2 
            state[0] = 1 
            cond.notify() 
 
def odd_printer(n, cond, state): 
    i = 1 
    while i <= n: 
        with cond: 
            while state[0] != 1: 
                cond.wait() 
            print(i, end=" ", flush=True) 
            i += 2 
            state[0] = 0 
            cond.notify() 
 
if __name__ == "__main__": 
    n = int(input("Enter n (>=0): ")) 
    cond = threading.Condition() 
    # state[0] == 0 -> even's turn, ==1 -> odd's turn 
    state = [0] 
    t1 = threading.Thread(target=even_printer, args=(n, cond, state)) 
    t2 = threading.Thread(target=odd_printer, args=(n, cond, state)) 
    t1.start(); t2.start() 
    t1.join(); t2.join() 
    print("\nDone.") 
