import tablero

class Maquina_Elemental:
    def __init__(self, celdaInicial, archivo):
        self.acumulador = "0" #Acumulador de la maquina
        '''
        Cada celda es un numero binario en formato hexadecimal de 3 bytes, que tiene guardada una celda de 4 bytes (1 byte para la instruccion y los otros 3 bytes para la celda a la que se le aplica). Nosotros guardamos las celdas como strings que representan numeros en base 16
        {
        300: 1500
        301: 2300
        }
        '''
        self.tablero = tablero.Tablero(archivo).tablero
        self.celdaActual = celdaInicial #String que representa un numero en base 16
        self.finPrograma = False


    def __str__(self):
        texto = ""
        listOfKeys = []
        [listOfKeys.append(x) for x in self.tablero]
        listOfKeys.sort()
        for line in listOfKeys:
            texto += f'''
            {line}: {self.tablero[line]
            '''

        return str(listOfKeys)

    def _mostrarAcumulador(self):
        return self.acumulador

    def _pasarABinario(self, valor): #TODO: Borrar
        return bin(valor)#.split("b",1)[1]#[2:]

    def _obtenerValorcelda(self, celda): #Esta funcion devuelve el valor almacenado en la celda. No es parte de las primitivas de la maquina Abacus, sino para la facilitacion del codigo
        return self.tablero[celda]

    def _siguienteCelda(self):
        self.celdaActual = hex(int (self.celdaActual, 16) + 1).split("x",1)[1] #Pasa el numero a decimal, le suma 1, lo pasa a hexadecimal y le saca el "0x" de python del principio

    def _actualizarCelda(self, celda, valor):
        self.tablero[celda].actualizar_valor(valor)

#----------------Primitivas del Abacus------------------------------------------------------------


    def cargaInmediata(self, valor): # 0 guarda el valor pasado directamente en el acumulador
        self.acumulador = valor

    def carga(self, celda): # 1 Carga el valor de la celda en el acumulador
        self.acumulador = self.obtenerValorcelda(celda)

    def almacenar(self, celda): # 2 Guarda el contenido del acumulador en la celda pasada
        self.tablero[celda].actualizar_valor(self.acumulador)

    def suma(self, celda): # 3 Suma el contenido de la celda al acumulador y lo deja en el acumulador
        self.acumulador += self.obtenerValorcelda(celda)

    def notAbacus(self): # 4 Le aplica el not al acumulador
        self.acumulador = ~self.acumulador #Bytewise not operator

    def difIgual(self, celda): # 7 Si el contenido de la celda es igual a 0, entonces vamos a esa celda
        if self.obtenerValorcelda(celda) == 0:
            self.celdaActual = celda

    def difMenor(self, celda): # 8 Si el contenido de la celda es menor a 0, entonces vamos a esa celda
        if self.obtenerValorcelda(celda) < 0:
            self.celdaActual = celda

    def difMayor(self, celda): # 9 Si el contenido de la celda es mayor a 0, entonces vamos a esa celda
        if self.obtenerValorcelda(celda) > 0:
            self.celdaActual = celda

