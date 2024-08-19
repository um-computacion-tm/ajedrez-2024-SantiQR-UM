# El juego de ajedrez en 3 días

¡Hola! Este es el repositorio del proyecto de ajedrez de la asignatura de computación de Santiago Quiroga Rivarossa. Legajo: 63170

Este juego de ajedrez es un juego más simplón que el original, pero fue hecho
con mucho amor (y velocidad), así que disfruten.

## :wheelchair:  ¿Cómo jugar?

El juego se juega de a 2 jugadores, a cada uno se le asigna movimientos, y...
Dudo que no sepan jugar ajedrez, y si no saben leeanse unas reglas, no estas, no
tengo ganas de hacerlas, je.

Voy a decirles lo básico, los movimientos de las fichas son las mismas que en original, pero se le agrega... No... Se le quita que no hay jaque, ni jaque mate, ni reglas especiales como enroque, coronación, bla bla bla... Que juego más aburrido... Me estoy arrepintiendo...

Bueno, la forma de ganar es que un jugador se coma el rey del otro, o que se le acaben las posibilidades de mover a cualquiera, es decir, tablas. (Re largo...), así que les agregue una funcionalidad para que en cualquier momento lo puedan empatar y decidir quien ganó haciendo piedra, papel o tijera... No me jodan.

### Para hacerlo funcionar:

#### 1. Instalen `requirements.txt`.

```
pip install -r requirements.txt
```

#### 2. Ejecuten los siguientes comandos desde la __terminal__:

```
docker buildx build -t ajedrez-santiqr .
docker run -i ajedrez-santiqr
```

#### 3. Necesitan _Python 3.x_.

## :black_nib:  Nota del autor

Sí, soy un comilón... Era un proyecto para hacer en 3 meses, pero no tenía nada que hacer así que lo hice en 3 días... 

De todas formas, espero que lo disfruten. ¿Suerte?, supongo... :smiley:


## :bar_chart:  Testeos

### Circle CI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-SantiQR-UM/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-SantiQR-UM/tree/main)

### Maintainability with Code Climate
[![Maintainability](https://api.codeclimate.com/v1/badges/71589bfc701ea01df930/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-SantiQR-UM/maintainability)

### Test Coverage with Code Climate
[![Test Coverage](https://api.codeclimate.com/v1/badges/71589bfc701ea01df930/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-SantiQR-UM/test_coverage)