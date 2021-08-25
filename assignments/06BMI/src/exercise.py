def main():
    #escribe tu código abajo de esta línea
    #programa que calcule el IMC (Índice de Masa Corporal) de una persona, 
    #el cual se utiliza para determinar si la proporción de peso y altura es adecuada. 
    p = float(input('Peso en kg: '))
    h = float(input('Altura en m: '))

    if p> 0 and h>0:
        i = p / (h**2)
        if i<20:
            print('PESO BAJO')
        elif i>=20 and i<25:
            print('NORMAL')
        elif i>=25 and i<30:
            print('SOBREPESO')
        elif i>=30 and i<40:
            print('OBESIDAD')
        elif i>=40:
            print('	OBESIDAD MORBIDA')
    else:
        print('Revisa tus datos, alguno de ellos es erróneo.')
    pass
if __name__=='__main__':
    main()
