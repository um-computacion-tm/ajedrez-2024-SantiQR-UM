# Piezas blancas
T = u"\u2656"  # Torre ♖
C = u"\u2658"  # Caballo ♘
A = u"\u2657"  # Alfil ♗
D = u"\u2655"  # Dama ♕
R = u"\u2654"  # Rey ♔
P = u"\u2659"  # Peón ♙

# Piezas negras
t = u"\u265C"  # Torre ♜ 
c = u"\u265E"  # Caballo ♞
a = u"\u265D"  # Alfil ♝
d = u"\u265B"  # Dama ♛
r = u"\u265A"  # Rey ♚
p = u"\u265F"  # Peón ♟

# Espacios
B = u"\u25A1"  # Espacio blanco □
# N = u"\u25A0"  # Espacio negro ■

def main():
    # Tablero con variables de unicode
    tablero = [
        [t, c, a, d, r, a, c, t],
        [p, p, p, p, p, p, p, p],
        [B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B],
        [B, B, B, B, B, B, B, B],
        [P, P, P, P, P, P, P, P],
        [T, C, A, D, R, A, C, T]
    ]

    # Print del tablero
    for fila in tablero:
        for pieza in fila:
            print(pieza, end=' ')
        print()  # Salto de línea

if __name__ == "__main__":
    main()
