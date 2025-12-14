espacio= 0

def reiniciar(posicion_x):
    global espacio
    espacio = posicion_x

def adelante(pasos_adelante):
    global espacio
    print (espacio * " " + "-" * pasos_adelante + ">")
    espacio = espacio + pasos_adelante

def abajo (pasos_abajo):
    for i in range (pasos_abajo):
                camino_abajo = " " * espacio + "|\n"
                print(camino_abajo, end='')
    print(" " * espacio + "V")
