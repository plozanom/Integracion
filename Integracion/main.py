from integracion import Integracion

while True:
    print('\tMENU PRINCIPAL\nSelecciona una opcion del menu\n1 - Regla del Trapecio\n2 - Regla de Simpson 1/3\n3 - Regla de Simpson 3/8\n4 - Regla del Trapecio para segmentos desiguales\n0 - Cerrar')
    eleccion = input('\nIntroduzca su eleccion: ')

    if eleccion == '0':
        break
    elif eleccion == '1':
        integracion = Integracion()
        print(integracion.trapecio())
    elif eleccion == '2':
        integracion = Integracion()
        print(integracion.simpson_un_tercio())
    elif eleccion == '3':
        integracion = Integracion()
        print(integracion.simpson_tres_octavos())
    elif eleccion == '4':
        integracion = Integracion()
        print(integracion.segmentos_desiguales())
    else:
        print('\nIntroduzca una opcion valida\n')