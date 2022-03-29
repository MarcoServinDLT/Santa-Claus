# Santa-Claus
Solución al problema de Santa Claus con programación concurrente.

**¡¡El programa cuenta con interfaz gráfica!!**

----
## Problematica 
Santa Claus pasa su tiempo de descanso, durmiendo, en su casa del Polo Norte. 
Para poder despertarlo se ha de cumplir una de las 2 condiciones siguientes:

  1. Que todos los renos de los que dispone, 7 en total, hayan vuelto de vacaciones.
  2. Que algunos de sus duendes necesiten su ayuda para fabricar un juguete.

Para permitir que Santa Claus pueda descansar, los duendes han acordado despertarle si 3 de ellos tienen problemas a la hora de fabricar un juguete. en el caso de que un grupo de 3 duendes están siendo ayudados por Santa, el resto de los duendes con problemas tendrán que esperar a que Santa termine de ayudar al primer grupo.
En caso de que haya duendes esperando y todos los renos hayan vuelto de vacaciones, entonces Santa Claus decidirá preparar el trineo y repartir los regalos, ya que su entrega es más importante que la fabricación de otros juguetes que podrían esperar al año siguiente. El último reno en llegar ha de despertar a Santa mientras el resto de los renos esperan antes de ser enganchados al trineo.

## ¿Cómo funciona?
Para solucionar este problema, se pueden distinguir 3 procesos básicos: Santa Claus, duende y reno. respecto a los recursos compartidos, es necesario controlar el número de duendes que, en un determinado momento, necesitan la ayuda de Santa y el número de renos que, en un determinado momento están disponibles.

Evidentemente, el acceso concurrente a estas variables ha de estar controlado por un semáforo binario.
Respecto a los eventos de sincronización, será necesario disponer de mecanismos para despertar a Santa Claus, notificar a los renos que se han de enganchar al trineo y controlar la espera por parte de los duendes cuando otro grupo de duendes esté siendo ayudado por Santa Claus.

En resumen, se utilizarán las siguientes estructuras para plantear la solución del problema:

  1. Elfs: variable compartida que contiene el número de duendes que necesitan la ayuda de Santa en un determinado instante de tiempo
  2. Reindeers: variable compartida que contiene el número de renos que han vuelta de vacaciones y están disponibles para viajar.
  3. Mutex: semáforo binario que controla el acceso a duendes y renos.
  4. Santa_sem: Semáforo binario utilizado para despertar a Santa Claus
  5. Reindeers_sem: semáforo contador utilizado para notificar a los renos que van a emprender el viaje en trineo

## Requisitos⚙️
  1. Python 3
  
## Construido con...🛠️
  1. Python 3 
  2. Libreria tkinter
  
## Ejecución
```
python main.py
```
