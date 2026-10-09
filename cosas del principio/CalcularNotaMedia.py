def notaMedia(nota1, nota2):
    media=(nota1+nota2)/2
    return media
for i in range(6):
    nota=float(input())
    notas=[nota]
for i in range(3):
    mediaParcial=notaMedia(notas[1],notas[i+1])
    mediaFinal=mediaFinal+mediaParcial
print(f"la media final es {mediaFinal}")
#no funciona, que le den por el puto culo