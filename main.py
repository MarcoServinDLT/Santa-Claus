import threading
from time import sleep
import tkinter
from PIL import ImageTk, Image

# -------------------- Variables -------------------- #
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

# -------------------- Interfaz -------------------- #

# Inicialización de la interfaz gráfica
App = tkinter.Tk()
App.title("Santa Claus 🎅")
App.geometry("700x350")
# App["background"] = "#343a40"

# Se cargan las impagenes de los duendes.
elf_img = ImageTk.PhotoImage(Image.open("res/si.png"))

# Se cargan las imagenes de los renos.
reindeer_img = ImageTk.PhotoImage(Image.open("res/si.png"))

# Se cargan las imagenes para santa.
santa_zzz_img = ImageTk.PhotoImage(Image.open("res/si.png"))
santa_work_img = ImageTk.PhotoImage(Image.open("res/si.png"))
santa_sled = ImageTk.PhotoImage(Image.open("res/si.png"))

# Imégen en la app correspondiente a los duendes.
elf_gui = tkinter.Label(App, image = elf_img)
elf_gui.grid(row = 0, column = 0)

# Etiqueta del conteo de duendes.
elfs_cont = tkinter.StringVar()
elf_lb = tkinter.Label(App, textvariable = elfs_cont).grid(row = 1, column = 0)


# Imágen en la app correspondiente a los renos.
reindeer_gui = tkinter.Label(App, image = reindeer_img)
reindeer_gui.grid(row = 0, column = 1)

# Etiquwta del conteo de renos.
reindeer_cont = tkinter.StringVar()
reindeer_lb = tkinter.Label(App, textvariable = reindeer_cont).grid(row = 1, column = 2)

# Imagen de santa.
santa_gui = tkinter.Label(App, image = santa_zzz_img)
santa_gui.grid(row = 0, column = 2, sticky="nsew")

# Etiqueta del estado de santa
santa_state = tkinter.StringVar()
santa_lb = tkinter.Label(App, textvariable = santa_state).grid(row = 1, column = 1)

# -------------------- Funciones para modificar la interfaz grafica. -------------------- #

# Función para atender a los procesos renos.
def prepare_sled() -> None:
    santa_gui.configure(image = santa_sled)
    santa_state.set("Preparando trineo")

# Función para definir que los regalos se repartieron.
def help_to_elfs() -> None:
    santa_gui.configure(image = santa_work_img)
    santa_state.set("Trabajando")

# Función para domir a santa.
def back_to_sleep() -> None:
    elf_gui.configure(image = santa_zzz_img)
    santa_state.set("Dormido")

# Función para el proceso de santa claus. #
def santa_process() -> None:
    global reindeers, MAX_REINDEERS, elfs, MAX_ELFS
    while True:
        santa_sem.acquire()
        mutex.acquire()
        if reindeers == MAX_REINDEERS:
            prepare_sled()
            # Liberación de los procesos de los renos.
            while reindeers:
                reindeers -= 1
                reindeer_sem.release()
                sleep(2)
        elif elfs == MAX_ELFS:
            help_to_elfs()
            # Liberación de los duendes.
            while elfs:
                elfs -= 1
                sleep(3)
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
        sleep(3)
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
        reindeer_cont.set(f"{reindeers} Renos")
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