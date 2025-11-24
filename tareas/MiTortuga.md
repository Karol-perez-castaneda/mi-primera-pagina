<img width="980" height="980" alt="image" src="https://github.com/user-attachments/assets/bb0c8323-ff86-4b52-a4b1-00a5e8bd4d13" />

Como ejercio para aprender las funciones print e imput se trabajo y analizo la biblioteca turtle la cual se puede importar en python con un archivo de extension .py

```python
import turtle

t = turtle.Turtle()   # Crea una tortuga
t.forward(100)        # Avanza 100 unidades
turtle.done()         # Mantiene la ventana abierta
```

Ya importada solo se tiene ingresar a la terminar y escribir

```python
python3 mi_tortuga.py
```
Para tener esta salida

<img width="635" height="407" alt="image" src="https://github.com/user-attachments/assets/c9388382-dbec-4f41-b4fc-09a46d50c2eb" />

Ya sabiendo esto se propusieron **4 Retos** para simular este funcionamiento con variables, funciones, condicionales y ciclos.

### **Reto 1**

En ese primer reto se dio el objetivo de recrear el movimiento de la tortuga únicamente con texto, usando funciones, print() y input()

```python
# Escalon 1
cantidaddepasos1 = int (input("¿Cuantos pasos quieres que avance la tortuga hacia la derecha?"))
trazoadelante1 = "-" * cantidaddepasos1 + ">"
print (trazoadelante1) 
```
- Para definir cuantos pasos realizara la tortuga el sistema le pregunta al usuario cuantos dara la tortuga y el valor definido se guardara en el valor **cantidaddepasos1**
- Con el valor anterior definido se realiza la funcion interna **trazoadelante1** en donde el simbolo **-** se multiplica por la cantidad de de pasos definidos en **cantidaddepasos1** y se le suma un **>** al final para representar el punto donde paro la tortuga.
- Y al final se realiza la funcion de **print** para imprimir el resultado de la funcion **trazoadelante1**

En este caso pondremos el valor 5 para que la tortuga avance 5 pasos, como resultados tendremos:

<img width="920" height="172" alt="image" src="https://github.com/user-attachments/assets/12ca0015-0632-46d2-adf2-5469880409c7" />

### **Reto 2**

En este segundo reto se dio el objetivo de crea el rastro de la tortuga moviéndose hacia abajo usando únicamente print() e input()

```python
# Escalon 2
Abajo = "|"
Flecha = "V"
cantidaddepasos2 = int (input("¿Cuantos pasos quieres que avance la tortuga hacia abajo?"))
count = 1
while count <= cantidaddepasos2:
    print(Abajo)
    count += 1
print (Flecha)
```
- Se le define los valores **Abajo** y el valor **Flecha** con un **V**
- Para definir cuantos pasos realizara la tortuga hacia abajo el sistema le pregunta al usuario cuantos dara la tortuga y el valor definido se guardara en el valor **cantidaddepasos2**
- Se establece un ciclo **While** para imprimir el valor **Abajo** por la cantidad de de pasos definidos en **cantidaddepasos2** para simular que esta bajando la tortuga.
- Se imprime **Flecha** al final para representar el punto donde paro la tortuga.

En este caso pondremos el valor 2 para que la tortuga avance 2 pasos, como resultados tendremos:


<img width="886" height="323" alt="image" src="https://github.com/user-attachments/assets/e45b1c20-ea3c-4a19-bead-c3e6c66c1303" />

### **Reto 3**

En este tercer reto se dio el objetivo de hacer girar la tortuga en la bibloteca Turtle.

```python
import turtle
t = turtle.Turtle()
t.forward(100)
t.right(90)         
t.forward(100)
turtle.done()
```
Para tener la salida en forma de L.

<img width="964" height="832" alt="image" src="https://github.com/user-attachments/assets/39e92615-54e3-4c23-a0e0-8ca57764f83e" />

### **Reto 4**

