from maquina_elemental import Maquina_Elemental

def main():
    #                     Celda Inicial | Archivo   | Borre la pantalla despues de cada instruccion
    #                          \/           \/             \/
    maqEle = Maquina_Elemental("2fa","codigoExcel.xlsx", True)
    maqEle.start()

main()
