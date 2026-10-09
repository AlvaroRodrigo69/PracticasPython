def subrutina():
    def sub_subutina():
        nonlocal a
        print(a)
        a=1
        return
    #nonlocal no puede acceder de ninguna manera posible al programa principal ni siquiera si esta de un unico nivel a otro ¿por qué?
    #ni puta idea, patata, huevos con aceite , usa el global si quieres hacerlo
    #o pasala por parametro como un ser hunmano normal y razonable que nos es un puto retrasado
    a=3
    sub_subutina()
    print(a)
    return
a=5
subrutina()
print(a)