En este cuarto reto se dio el objetivo de usar funciones para representar los movimientos antes vistos con texto.

```python
# Escalon 1
adelante = "-"
cantidaddepasos1 = 5
espacio = adelante * cantidaddepasos1
trazoadelante1 = espacio + ">"
print (trazoadelante1) 

# Escalon 2
Abajo = "|"
cantidaddepasos2 = 3
espacio = " " * cantidaddepasos1
linea = espacio + Abajo
flecha = espacio  + "V"
count = 1
while count <= cantidaddepasos2:
    print(linea)
    count += 1
print (flecha)
```

En su base se usan los mismos valores antes establecidos y pasos a excepción de:

- En el escalon 2 se define el valor **espacio** para definir cuantos pasos ya dio hacia la derecha la tortuga para asegurar que cuando gire y camine hacia abajo si continue desde donde habia quedado antes multiplicando un espacio en blando " " por la cantidad ya dados hacia la derecha.
- Se define el valor **linea** para asegurarse que las lineas continue desde donde habia quedado antes la tortuga sumando ya los espacios en blanco definidos en el valor **espacio** y sumando el simbolo **Abajo**.
- Se define el valor **flecha** para cumplir con la misma funcion que el anterior valor pero en su lugar de **Abajo** es para poner una **V** al final para representar el punto donde paro la tortuga.
- Se establece un ciclo **While** para imprimir el valor **linea** por la cantidad de de pasos definidos en **cantidaddepasos2** para simular que esta bajando la tortuga.

Como resultados tendremos:

<img width="922" height="491" alt="image" src="https://github.com/user-attachments/assets/3a63625f-9e01-4260-9870-f9d0f52356b4" />

### **Reto 5**

En este quinto reto se dio el objetivo de hacer que la tortuga baje en forma de escalera en el que cada escalón debe conservar la posición horizontal acumulada y dibujar correctamente tanto el tramo horizontal como el vertical.

```python
# Escalon 1
adelante = "-"
cantidaddepasos1 = 5
espacio = adelante * cantidaddepasos1
trazoadelante1 = espacio + ">"
print (trazoadelante1) 

# Escalon 2
Abajo = "|"
cantidaddepasos2 = 3
espacio = " " * cantidaddepasos1
linea = espacio + Abajo
flecha = espacio  + "V"
count = 1
while count <= cantidaddepasos2:
    print(linea)
    count += 1
print (flecha)

# Escalon 3
adelante = "-"
cantidaddepasos3 = 5
espaciototal = " " * cantidaddepasos1
espacio = adelante * cantidaddepasos3
trazoadelante3 = espaciototal + espacio + ">"
print (trazoadelante3) 

# Escalon 4
Abajo = "|"
cantidaddepasos4 = 3
espaciototal = cantidaddepasos1 + cantidaddepasos3
espacio = " " * espaciototal
linea = espacio + Abajo
flecha = espacio  + "V"
count = 1
while count <= cantidaddepasos4:
    print(linea)
    count += 1
print (flecha)
```
En su base se usan los mismos valores antes establecidos y pasos pero con ligeros cambios para que haya continuidad, se resalta el cambio:

- Apartir de escalon 3 se implementa el valor **espaciototal** donde se suman los pasos ya realizados hacia la derecha y se suman son los siguientes que se realizaran hacia esa misma direccion para asegurar la continuidad del recorrido hecho por la tortuga.

Como resultado tendremos esta escalera hecha completamente con texto:

<img width="199" height="219" alt="image" src="https://github.com/user-attachments/assets/23e7dac6-7793-4016-ac84-941d02abce6b" />


# Bibliologia

Guía completa de Ciclos en Python (For y While) 🐍👨‍🏫👌

Code & Chill

[https://medium.com/@diego.coder/ciclos-en-python-for-y-while-20cbe73f7193](https://medium.com/@diego.coder/ciclos-en-python-for-y-while-20cbe73f7193)
