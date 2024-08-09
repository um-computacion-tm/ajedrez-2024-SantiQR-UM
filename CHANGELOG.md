# Changelog

Un resumen de todos los cambios realizados en cada versión de este proyecto.
Muy resumido. Pero impresionante.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0] - 08-08-2024 - Día tres y fin :)

### Añadido

- Archivo `code/test_interfaz.py` creado
- Archivo `code/test_tablero.py` creado
- Archivo `code/test_piezas.py` creado
- Archivo `code/test_BD.py` creado

- Añadidos métodos para verificar victoria.
- Añadidos try y except y captura de errores.
- Hechos los tests para el 100% de cobertura.

### Corregido

- Archivo `code/interfaz.py` corregido
- Archivo `code/tablero.py` corregido
- Archivo `code/piezas.py` corregido
- Archivo `code/BD.py` corregido

- Documentación de los tests y del código.

### Cambiado

- Modifiqué los nombres de los atributos para que esten rodeados de un doble underscore "__"
- Cambié la forma en la que se crea el tablero, haciendolo menos grafico y
  más legible usando loops.
- Cambié el nombre de la clase `Casilla` por `Espacio` e hice que la clase
  `Espacio` y `Pieza` hereden de la clase `Casilla`.
- Cambié el funcionamiento interno de diferentes funciones.

### Eliminado

- Archivo `code/ideas.py` eliminado
- Archivo `ToDo.txt` eliminado

## [0.2] - 07-08-2024 - Día dos

### Añadido

- Archivo `code/interfaz.py` creado
- Archivo `code/tablero.py` creado
- Archivo `code/piezas.py` creado
- Archivo `code/BD.py` creado

- Añadidas funciones generales para crear clases e instancias.
- Añadidos métodos para obtener piezas movibles, para mover piezas, etc.
- Añadidos métodos para hacer la actualización de la pieza en el tablero.
- Añadido métodos de almacenamiento para guardar y cargar piezas.

## [0.1] - 06-08-2024 - Día uno

### Añadido

- Archivo `CHANGELOG.md` creado
- Archivo `README.md` creado
- Archivo `LICENSE` creado
- Archivo `requirements.txt` creado
- Archivo `.gitignore` creado
- Archivo `code/ideas.py` creado
- Archivo `.coveragerc` creado
- Archivo `.coverage` creado
- Archivo `.codeclimate.yml` creado
- Carpeta `.circleci` añadida
- Archivo `ToDo.txt` creado