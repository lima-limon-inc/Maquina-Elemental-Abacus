from maquina_elemental import Maquina_Elemental
from sys import argv

def main():
    #                     Celda Inicial | Archivo   | Borre la pantalla despues de cada instruccion
    #                          \/           \/             \/
    nombreArchivo = argv[1]
    celdaInicial = argv[2]

    maqEle = Maquina_Elemental(nombreArchivo, celdaInicial, True)
    maqEle.start()

main()
