    # Mini Mini 🐢

    Un paquete utilitario de Python simple para dibujar una escalera la cual una tortuga puede ir hacia adelante y bajar escalones hecho con texto.

    ## 🐢 Instalación

    Este paquete no está publicado en PyPI (por ahora), pero puede instalarlo localmente clonando el repositorio:

    ```bash
    git clone https://github.com/Karol-perez-castaneda/mini_tortuga_task.git
    cd mini_tortuga_task
    pip install .
    ```

    ## ✨ Uso

    Una vez instalado, importe las funciones directamente desde el paquete `mini_tortuga`:

    ```python
    from mini_tortuga import adelante, abajo, reiniciar
    import drawer_logic

    # Avanzar hacia adelante
    adelante (10)
    # Salida: 
    ---------->

    # Avanzar hacia abajo
    abajo (5)
    # Salida:
    |
    |
    |
    |
    |
    V

    # Avanzar hacia adelante y abajo al mismo tiempo
    adelante (10)
    abajo (5)
    # Salida
    ---------->
              |
              |
              |
              |
              |
              V

    # Reiniciar para reiniciar la posicion de la tortuga
    reiniciar (0)
    
    ```