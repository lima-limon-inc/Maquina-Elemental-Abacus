

class Maquina_Elemental:
    def __init__(self,acumulador, tablero, celdaInicial):
        self.acumulador = acumulador #Acumulador de la maquina
        self.tablero = tablero #Diccionario de celdas
        self.celdaActual = celdaInicial

class Celda:
    def __init__(self,valor):
        self.valor = valor


