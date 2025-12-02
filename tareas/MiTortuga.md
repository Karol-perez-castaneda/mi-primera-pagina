# Implementando la Libreria Turtle desde Cero
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/bb0c8323-ff86-4b52-a4b1-00a5e8bd4d13" />

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
pasos_abajo = int (input("¿Cuantos pasos quieres que avance la tortuga hacia abajo?"))
cantidaddepasos2 = pasos_abajo
for i in range (cantidaddepasos2):
            print("|\n", end='')
print("V")
```

- Para definir cuantos pasos realizara la tortuga hacia abajo el sistema le pregunta al usuario cuantos dara la tortuga y el valor definido se guardara en el valor **cantidaddepasos2**
- Se establece un ciclo **range** para imprimir la cantidad de de pasos definidos en **cantidaddepasos2** para simular que esta bajando la tortuga.
- Se imprime **Flecha** al final para representar el punto donde paro la tortuga.

En este caso pondremos el valor 2 para que la tortuga avance 2 pasos, como resultados tendremos:

<img width="887" height="250" alt="image" src="https://github.com/user-attachments/assets/b6388409-c6a9-4c0a-b8f6-05c0d9a27439" />


### **Reto 3**

En este tercer reto se dio el objetivo de hacer girar la tortuga con lo ya trabajado.

```python
espacio= 0

# Escalon 1
cantidaddepasos1 = 5
trazoadelante1 = "-" * cantidaddepasos1 + ">"
global espacio
espacio = cantidaddepasos1
print (trazoadelante1) 

# Escalon 2
pasos_abajo = 4
espacio = " " * cantidaddepasos1
for i in range (pasos_abajo):
            camino_abajo = espacio + "|\n"
            print(camino_abajo, end='')
print( " " * cantidaddepasos1 + "V")


```
En su base se usan los mismos valores antes establecidos y pasos a excepción de:

- Se define el valor **espacio** para definir cuantos pasos ya dio hacia la derecha la tortuga y dandele el balor de **global** para que vaya acumulando la cantidad, para asegurar que cuando gire y camine hacia abajo si continue desde donde habia quedado antes multiplicando un espacio en blando " " por la cantidad ya dados hacia la derecha.

En este caso pondremos el valores 5 y 4 para que la tortuga avance 5 pasos a delante y 4 hacia abajo, como resultados tendremos:

<img width="885" height="509" alt="image" src="https://github.com/user-attachments/assets/c90d3669-b015-4d7b-ad21-af38bee187a3" />


### **Reto 4**

En este cuarto reto se dio el objetivo de usar funciones para representar los movimientos antes vistos con texto.

```python
espacio= 0

# Escalon 1
def adelante(cantidaddepasos1):
    trazoadelante1 = "-" * cantidaddepasos1 + ">"
    global espacio
    espacio = cantidaddepasos1
    print (trazoadelante1) 

# Escalon 2
def abajo(cantidaddepasos2):
    pasos_abajo = cantidaddepasos2
    espacio_ = " " * espacio
    for i in range (pasos_abajo):
            camino_abajo = espacio_ + "|\n"
            print(camino_abajo, end='')
    print( " " * espacio + "V")

```

Ya las lineas ya escritas se les da la **funcion** para que se pueda ejecutar con una interfaz de usuario:

```python
adelante(5)
abajo(5)
```

Como resultados tendremos:

<img width="885" height="243" alt="image" src="https://github.com/user-attachments/assets/e336a7fc-0b0c-4894-b821-b1a05b1bf5a4" />


### **Reto 5**

En este quinto reto se dio el objetivo de hacer que la tortuga baje en forma de escalera en el que cada escalón debe conservar la posición horizontal acumulada y dibujar correctamente tanto el tramo horizontal como el vertical.

```python
espacio= 0

def adelante(pasos_adelante):
    global espacio
    print (espacio * " " + "-" * pasos_adelante + ">")
    espacio = espacio + pasos_adelante

def abajo (pasos_abajo):
    for i in range (pasos_abajo):
                camino_abajo = " " * espacio + "|\n"
                print(camino_abajo, end='')
    print(" " * espacio + "V")
```
En su base se usan los mismos valores antes establecidos y pasos pero con ligeros cambios para que haya continuidad, se resalta el cambio:

- Se modifica la **función** abajo para que tome en cuenta los pasos ya dados por el mismo valor y el de adelante y si poder continuar la escalera en siguientes escalones.

Ya con lo hecho solo se tiene que poner los valores a travez de la interfaz de usuario

```python
adelante(6)
abajo(3)

adelante(5)
abajo(4)

adelante(7)
abajo(3)

```

Como resultado tendremos esta escalera hecha completamente con texto:

<img width="260" height="327" alt="image" src="https://github.com/user-attachments/assets/61b93273-3b5c-4769-8242-49ea37e30337" />


### Esta evidencia se ha realizado ***<ins>sin el uso o asistencia de una AI</ins>***
