from tablero import Tablero

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
                    # Acá está la lógica para mover piezas
                    tablero.obtener_piezas_movibles(tablero.__BD_piezas__, color)
                    
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

if __name__ == "__main__":
    main()
