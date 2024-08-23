# Changelog

Un resumen de todos los cambios realizados en cada versión de este proyecto.
Muy resumido. Pero impresionante.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.12] - 22-08-2024

### Corregido

- Corregido `test_interfaz` y `test_ajedrez`.

## [1.11] - 21-08-2024

### Corregido

- Corregido `test_tablero` y `test_piezas`.

## [1.10] - 20-08-2024

### Corregido

- Corregido `tablero.py` para pasar test CodeClimate.
- Ahora se puede ganar comiendo al rey.

## [1.9] - 19-08-2024

### Corregido

- Corregido `piezas.py` para pasar test CodeClimate.

## [1.8] - 18-08-2024

### Corregido

- Corregidas ubicaciones de los prints en `interfaz.py`.

## [1.7] - 17-08-2024

### Añadido

- Archivo `test/test_ajedrez.py` creado.
- Más funciones agregadas a `ajedrez.py`.

## [1.6] - 16-08-2024

### Añadido

- Más funciones agregadas a `ajedrez.py`.

## [1.5] - 15-08-2024

### Cambiado

- Funciones agregadas a `ajedrez.py`.

## [1.4] - 14-08-2024

### Añadido

- Archivo `juego/ajedrez.py` creado.

## [1.3] - 13-08-2024

### Añadido

- Archivo `Dockerfile` creado.

### Cambiado

- Readme actualizado.
- Cambiada la forma en la que se acceden a los modulos, ahora es con `ipdb`.
- Para ejecutar interfaz, se debe ejecutar `python -m juego.interfaz`.

## [1.2] - 10-08-2024

### Añadido

- Instrucciones de ejecución en el archivo `README.md`.

### Cambiado

- Dividí la función `obtener_piezas_moviles` en dos funciones y una de ellas la mandé a `interfaz.py`.
- Diseño del `README.md` ligeramente modificado.

### Corregido

- Tests corregidos en base a los cambios realizados.

## [1.1] - 09-08-2024

### Cambiado

- Modifiqué la estructura de los archivos para que se dividan en módulos.

### Corregido

- Archivo `README.md` corregido.
- Archivo `CHANGELOG.md` actualizado y corregido.

### Eliminado

- Quitado atributo `color_casilla` de la clase `Pieza`.

## [1.0] - 08-08-2024 - Día tres y fin :)

### Añadido

- Archivo `code/test_interfaz.py` creado.
- Archivo `code/test_tablero.py` creado.
- Archivo `code/test_piezas.py` creado.
- Archivo `code/test_BD.py` creado.

- Añadidos métodos para verificar victoria.
- Añadidos try y except y captura de errores.
- Hechos los tests para el 100% de cobertura.

### Corregido

- Archivo `code/interfaz.py` corregido.
- Archivo `code/tablero.py` corregido.
- Archivo `code/piezas.py` corregido.
- Archivo `code/BD.py` corregido.

- Documentación de los tests y del código.

### Cambiado

- Modifiqué los nombres de los atributos para que esten rodeados de un doble underscore "__".
- Cambié la forma en la que se crea el tablero, haciendolo menos gráfico y
  más legible usando loops.
- Cambié el nombre de la clase `Casilla` por `Espacio` e hice que la clase
  `Espacio` y `Pieza` hereden de la clase `Casilla`.
- Cambié el funcionamiento interno de diferentes funciones.

### Eliminado

- Archivo `code/ideas.py` eliminado.
- Archivo `ToDo.txt` eliminado.
- Atributo `num` de la clase `Pieza`.

## [0.2] - 07-08-2024 - Día dos

### Añadido

- Archivo `code/interfaz.py` creado.
- Archivo `code/tablero.py` creado.
- Archivo `code/piezas.py` creado.
- Archivo `code/BD.py` creado.

- Añadidas funciones generales para crear clases e instancias.
- Añadidos métodos para obtener piezas movibles, para mover piezas, etc.
- Añadidos métodos para hacer la actualización de la pieza en el tablero.
- Añadido métodos de almacenamiento para guardar y cargar piezas.

## [0.1] - 06-08-2024 - Día uno

### Añadido

- Archivo `CHANGELOG.md` creado.
- Archivo `README.md` creado.
- Archivo `LICENSE` creado.
- Archivo `requirements.txt` creado.
- Archivo `.gitignore` creado.
- Archivo `code/ideas.py` creado.
- Archivo `.coveragerc` creado.
- Archivo `.coverage` creado.
- Archivo `.codeclimate.yml` creado.
- Carpeta `.circleci` añadida.
- Archivo `ToDo.txt` creado.
