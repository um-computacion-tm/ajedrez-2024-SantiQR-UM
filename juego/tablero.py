from juego.piezas import *
from juego.BD import *

class Tablero:
    def __init__(self):
        self.__tablero__, self.__BD_piezas__, self.__BD_espacios__ = self.crear_tablero_inicial()

    # Método para crear el tablero inicial.
    def crear_tablero_inicial(self):
        # Creo las piezas y los espacios:

        #Piezas blancas.
        info_piezas = [
        ("P1" , "blanca", (1,7), u"\u2659", "Peon"), # ♙
        ("P2" , "blanca", (2,7), u"\u2659", "Peon"), # ♙
        ("P3" , "blanca", (3,7), u"\u2659", "Peon"), # ♙
        ("P4" , "blanca", (4,7), u"\u2659", "Peon"), # ♙
        ("P5" , "blanca", (5,7), u"\u2659", "Peon"), # ♙
        ("P6" , "blanca", (6,7), u"\u2659", "Peon"), # ♙
        ("P7" , "blanca", (7,7), u"\u2659", "Peon"), # ♙
        ("P8" , "blanca", (8,7), u"\u2659", "Peon"), # ♙
        ("C1" , "blanca", (2,8), u"\u2658", "Caballo"), # ♘
        ("C2" , "blanca", (7,8), u"\u2658", "Caballo"), # ♘
        ("A1" , "blanca", (3,8), u"\u2657", "Alfil"), # ♗
        ("A2" , "blanca", (6,8), u"\u2657", "Alfil"), # ♗
        ("T1" , "blanca", (1,8), u"\u2656", "Torre"), # ♖
        ("T2" , "blanca", (8,8), u"\u2656", "Torre"), # ♖
        ("D1" , "blanca", (4,8), u"\u2655", "Dama"), # ♕
        ("R1" , "blanca", (5,8), u"\u2654", "Rey"), # ♔
        
        # Piezas negras.
        ("p1" , "negra", (1,2), u"\u265F", "Peon"), # ♟
        ("p2" , "negra", (2,2), u"\u265F", "Peon"), # ♟
        ("p3" , "negra", (3,2), u"\u265F", "Peon"), # ♟                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("p4" , "negra", (4,2), u"\u265F", "Peon"), # ♟
        ("p5" , "negra", (5,2), u"\u265F", "Peon"), # ♟
        ("p6" , "negra", (6,2), u"\u265F", "Peon"), # ♟
        ("p7" , "negra", (7,2), u"\u265F", "Peon"), # ♟
        ("p8" , "negra", (8,2), u"\u265F", "Peon"), # ♟
        ("c1" , "negra", (2,1), u"\u265E", "Caballo"), # ♞
        ("c2" , "negra", (7,1), u"\u265E", "Caballo"), # ♞                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        ("a1" , "negra", (3,1), u"\u265D", "Alfil"), # ♝
        ("a2" , "negra", (6,1), u"\u265D", "Alfil"), # ♝                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
        ("t1" , "negra", (1,1), u"\u265C", "Torre"), # ♜
        ("t2" , "negra", (8,1), u"\u265C", "Torre"), # ♜
        ("d1" , "negra", (4,1), u"\u265B", "Dama"), # ♛
        ("r1" , "negra", (5,1), u"\u265A", "Rey") # ♚
        ]
        
        # Espacios.
        info_espacios = [
        ("B" , "blanca", u"\u25A1"), # Espacio blanco □
        ("N" , "negra", u"\u25A0") # Espacio negro ■
        ]
        
        # Creo las BDs.
        BD_piezas = BD()
        BD_espacios = BD()
        
        # Añado las piezas a la BD.
        # Quite los atributos 'num' y 'color_casilla' de las piezas.
        for var, color, posicion, s, nom in info_piezas:
            
            # Uso globals() para obtener la clase a partir del nombre (string) de la pieza.
            clase_pieza = globals().get(nom)
            
            if clase_pieza:
                pieza = clase_pieza(var, color, posicion, s, nom)
                BD_piezas.add(pieza)

            # Para depurar:
            # else:
            #     print(f"No se encontró la clase: {nom}")
        
        # Añado los espacios a la BD.
        for var, color, s in info_espacios:
            espacio = Espacio(var, color, s)
            BD_espacios.add(espacio)
        
        # Creo el tablero vacío.
        tablero = [[" " for _ in range(10)] for _ in range(10)]
        
        # Coloco las coordenadas del tablero.
        letras = [" ", "a", "b", "c", "d", "e", "f", "g", "h", " "]
        for i in range(10):
            # Las letras:
            tablero[0][i] = tablero[9][i] = letras[i]
            # Las números:
            tablero[i][0] = tablero[i][9] = str(9 - i) if i > 0 and i < 9 else " "
        
        # Coloco las piezas en el tablero según su posición.
        for pieza in BD_piezas.__base_datos__.values():
            x, y = pieza.__posicion__
            # Importante: x e y van invertidos porque el tablero es una lista de listas.
            tablero[y][x] = pieza
        
        # Coloco los espacios en las casillas vacías.
        for y in range(3, 7):
            for x in range(1, 9):
                # Acá lo mismo, ¡x e y invertidos!
                tablero[y][x] = BD_espacios.search('B' if (x + y) % 2 == 0 else 'N')
        
        # Devuelvo el tablero y las BDs para la interfaz.
        return tablero, BD_piezas, BD_espacios
    
    # Método para convertir el tablero en un string.
    def __str__(self):
        string_tablero = "\n"
        for fila in self.__tablero__:
            for casilla in fila:
                # Si es una pieza o una casilla, muestro el símbolo.
                if isinstance(casilla, Pieza):
                    string_tablero += (str(casilla.__s__) + (" "))
                elif isinstance(casilla, Espacio):
                    string_tablero += (str(casilla.__s__) + (" "))
                else:
                    string_tablero += (str(casilla) + (" "))
            string_tablero += ("\n")
        return string_tablero
    
    # Método para obtener las piezas movibles.
    # Llama a submétodos.
    def obtener_piezas_movibles(self, color):
        # Devuelvo una lista de nombres de piezas que pueden moverse para el color dado.
        # Luego una lista de las instancias de esas piezas.
        # Y después pido la posición a la que se quiere avanzar.

        lista_piezas = []  # Lista para los nombres las piezas que voy a mostrar.
        lista_instancias = []  # Lista para las instancias de las piezas que voy a mostrar.
        lista_posibilidades = []  # Lista para las posibilidades de cada una de las piezas.

        # Para las 16 piezas del jugador:
        piezas = [
            (1, 8, "P", "p"),  # Peones
            (9, 10, "C", "c"),  # Caballos
            (11, 12, "A", "a"),  # Alfiles
            (13, 14, "T", "t"),  # Torres
            (15, 15, "D", "d"),  # Dama
            (16, 16, "R", "r")  # Rey
        ]

        # Hago la iteración para recorrer todas las piezas.
        for i in range(1, 17):
            # Mando a buscar la letra y la cantidad de la pieza según su rango.
            letra, cant = self.obtener_letra_y_cantidad(piezas, i, color)

            # Mando a buscar las instancias de las piezas.
            resultado, movible, posibilidades = self.instancias_piezas\
                                                (self.__BD_piezas__, letra, cant)

            # Agrego las piezas a las listas correspondientes.
            if movible:
                if resultado.__nom__ not in lista_piezas:
                    lista_piezas.append(resultado.__nom__)
                if resultado not in lista_instancias:
                    lista_instancias.append(resultado)
                    lista_posibilidades.append(posibilidades)

        # Devuelvo el tablero, las listas de piezas, instancias y posibilidades.
        return self, lista_piezas, lista_instancias, lista_posibilidades

    # Método para obtener la letra y la cantidad de la pieza según su rango.
    def obtener_letra_y_cantidad(self, piezas, i, color):
        for inicio, fin, letra_blanca, letra_negra in piezas:
            if inicio <= i <= fin:
                cant = i - inicio + 1
                letra = letra_blanca if color == "blanca" else letra_negra
                return letra, cant

    # Método para obtener las instancias movibles de las piezas.
    def instancias_piezas(self, BD_piezas, letra, i):
        
        # Uso el método 'search' para repasar la BD de piezas, donde están las instancias, 
        # entregando el valor var (usando la letra más el número de pieza).
        pieza = BD_piezas.search(letra + str(i))
        # Reviso si se puede mover.
        movible, posibilidades = self.movible(pieza)  
        
        # Devuelvo la instancia de la pieza, si es movible (bool) y las posibilidades.
        return pieza, movible, posibilidades
        
    # Método principal para verificar si una pieza puede moverse.
    # Este llama a submétodos.
    def movible(self, pieza):
        # Me fijo si la pieza está viva y obtengo los movimientos posibles.
        # Luego, filtro los movimientos posibles según las reglas del juego.
        # Finalmente, verifico si el camino entre el origen y el destino está libre.
        viva, posibilidades = self.verificar_viva_y_movimientos(pieza)
        
        if not viva:
            return False, []
        
        posibilidades_checked = self.filtrar_movimientos(pieza, posibilidades)
        posibilidades_double_checked = self.verificar_camino_libre(pieza, posibilidades_checked)
        
        return bool(posibilidades_double_checked), posibilidades_double_checked

    # Parte 1 del método movible.
    def verificar_viva_y_movimientos(self, pieza):
        # Me fijo si la pieza está viva. Si no lo está, retorno False y una lista vacía.
        # Si está viva, retorno True y la lista de movimientos posibles de la pieza.
        if not pieza.__vive__:
            return False, []
        
        return True, pieza.movimientos_posibles()

    # Parte 2 del método movible.
    def filtrar_movimientos(self, pieza, posibilidades):
    # Filtro los movimientos posibles según las reglas del juego.
        posibilidades_checked = []

        for posicion in posibilidades:
            x, y = posicion
            
            # Aunque ya está hecha la verificación en el método 'movimientos_posibles', lo hago
            # de nuevo por si acaso.
            if not (1 <= x <= 8 and 1 <= y <= 8):
                continue

            casilla = self.__tablero__[y][x]

            # Primero, si la pieza no es peón:
            if not isinstance(pieza, Peon):
                # Si la casilla está vacía.
                if isinstance(casilla, Espacio):
                    posibilidades_checked.append(posicion)
                # Si la casilla tiene una pieza de distinto color.
                elif isinstance(casilla, Pieza) and casilla.__color__ != pieza.__color__:
                    posibilidades_checked.append(posicion)
            # Si la pieza es peón:
            else:
                # Lo mando a verificar según el tipo de movimiento.
                if self.filtrar_movimiento_vertical_peon(pieza, x, y, casilla):
                    posibilidades_checked.append(posicion)
                elif self.filtrar_movimiento_diagonal_peon(pieza, x, y, casilla):
                    posibilidades_checked.append(posicion)

        return posibilidades_checked

    # Parte 1 del método filtrar_movimientos.
    def filtrar_movimiento_vertical_peon(self, peon, x, y, casilla):
        # Verifica si el movimiento vertical del peón es válido.
        # Primero vé si está en las posibilidades y después si está vacío.
        flag = True
        if abs(peon.__posicion__[0] - x) != 0:
            flag = False
        if abs(peon.__posicion__[1] - y) not in [1, 2]:
            flag = False
        if not isinstance(casilla, Espacio):
            flag = False
        return flag

    # Parte 2 del método filtrar_movimientos.
    def filtrar_movimiento_diagonal_peon(self, peon, x, y, casilla):
        # Verifica si el movimiento diagonal del peón es válido.
        # Si está en las posibilidades y si hay una pieza de otro color.
        flag = True
        if abs(peon.__posicion__[0] - x) != 1:
            flag = False
        if abs(peon.__posicion__[1] - y) != 1:
            flag = False
        if not isinstance(casilla, Pieza):
            flag = False
        if casilla.__color__ == peon.__color__:
            flag = False
        return flag

    # Parte 3 del método movible.
    def verificar_camino_libre(self, pieza, posibilidades_checked):
        # Verifico si el camino entre el origen y el destino está libre.
        posibilidades_double_checked = []

        # Por cada una de las posiciones:
        for posicion in posibilidades_checked:
            # Mando a ver en la siguiente función.
            if self.es_camino_libre(pieza, posicion):
                posibilidades_double_checked.append(posicion)

        return posibilidades_double_checked

    # Parte 1 del método verificar_camino_libre.
    def es_camino_libre(self, pieza, posicion):
        # Verifica si el camino está libre para una pieza específica.
        # Si es caballo, directamente lo devuelve.
        if isinstance(pieza, Caballo):
            return True

        # Define inicio y final.
        x_start, y_start = pieza.__posicion__
        x_end, y_end = posicion

        # Define las direcciónes.
        dx = self.calcular_direccion(x_start, x_end)
        dy = self.calcular_direccion(y_start, y_end)

        # Lo manda a verificar.
        parametros = (x_start, y_start, x_end, y_end, dx, dy)
        return self.verificar_casillas_libres(parametros)

    # Parte 2 del método verificar_camino_libre.
    def calcular_direccion(self, start, end):
        # Calcula la dirección del movimiento.
        if end == start:
            return 0
        return 1 if end > start else -1

    # Parte 3 del método verificar_camino_libre.
    def verificar_casillas_libres(self, parametros):
        # Verifica si todas las casillas en el camino están libres.
        x_start, y_start, x_end, y_end, dx, dy = parametros

        # Define hacia adonde es el avance.
        x_avance, y_avance = x_start + dx, y_start + dy

        # Mientras no se choque con nada se sigue moviendo por el camino.
        while x_avance != x_end or y_avance != y_end:
            # Si hay algo devuelve False.
            if isinstance(self.__tablero__[y_avance][x_avance], Pieza):
                return False
            x_avance += dx
            y_avance += dy

        return True             

    # Este es el método que se llama para mover una pieza.
    def mover_pieza(self, pieza, nueva_posicion_str, nueva_posicion_int, \
                    vieja_posicion, posibilidades):
        # Acá está la logica para mover la pieza.
        
        # Obtengo la casilla destino.
        x, y = nueva_posicion_int
        casilla_destino = self.__tablero__[y][x]

        x_vieja, y_vieja = vieja_posicion
        
        # Verifico si hay una pieza en la casilla destino.
        # Si casilla es una instancia pieza digo que la capturó.
        string_movimiento = ""
        if isinstance(casilla_destino, Pieza):
            string_movimiento += f"\nMovimiento realizado: {pieza.__nom__} {pieza.__color__} {x_vieja}{y_vieja}"
            string_movimiento += f" ha capturado {casilla_destino.__nom__} {casilla_destino.__color__} en {nueva_posicion_str}\n"
        
            # Actualizo el estado de la pieza capturada.
            casilla_destino.__vive__ = False
        # Si es un espacio vacío.
        else:
            string_movimiento += f"\nMovimiento realizado: {pieza.__nom__} {pieza.__color__} {x_vieja}{y_vieja}"
            string_movimiento += f" se ha movido a {nueva_posicion_str}\n"

        # Actualizo el tablero con la nueva posición de la pieza:
        # Saco las viejas coordenadas.
        x_actual, y_actual = pieza.__posicion__
        # Restauro la casilla original con el espacio correspondiente.
        self.__tablero__[y_actual][x_actual] = self.__BD_espacios__.search\
                                               ('B' if (x_actual + y_actual) % 2 == 0 else 'N')
        # Coloco la pieza en la nueva posición.
        self.__tablero__[y][x] = pieza  

        # Actualizo los atributos de la pieza con la nueva posición de la pieza.
        pieza.mover((x, y))

        return string_movimiento # Devuelvo que se completó el movimiento y el string para printear.

    # Este es el método principal para verificar si el juego ha terminado.
    def verificar_victoria(self):
        # Verifico si el juego ha terminado.

        # Para una victoria por piezas:
        string_victoria, piezas_blancas_vivas, piezas_negras_vivas = self.victoria_por_piezas()

        if string_victoria != "":
            return string_victoria

        # Para una victoria por movimientos:
        # Reviso si hay al menos un movimiento posible para cada jugador.
        movimientos_blancas = any(self.movible(pieza)[0] for pieza in piezas_blancas_vivas)
        movimientos_negras = any(self.movible(pieza)[0] for pieza in piezas_negras_vivas)

        if not movimientos_blancas and not movimientos_negras:
            string_victoria += "¡Empate por movimientos!"

        elif not movimientos_blancas:
            string_victoria += "¡El jugador negro ha ganado por movimientos!"

        elif not movimientos_negras:
            string_victoria += "¡El jugador blanco ha ganado por movimientos!"

        return string_victoria # Devuelvo el string de victoria, si está vacío no pasó nada.
    
    # Submétodo de verificar_victoria
    def victoria_por_piezas(self):
        # Reviso si el rey de cada jugador sigue vivo.
        rey_blanco_vivo = any(pieza.__nom__ == "Rey" and pieza.__color__ == 'blanca' 
                    and pieza.__vive__ for pieza in self.__BD_piezas__.__base_datos__.values())
        
        rey_negro_vivo = any(pieza.__nom__ == "Rey" and pieza.__color__ == 'negra'
                    and pieza.__vive__ for pieza in self.__BD_piezas__.__base_datos__.values())

        # Creo el string vacío.
        string_victoria = ""

        if not rey_blanco_vivo:
            string_victoria += "¡El jugador negro ha ganado por capturar al rey blanco!"

        if not rey_negro_vivo:
            string_victoria += "¡El jugador blanco ha ganado por capturar al rey negro!"
        
        # Reviso cada una de las piezas vivas de cada jugador.
        piezas_blancas_vivas = [pieza for pieza in self.__BD_piezas__.__base_datos__.values() if \
                                pieza.__color__ == 'blanca' and pieza.__vive__]
        piezas_negras_vivas = [pieza for pieza in self.__BD_piezas__.__base_datos__.values() if \
                                pieza.__color__ == 'negra' and pieza.__vive__]

        # Devuelvo el mensaje de victoria y las piezas vivas de cada jugador.
        return string_victoria, piezas_blancas_vivas, piezas_negras_vivas