import tkinter
import threading
from time import sleep

# Variabes globales y semaforos. #
MAX_ELFS = 3
MAX_REINDEERS = 7
elfs = 0
reindeers = 0
elfs_sem = threading.Semaphore()
reindeer_sem = threading.Semaphore()
mutex = threading.Semaphore(1)
santa_sem = threading.Semaphore()
elfs_mutex = threading.Semaphore()

# Función para el proceso de santa claus. #
def santa_process() -> None:
    global reindeers, MAX_REINDEERS, elfs, MAX_ELFS
    print("El santa se anda échando una jeta...")
    while True:
        santa_sem.acquire()
        mutex.acquire()
        if reindeers == MAX_REINDEERS:
            print("Preparando trineo...")
            while reindeers:
                reindeers -= 1
                reindeer_sem.release()
            sleep(3)
        elif elfs == MAX_ELFS:
            print("Santa ayuda a los duendes...")
            for i in range(MAX_ELFS):
                elfs_sem.release()
        mutex.release()

# Función para el proceso de los duendes. #
def elf_process() -> None:
    global elfs, MAX_ELFS
    while True:
        elfs_mutex.acquire()
        mutex.acquire()
        elfs += 1
        if elfs == MAX_ELFS:
            santa_sem.release()
        else:
            elfs_mutex.release()
        mutex.release()
        print("número de duendes:", elfs)
        elfs_sem.acquire()
        mutex.acquire()
        elfs -= 1
        if not elfs:
            elfs_mutex.release()
        mutex.release()


# Función para realizar el proceso de los renos. #
def reindeer_process() -> None:
    global reindeers, MAX_REINDEERS
    while True:
        mutex.acquire()
        reindeers += 1
        if reindeers == MAX_REINDEERS:
            santa_sem.release()
        mutex.release()
        print('total de renos:', reindeers)
        reindeer_sem.acquire()
        sleep(1)

# Ejecución principal del programa.
if __name__ == "__main__":
    santa_thread = threading.Thread(target=santa_process)
    elf_threads = threading.Thread(target=elf_process)
    reindeer_threads = threading.Thread(target=reindeer_process)

    santa_thread.start()
    elf_threads.start()
    reindeer_threads.start()
