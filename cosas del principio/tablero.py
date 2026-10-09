import random
def visualizarFila(filaActual, tablero):
    for i in range(15):
        print(tablero[filaActual][i], end=" ")

def visualizarTablero(arr):
    for i in range(10):
        visualizarFila(i,arr)
        print()

filas=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]#cada fila a de tener 15 elementos, 1 por columna
mar=[]
for i in range(10):
    mar.append(filas.copy())
x=random.randint(0,14)
y=random.randint(0,9)
print(x, y)
mar[y][x]=1
visualizarTablero(mar)