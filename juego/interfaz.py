from juego.ajedrez import Ajedrez


# Primero creo la clase juego que va a manejar la comunicacion principal con la fachada.
class Juego:
    def __init__(self):
        # Inicializo una instancia de la clase Ajedrez.
        self.__ajedrez__ = Ajedrez()


    def main(self):
        # Este es el bucle principal del juego.
        while True:
            print("\n¿Qué desea hacer?")
            print("1. Iniciar el juego")
            print("2. Cerrar")
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                # Acá reinicio el juego para que cuando se elija terminar en empate se reinicie
                # el tablero.
                self.__init__()
                self.iniciar_juego()

            elif opcion == "2":
                print("\nCerrando el juego.\n")
                exit()

            else:
                print("\nOpción no válida.\n")
                continue


    def iniciar_juego(self):
        # Acá hice el bucle secundario para manejar el juego de ajedrez ya inicializado.
        while True:

            # Muestro el tablero y las opciones.
            InterfazDeUsuario.imprimir_tablero(self.__ajedrez__)

            print("\n1. Mover pieza (" + self.__ajedrez__.__turno__ + "s mueven)")
            print("2. Finalizar juego (Empate)")
            accion = input("\nSeleccione una opción: ")

            if accion == "1":
                # Mando a buscar las opciones de selección de piezas.
                self.__ajedrez__ = Ajedrez.jugar(self.__ajedrez__)
                
                # Salto a la funcion para mostrarlas.
                self.opciones_1()
                
                # Verifico si el juego terminó.
                string_fin = self.__ajedrez__.verificar_fin()
                if string_fin != "":
                    print(string_fin)
                    InterfazDeUsuario.imprimir_tablero(self.__ajedrez__)
                    break
                
                # Si no, cambio el turno.
                self.__ajedrez__.cambiar_turno()

            elif accion == "2":
                print("\nJuego finalizado en empate.\n")
                break

            else:
                print("\nOpción no válida.\n")
                continue


    def opciones_1(self):
        # Muestro las opciones de selección de piezas.
        while True:

            # Muestro el tablero para siempre poder estarlo viendo.
            InterfazDeUsuario.imprimir_tablero(self.__ajedrez__)

            # Muestro las opciones de piezas.
            print("\nOpciones:")
            k = 1
            for pieza in self.__ajedrez__.__lista_piezas__:
                print(f"{k}. {pieza}")
                k += 1

            opcion = input("\nSeleccione una opción: ")
            # Verifico si la opción ingresada es válida.
            opcion, isOK = InterfazDeUsuario.chequear_opcion(opcion, k-1)

            if not isOK:
                continue
            
            # Salto a la función para mostrar las instancias de la pieza seleccionada.
            resultado = self.opciones_2(opcion)

            # Si el movimiento se realizó vuelvo.
            if resultado:
                return

    def opciones_2(self, opcion):
        # Muestro las opciones de selección de instancias de piezas.

        # Muestro el tablero otra vez.
        InterfazDeUsuario.imprimir_tablero(self.__ajedrez__)
        
        # Muestro las instancias de la pieza seleccionada.
        print("\nInstancias de la pieza:")
        count = 1
        elegir = []
        for z in range(len(self.__ajedrez__.__lista_instancias__)):

            # Si la pieza seleccionada es igual a la pieza en la lista de instancias, la muestro.
            if self.__ajedrez__.__lista_piezas__[opcion-1] == \
                self.__ajedrez__.__lista_instancias__[z].__nom__:

                # Convierto las coordenadas de formato numérico a formato de ajedrez.
                x, y = InterfazDeUsuario.conversion_coordenadas\
                    (self.__ajedrez__.__lista_instancias__[z].__posicion__)
                
                # Muestro las instancias de la pieza.
                print(f"{count}. {self.__ajedrez__.__lista_instancias__[z].__nom__} {x}{y}")

                # Guardo las instancias en una lista para poder seleccionarlas.
                elegir.append(z)
                count += 1
        # Muestro una opción para volver.
        print(f"{count}. Atrás")

        opcion_2 = input("\nSeleccione una pieza: ")
        # Verifico si la opción ingresada es válida.
        opcion_2, isOK = InterfazDeUsuario.chequear_opcion(opcion_2, count)
        if not isOK:
            return False
        
        # Si se elige la opción de atrás, vuelvo.
        if opcion_2 == count:
            return False
        
        # Si no, pido la nueva posición.
        else:
            # Elijo la instancia de la pieza, usando la lista elegir.
            nro_instancia = elegir[opcion_2-1]

            # Busco las posibilidades finales de movimiento de la pieza.
            posibilidades_finales = self.__ajedrez__.__lista_posibilidades__[nro_instancia]

            # Busco la instancia de la pieza seleccionada.
            seleccion = self.__ajedrez__.__tablero__.__BD_piezas__.search(\
                self.__ajedrez__.__lista_instancias__[nro_instancia].var())
            
            # Pido la nueva posición.
            nueva_posicion = input("Ingrese la nueva posición (ej. 'a3'): ")

            # Salto a la función para mover la pieza.
            resultado = self.mover(seleccion, nueva_posicion, posibilidades_finales)

            # Si el movimiento se realizó vuelvo.
            if resultado:
                return True


    def mover(self, seleccion, nueva_posicion_str, posibilidades_finales):
        # Muevo una pieza a una nueva posición.

        # Convierto las coordenadas de formato de ajedrez a formato numérico.
        posicion = InterfazDeUsuario.conversion_coordenadas_inversa(nueva_posicion_str)
        # Verifico si la opción ingresada es válida.
        if not posicion:
            return False
        
        nueva_posicion_int = posicion

        # Convierto las coordenadas de formato numérico a formato de ajedrez.
        posicion = InterfazDeUsuario.conversion_coordenadas(seleccion.__posicion__)
        # Verifico si la opción ingresada es válida.
        if not posicion:
            return False
        
        vieja_posicion = posicion

        # Verifico si la nueva posición es válida.
        if nueva_posicion_int not in posibilidades_finales:
            print("\nEste movimiento no es posible.\n")
            return False
        
        # Muevo la pieza.
        self.__ajedrez__, string_movimiento = self.__ajedrez__.mover_ajedrez(seleccion, \
            nueva_posicion_str, nueva_posicion_int, vieja_posicion, posibilidades_finales)
        print(string_movimiento)

        # Devuelvo que se movió.
        return True


