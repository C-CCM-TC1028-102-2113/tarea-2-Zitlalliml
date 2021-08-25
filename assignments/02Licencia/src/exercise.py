
def main():
    #Escribe tu código debajo de esta línea
    # programa que lee la edad de una persona y si tiene (s/n) identificación oficial.
    print('Ingresa tu edad: ')
    e = int(input())

    if e >= 18:
        print('¿Tienes identificación oficial? (s/n): ')
        id = str(input())
        if id == 's' or id == 'S':
            print('Trámite de licencia concedido')
        elif id == 'n' or id == 'N':
            print ('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    elif e < 18:
    print('No cumples requisitos')

    pass


if __name__ == '__main__':
    main()
