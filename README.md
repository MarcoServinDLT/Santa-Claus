# Santa-Claus
Solución al problema de Santa Claus con programación concurrente.

**¡¡El programa cuenta con interfaz gráfica!!**

## ¿Cómo funciona?
Para comprender el funcionamiento del programa es necesario comprender lo que se quiere solucionar, en este caso la problemática corresponde a tratar de identificar trastornos (estos se encuentran ampliamente descritos en los distintos documentos ubicados en la carpeta **context**). Los trastornos cuentan con una gran cantidad de condiciones y restricciones para su diagnostico.

Debido a que muchos trastornos comparten síntomas, se pensó en solucionar el problema mediante teoría de conjuntos, realizando preguntas de los más general (los síntomas más comunes en los diferentes trastornos) a lo particular (síntomas propios del trastorno), lo cual ayudaba a descartar trastornos de manera más rápida y a no repetir varias veces una misma pregunta, esto también ayudaba parcialmente a identificar de entre dos o más trastornos similares, ya que hay trastornos que no pueden coexistir, debe definirse como uno solamente.

La representación del problema mediante teoría de conjuntos sería la siguiente :


Cuando el trastorno se encuentra en la base de conocimientos del programa, este mismo notificará el diagnostico, de lo contrario, el programa notificará que no se identificó ningún trastorno, por lo que preguntará si conoces el nombre del trastorno, en caso de que la respuesta sea negativa el programa finalizará, si la respuesta fue positiva, el programa solicitará preguntas basadas en los criterios de diagnostico del trastorno para aprenderlo.

## Requisitos⚙️

## Construido con...🛠️

## Ejecución
```bash
[python | python3 | py] main.py
```
