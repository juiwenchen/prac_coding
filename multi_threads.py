from threading import Thread, Lock
from time import sleep

counter = 0

mutex = Lock()

def touch_counter(idx, increment):
    global counter

    mutex.acquire() # this thread get the mutex and is exclusive to use this function

    print(f"thread {idx} is running")

    local_counter  = counter
    local_counter += increment

    sleep(0.5) # wait for other thread to execute

    counter = local_counter
    print(f"counter = {counter}")
    print(f"thread {idx} finished")

    mutex.release() # release mutex for the other thread

def main():
    # with mutex, these threads will be executed and finished by order. It is know as synchronization
    # without mutex, race condition will occur. The order of threads will be arbitrary 

    for i in range(1,10+1):
        th = Thread(target=touch_counter, args=(i, i))
        th.start()
        print(f"iteration {i}")

if __name__ == "__main__":
    main()