# Ahora creo las funciones especiales que va a tener la interfaz de usuario.
class InterfazDeUsuario:
    # EL método staticmethod sirve para poder llamar al método sin tener que instanciar la clase.
    @staticmethod
    def imprimir_tablero(ajedrez):
        # Muestro el tablero de ajedrez.
        ajedrez.imprimir_tablero_ajedrez()


    @staticmethod
    def chequear_opcion(opcion, k):
        # Verifico si la opción ingresada es válida.
        try:
            # Convierto la opción a entero.
            opcion = int(opcion)

            # Reviso que no se pase del limite ni sea 0.
            if opcion > k or opcion == 0:
                print("\nOpción no válida.\n")
                return opcion, False
            
            # Si todo está bien, devuelvo la opción y True.
            return opcion, True
        
        # Si no se puede convertir a entero, devuelvo False.
        except ValueError:
            print("\nOpción no válida.\n")
            return opcion, False


    @staticmethod
    def conversion_coordenadas(posicion):
        # Convierto coordenadas de formato numérico a formato de ajedrez.
        columnas = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
        filas = {8: '1', 7: '2', 6: '3', 5: '4', 4: '5', 3: '6', 2: '7', 1: '8'}
        
        # Lo intento pasar.
        try:
            nueva_columna, nueva_fila = posicion
            x = columnas[nueva_columna]
            y = filas[nueva_fila]

        # Si no se puede convertir, devuelvo False.
        except (KeyError, ValueError, TypeError, IndexError):
            print("\nValores mal ingresados.\n")
            return False
        
        # Si pude, lo devuelvo.
        return x, y


    @staticmethod
    def conversion_coordenadas_inversa(posicion):
        # Convierto coordenadas de formato de ajedrez a formato numérico.
        columnas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        filas = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1}

        # Lo intento pasar.
        try:
            nueva_columna, nueva_fila = posicion[0], posicion[1]
            x = columnas[nueva_columna]
            y = filas[nueva_fila]

        # Si no se puede convertir, devuelvo False.
        except (KeyError, ValueError, TypeError, IndexError):
            print("\nValores mal ingresados.\n")
            return False
        
        # Si pude, lo devuelvo.
        return x, y


# Ejecuto main.
if __name__ == "__main__":
    juego = Juego()
    juego.main()