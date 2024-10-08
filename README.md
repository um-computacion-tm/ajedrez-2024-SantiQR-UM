# El juego de ajedrez en 3 días

¡Hola! Este es el repositorio del proyecto de ajedrez de la asignatura de computación de Santiago Quiroga Rivarossa. Legajo: 63170

Este juego de ajedrez es un juego más simplón que el original, pero fue hecho
con mucho amor (y velocidad), así que disfruten.

## :wheelchair:  ¿Cómo jugar?

El juego es un juego de ajedrez de dos jugadores común y corriente, salvo por el hecho de que se le quita que no hay jaque, ni jaque mate, ni reglas especiales como enroque, coronación, etc.

La forma de ganar es que un jugador se coma el rey del otro, o que se le acaben las posibilidades de mover a cualquiera, es decir, tablas. Tienen agregada una funcionalidad para que en cualquier momento puedan empatar la partida.

### Para hacerlo funcionar ejecuten los siguientes comandos desde la __terminal__:

#### 1. Para instalar docker:

```
$ sudo apt install docker
```

#### 2. Para crear la imagen de docker con el juego:

```
$ sudo docker buildx build --no-cache -t ajedrez-santiqr .
```

#### 3. Para ejecutar los tests y el juego:

```
$ sudo docker run -i ajedrez-santiqr
```


## :bar_chart:  Testeos

### Circle CI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-SantiQR-UM/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-SantiQR-UM/tree/main)

### Maintainability with Code Climate
[![Maintainability](https://api.codeclimate.com/v1/badges/71589bfc701ea01df930/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-SantiQR-UM/maintainability)

### Test Coverage with Code Climate
[![Test Coverage](https://api.codeclimate.com/v1/badges/71589bfc701ea01df930/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-SantiQR-UM/test_coverage)
