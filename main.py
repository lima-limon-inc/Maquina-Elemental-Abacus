from maquina_elemental import Maquina_Elemental



def main():
    #                     Celda Inicial | Archivo   | Borre la pantalla despues de cada instruccion
    #                          \/           \/             \/
    maqEle = Maquina_Elemental("2fa","codigoEjemplo.abs", True)
    maqEle.start()

main()
