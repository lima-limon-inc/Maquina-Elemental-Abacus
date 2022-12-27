EXTENSIONES_VALIDAS = ["abs", "xlsx", "xls"]

class Tablero:
    def __init__(self, archivo):
        extensionArchivo = (archivo.split(".",1))[1]
        if extensionArchivo not in EXTENSIONES_VALIDAS:
            extensionesValidasConFormato = ""
            for extension in EXTENSIONES_VALIDAS:
                extensionesValidasConFormato += extension + ", "
            extensionesValidasConFormato = extensionesValidasConFormato[:-2] #Le saca la coma de mas del ultima extension
            raise OSError(f'''
{archivo} no tiene la extension requerida, se necesita un archivo con extension: {extensionesValidasConFormato}''')

        if extensionArchivo != "abs":
            from leerExcel import leerAbacusExcel #De esta manera, logramos que la libreria openpyxl sea modular/opcional. Solo la descargas si queres
            leerAbacusExcel(archivo)
            archivo = str(archivo.split(".",1)[0]) + ".abs"

        self.tablero = self.crearTableroDeCodigo(archivo)

    def crearTableroDeCodigo(self, archivo): #Devuelve un diccionario
        tablero = {}
        with open(archivo, "r") as f:
            for linea in f:
                linea_separada = linea.rstrip("\n").split(",", 2)
                if len(linea_separada) == 1:
                    continue
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
