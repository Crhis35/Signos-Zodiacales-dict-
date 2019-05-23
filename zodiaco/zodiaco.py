signos = { 'aries': ((3,21),(4,20)),'tauro':((4,21),(5,21)),'geminis':((5, 22),(6,21)),'cancer':((6,22),(7,23)),'leo':((7,24),(8,23)),'virgo':((8,24),(9,23)),'libra':((9,24),(10,23)),'escorpio':((10,22),(11,22)),'sagitario':((11,23),(12,21)),'capricornio':((12,22),(1,20)),'acuario':((1,21),(2,19)),'piscis':((2,20),(3,20))}
anio =int(input("Ingrese año: "))
mes =int(input("Ingrese mes: "))
dia =int(input("Ingrese dia: ")) 
datos = (anio,mes,dia)
def signo(signos,datos):
    s = signos.items()
    for v,k in s:
        if mes == k[0][0]:
            if dia >= k[0][1]:
                print(v)
        elif mes == k[1][0]:
            if dia <= k[0][1]:
                print(v)
signo(signos,datos)