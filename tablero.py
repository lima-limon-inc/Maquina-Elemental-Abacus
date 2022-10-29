class Tablero:
    def __init__(self, archivo): #TODO: Chequear que el archivo es .abs
        self.tablero = self.crearTableroDeCodigo(archivo)

    def crearTableroDeCodigo(self, archivo): #Devuelve un diccionario
        tablero = {}
        with open(archivo, "r") as f:
            for linea in f:
                celda, valor = linea.rstrip("\n").split("|")
                tablero[celda.strip()] = valor.strip()

        return tablero

def main():
    tablero = Tablero("archivo.abs")
    print(tablero.tablero)

main()
