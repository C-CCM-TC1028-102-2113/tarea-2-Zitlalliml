def main():
    # Escribe el código adecuado para completar el programa
    print('Ingresa el primer número: ')
    x = int(input())

    print('Ingresa el segundo número: ')
    y = int(input())

    print('Ingresa el tercer número: ')
    z = int(input())

    if x<y and x<z:
        print(x)
        if y<z:
            print(y)
            print(z)
        else:
            print(z)
            print(y)
    elif y<x and y<z:
        print(y)
        if x<z:
            print(x)
            print(z)
        else:
            print(z)
            print(x)

    elif z<x and z<y:
        print (z)
        if y<x:
            print(y)
            print(x)
        else:
            print(x)
            print(y)
    pass


if __name__=='__main__':
    main()
