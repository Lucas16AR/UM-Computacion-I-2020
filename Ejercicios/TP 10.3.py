from Humanos import Humano, HumanoGuerrero, HumanoArquero
from Orcos import Orco, OrcoGuerrero, OrcoLancero

salida = False
while not salida:
    print("RAZAS")
    print("1: Humanos")
    print("2: Orcos")
    print("3: Salir")
    respuesta = int(input("Ingrese una opcion: "))
    if respuesta == 1:
        cantidad_humanos_guerreros = 0
        cantidad_humanos_arqueros = 0
        saldo = 1000
        salida_humanos = False
        while not salida_humanos:
            print("Saldo restante", saldo)
            print("HUMANOS")
            print("1: Guerrero, $150")
            print("2: Arquero, $100")
            print("3: Salir")
            respuesta_humanos = int(input("Ingrese una opcion: "))
            if respuesta_humanos == 1:
                if (saldo - 150) < 0:
                    print("Te has quedado sin saldo")
                    print("Tu ejercito esta formado por",  cantidad_humanos_guerreros, "guerreros", cantidad_humanos_arqueros, "arqueros")
                    salida_humanos = True
                    salida = True
                else:
                    print("Has comprado al guerrero")
                    saldo = saldo - 150
                    cantidad_humanos_guerreros = cantidad_humanos_guerreros + 1
            if respuesta_humanos == 2:
                if (saldo - 100) < 0:
                    print("Te has quedado sin saldo")
                    print("Tu ejercito esta formado por",  cantidad_humanos_guerreros, "guerreros", cantidad_humanos_arqueros, "arqueros")
                    salida_humanos = True
                    salida = True
                else:
                    print("Has comprado al arquero")
                    saldo = saldo - 100
                    cantidad_humanos_arqueros = cantidad_humanos_arqueros + 1
            if respuesta_humanos == 3:
                salida_humanos = True
                salida = True
            if saldo == 0:
              print("Tu ejercito esta formado por",  cantidad_humanos_guerreros, "guerreros", cantidad_humanos_arqueros, "arqueros")
              salida_humanos = True
              salida = True
 
    if respuesta == 2:
        cantidad_orcos_guerreros = 0
        cantidad_orcos_lanceros = 0
        saldo = 1000
        salida_orcos = False
        while not salida_orcos:
            print("Saldo restante", saldo)
            print("ORCOS")
            print("1: Guerrero, $250")
            print("2: Lancero, $150")
            print("3: Salir")
            respuesta_orcos = int(input("Ingrese una opcion: "))
            if respuesta_orcos == 1:
                if (saldo - 250) < 0:
                    print("Te has quedado sin saldo")
                    print("Tu ejercito esta formado por",  cantidad_orcos_guerreros, "guerreros", cantidad_orcos_lanceros, "lanceros")
                    salida_orcos = True
                    salida = True
                else:
                    print("Has comprado al guerrero")
                    saldo = saldo - 150
                    cantidad_orcos_guerreros = cantidad_orcos_guerreros + 1
            if respuesta_orcos == 2:
                 if (saldo - 150) < 0:
                    print("Te has quedado sin saldo")
                    print("Tu ejercito esta formado por",  cantidad_orcos_guerreros, "guerreros", cantidad_orcos_lanceros, "lanceros")
                    salida_orcos = True
                    salida = True
                 else:
                    print("Has comprado al lancero")
                    saldo = saldo - 150
                    cantidad_orcos_lanceros = cantidad_orcos_lanceros + 1
            if respuesta_orcos == 3:
                 salida_orcos = True
                 salida = True
            if saldo == 0:
              print("Tu ejercito esta formado por",  cantidad_orcos_guerreros, "guerreros", cantidad_orcos_lanceros, "lanceros")
              salida_orcos = True
              salida = True

    if respuesta == 3:
        salida = True