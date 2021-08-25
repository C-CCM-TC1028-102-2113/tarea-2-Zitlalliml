def main():
    #escribe tu código abajo de esta línea
    # programa que muestre el mayor de 3 números enteros x, y, z 
    # proporcionados por el usuario.
    print('Ingresa el primer número: ')
    x = int(input())

    print('Ingresa el segundo número: ')
    y = int(input())

    print('Ingresa el tercer número: ')
    z = int(input())

    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    elif z>x and z>y:
        print(z)
        
    pytest --tb=short
    pass


if __name__=='__main__':
    main()
