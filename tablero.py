class Tablero:
    def __init__(self, archivo): #TODO: Chequear que el archivo es .abs
        self.tablero = self.crearTableroDeCodigo(archivo)

    def crearTableroDeCodigo(self, archivo): #Devuelve un diccionario
        tablero = {}
        with open(archivo, "r") as f:
            for linea in f:
                linea_separada = linea.rstrip("\n").split(",", 2)
                if len(linea_separada) == 2:
                    tablero[linea_separada[0].strip()] = Celda(linea_separada[1].strip())
                else:
                    tablero[linea_separada[0].strip()] = Celda(linea_separada[1].strip(), linea_separada[2].strip())

        return tablero

class Celda:
    def __init__(self,valor, comentario = ""):
        self.valor = valor
        self.comentario = comentario

    def __str__(self):
        return f"{self.valor} | {self.comentario}"

    def obtener_valor(self):
        return self.valor

    def obtener_comentario(self):
        return self.comentario

    def actualizar_valor(self, valorNuevo):
        self.valor = valorNuevo
