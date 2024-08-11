from juego.tablero import *

def main():
    tablero = Tablero()
    
    while True:
        print("\n¿Qué desea hacer?\n")
        print("1. Iniciar el juego")
        print("2. Cerrar")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print()
            color = "blanca"

            while True:
                print("1. Mover pieza (" + color + "s mueven)")
                print("2. Finalizar juego (Empate)")
                accion = input("\nSeleccione una opción: ")

                if accion == "1":

                    # Segunda parte del main:
                    main_2(tablero, color)
                    
                    # Verifico resultado de la partida
                    tablero.verificar_victoria()

                    # Cambio el color si ya movio
                    if color == "blanca":
                        color = "negra"
                    else:
                        color = "blanca"

                elif accion == "2":
                    print("\nJuego finalizado en empate.\n")
                    exit()
                
                else: 
                    print("\nOpción no válida.\n")
                    continue

        elif opcion == "2":
            print("\nCerrando el juego.\n")
            break

        else: 
            print("\nOpción no válida.\n")
            continue


def main_2(self, color):
    
    while True:
        # Acá está la lógica para mover piezas
        self, lista_piezas, lista_instancias, lista_posibilidades = \
            self.obtener_piezas_movibles(color)

        # Hago un print del tablero para mostrarlo antes de dar opciones.
        # Lo puse acá para poder verlo cada vez que se repite el bucle.
        print()
        self.imprimir_tablero()

        # Muestro los nombres de las piezas que se pueden mover, no las instancias.
        print("\nOpciones:")
        
        k = 1
        for pieza in lista_piezas:
            print(f"{k}. {pieza}")
            k += 1
        
        # Pido la opción, si falla, vuelve al bucle.
        try:
            opcion = int(input("\nSeleccione una opción: "))
        
        except ValueError:
            print("\nOpción no válida.\n")
            continue
        
        if opcion > k-1 or opcion == '' or opcion == 0:
            print("\nOpción no válida.\n")
            continue
        
        # Muestro las instancias de la pieza que elegí, ¡solo las que se pueden mover!
        print("\nInstancias de la pieza:")

        count = 1
        elegir = [] # Uso esta lista para guardar los índices de la lista de instancias que se 
                # pueden mover para luego cuando la elija pueda usar esta lista y referenciarla.
        for z in range(len(lista_instancias)):
            
            # lista_piezas[opcion-1] es el nombre de la pieza elegida.
            # lista_instancias[z].__nom__ es el nombre de la instancia de la pieza.
            if lista_piezas[opcion-1] == lista_instancias[z].__nom__:
                
                # Convierto las coordenadas de la pieza a la notación de la tabla.
                a, b = lista_instancias[z].__posicion__
                x, y = self.conversion_coordenadas(a, b) # (Función cerca del final).

                print(f"{count}. {lista_instancias[z].__nom__} {x}{y}")
                elegir.append(z)
                count += 1
        print(f"{count}. Atrás") # Opción extra para volver atrás.

        # Para depurar:
        # print("count: ",count)
        
        # Pido la opción de la instancia, si falla, vuelve al bucle.
        try:
            opcion_2 = int(input("\nSeleccione una pieza: ")) # Para elegir una pieza o salir

        except ValueError:
            print("\nOpción no válida.\n")
            continue

        if opcion_2 > count or opcion_2 == '' or opcion_2 == 0:
            print("\nOpción no válida.\n")
            continue
        
        if opcion_2 == count:
            continue  # Salir para volver a preguntar por la pieza.

        else: 
            # Elijo mover una pieza:
            # Obtengo el índice de la instancia de la pieza de la lista elegir.
            nro_instancia = elegir[opcion_2-1] 
            # Obtengo las posibilidades de esa instancia.
            posibilidades_finales = lista_posibilidades[nro_instancia] 
            # Uso el método 'search' para buscarla (también uso el metodo var() de la pieza).
            seleccion = self.__BD_piezas__.search(lista_instancias[nro_instancia].var())
            
            # Pido la nueva posición.
            nueva_posicion = input("Ingrese la nueva posición (ej. 'a3'): ") 
        
            # Para no enviar valores vacíos.
            if nueva_posicion == '':
                print("\nOpción no válida.\n")
                continue
            
            # Muevo la pieza.
            movimiento = self.mover_pieza(seleccion, nueva_posicion, posibilidades_finales)  
            if movimiento:
                return # Si se completa el movimiento, salgo del bucle.



if __name__ == "__main__":
    main()
