import threading
import time


def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)


def print_alphabets():
    for ch in 'ABCDE':
        print("Alphabet:", ch)
        time.sleep(1)


def print_messages():
    for i in range(1, 6):
        print("Hello from Thread 3")
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)
t3 = threading.Thread(target=print_messages)


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

print("All threads completed successfully!")