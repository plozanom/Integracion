from integracion import Integracion
from utils import clear

while True:
    clear()
    print('\tMENU PRINCIPAL\nSelecciona una opcion del menu\n1 - Regla del Trapecio\n2 - Regla de Simpson 1/3\n3 - Regla de Simpson 3/8\n4 - Regla del Trapecio para segmentos desiguales\n0 - Cerrar')
    eleccion = input('\nIntroduzca su eleccion: ')
    clear()

    if eleccion == '0':
        break
    elif eleccion == '1':
        integracion = Integracion()
        print(integracion.trapecio())
        input('Presiona ENTER para volver...')
    elif eleccion == '2':
        integracion = Integracion()
        print(integracion.simpson_un_tercio())
        input('Presiona ENTER para volver...')
    elif eleccion == '3':
        integracion = Integracion()
        print(integracion.simpson_tres_octavos())
        input('Presiona ENTER para volver...')
    elif eleccion == '4':
        integracion = Integracion()
        print(integracion.segmentos_desiguales())
        input('Presiona ENTER para volver...')
    else:
        print('\nIntroduzca una opcion valida\n')
        input('Presiona ENTER para volver...')