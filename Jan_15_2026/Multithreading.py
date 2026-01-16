import time, threading
from concurrent.futures import ThreadPoolExecutor

def fun(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

# without multithreading

fun(3)
fun(2)
fun(1)

# with multithreading

t1 = threading.Thread(target=fun, args=[3])
t2 = threading.Thread(target=fun, args=[2])
t3 = threading.Thread(target=fun, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

def pooling():
    with ThreadPoolExecutor() as executor:
        future = executor.submit(fun, 3)
        print(future.result())
        future = executor.submit(fun, 2)
        print(future.result())
        future = executor.submit(fun, 1)
        print(future.result())

pooling()