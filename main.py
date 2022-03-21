from ctypes import resize
import tkinter
import threading
from PIL import ImageTk, Image
from time import sleep

# Variabes globales y semafóros. #
MAX_ELFS = 3
MAX_REINDEERS = 7
elfs = 0
reindeers = 0
elfs_sem = threading.Semaphore()
reindeer_sem = threading.Semaphore(MAX_REINDEERS)
mutex = threading.Semaphore()
santa_sem = threading.Semaphore()
elfs_mutex = threading.Semaphore()

# Inicialización de la interfaz gráfica
App = tkinter.Tk()
App.title("Santa Claus 🎅")
App.geometry("700x350")

# Se cargan las impagenes de los duendes.
elf_img = ImageTk.PhotoImage(Image.open("res/santa.jpg"))

# Imégen en la app correspondiente a los duendes.
elf_gui = tkinter.Label(App, image = elf_img)
elf_gui.grid(row = 0, column = 0)

# Etiqueta del conteo de duendes.
elfs_cont = tkinter.StringVar()
elf_lb = tkinter.Label(App, textvariable = elfs_cont).grid(row = 1, column = 0)


# -------------------- Funciones para modificar la interfaz grafica. -------------------- #

# Función de solicitud de ayuda de los duendes.
def elfs_get_help() -> None:
    pass

# Función para atender a los procesos renos.
def prepare_sled() -> None:
    pass

# Función para definir que los regalos se repartieron.
def gifts() -> None:
    pass

# Función para domir a santa.
def back_to_sleep() -> None:
    elf_gui.configure(image = ches_img)

# Función para el proceso de santa claus. #
def santa_process() -> None:
    global reindeers, MAX_REINDEERS, elfs, MAX_ELFS
    print("El santa se anda échando una jeta...")
    while True:
        santa_sem.acquire()
        mutex.acquire()
        if reindeers == MAX_REINDEERS:
            print("Preparando trineo...")
            # Liberación de los procesos de los renos.
            while reindeers:
                reindeers -= 1
                reindeer_sem.release()
            sleep(3)
        elif elfs == MAX_ELFS:
            print("Santa ayuda a los duendes...")
            # Liberación de los duendes.
            while elfs:
                elfs -= 1
                sleep(1)
            sleep(1)
        mutex.release()
        back_to_sleep()

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
        elfs_cont.set(f"{elfs} Duendes trabajando")
        sleep(1)
        mutex.acquire()
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
    santa_thread = threading.Thread(target = santa_process)
    elf_threads = threading.Thread(target = elf_process)
    reindeer_threads = threading.Thread(target = reindeer_process)

    santa_thread.start()
    elf_threads.start()
    reindeer_threads.start()

    App.mainloop()