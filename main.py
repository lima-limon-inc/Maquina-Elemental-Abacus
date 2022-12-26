from maquina_elemental import Maquina_Elemental



def main():
    maqEle = Maquina_Elemental("2fa","archivo.abs", True)
    # print(maqEle._mostrarAcumulador())
    # maqEle.cargaInmediata("400")
    # print(maqEle._mostrarAcumulador())
    # print(maqEle.tablero)
    # maqEle._actualizarCelda("300","1200")
    # print(maqEle.tablero)
    # maqEle.almacenar("300")
    # print(maqEle)
    maqEle.start()
    # print(maqEle)
    # print("Fin")

main()
