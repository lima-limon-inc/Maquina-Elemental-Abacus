from maquina_elemental import Maquina_Elemental


# class Sistema:
#     def __init__(self, archivo, celdaInicial): #TODO: Chequear que el archivo es .abs


def main():
    maqEle = Maquina_Elemental("300","archivo.abs")
    # print(maqEle._mostrarAcumulador())
    # maqEle.cargaInmediata("400")
    # print(maqEle._mostrarAcumulador())
    # print(maqEle.tablero)
    # maqEle._actualizarCelda("300","1200")
    # print(maqEle.tablero)
    # maqEle.almacenar("300")
    print(maqEle)
    maqEle.start()
    print(maqEle)
    # print("Fin")

main()
