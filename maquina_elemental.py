from os import system
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
            if self.celdaActual == line:
                texto += "> "
            texto += f'''{line}: {self.tablero[line]} \n'''

        return str(texto)
        return str(listOfKeys)

    def _mostrarAcumulador(self):
        return self.acumulador

    def _pasarABinario(self, valor): #TODO: Borrar
        return bin(valor)#.split("b",1)[1]#[2:]

    def _obtenerCelda(self, celda): #Esta funcion devuelve el valor almacenado en la celda. No es parte de las primitivas de la maquina Abacus, sino para la facilitacion del codigo
        return self.tablero[celda]

    def _siguienteCelda(self):
        self.celdaActual = hex(int (self.celdaActual, 16) + 1).split("x",1)[1] #Pasa el numero a decimal, le suma 1, lo pasa a hexadecimal y le saca el "0x" de python del principio
        if self.celdaActual not in self.tablero: 
            self.finPrograma = True

    def _actualizarCelda(self, celda, valor):
        self.tablero[celda].actualizar_valor(valor)

    def ejecutarCeldaActual(self):
        instruccionCeldaActual = self._obtenerInstruccionCelda(self.celdaActual)
        argumentoCelda = self._obtenerArgumentoCelda(self.celdaActual)
        # print(instruccionCeldaActual)
        # print(argumentoCelda)

        match instruccionCeldaActual:
            case '0':
                self.cargaInmediata(argumentoCelda)
            case '1':
                self.carga(argumentoCelda)
            case '2':
                self.almacenar(str(argumentoCelda))
            case '3':
                self.suma(argumentoCelda)
            case '4':
                self.notAbacus()
            case '7': 
                self.difIgual(argumentoCelda)
            case '8':
                self.difMenor(argumentoCelda)
            case '9':
                self.difMayor(argumentoCelda)

    def _obtenerInstruccionCelda(self, celda) -> int:
        valorDeLaCelda = self._obtenerCelda(celda).obtener_valor()
        instruccion = 0 #TODO: Restructure
        if len(valorDeLaCelda) < 4:
            instruccion = 0 # Hacemos esto como "instruccion default" si alguna celda tiene lognitud menor a 4, entonces asumimos que la instruccion que toma es la de cargaInmediata. Esto es una caracteristica de esta implementacion, no es propio de la especificacion de Abacus
        else:
            instruccion = valorDeLaCelda[0] #Sino el primer numero es la instruccion

        return instruccion

    def _obtenerArgumentoCelda(self, celda) -> int:
        argumentoCelda = self._obtenerCelda(celda).obtener_valor()
        valor = 0
        if len(argumentoCelda) < 4:
            valor = argumentoCelda #Si la longitud es menor a 4, devolvemos todo el numero
        else:
            valor = argumentoCelda[1:]

        return valor

    def start(self):
        while self.finPrograma != True:
            # print(self.celdaActual)
            print(
                f'''
                Acumulador:{self._mostrarAcumulador()}
                '''
                    )
            print(self)
            input()
            self.ejecutarCeldaActual()
            self._siguienteCelda()


#----------------Primitivas del Abacus------------------------------------------------------------


    def cargaInmediata(self, valor): # 0 guarda el valor pasado directamente en el acumulador
        self.acumulador = valor

    def carga(self, celda): # 1 Carga el valor de la celda en el acumulador
        self.acumulador = self.tablero[celda].obtener_valor()

    def almacenar(self, celda): # 2 Guarda el contenido del acumulador en la celda pasada
        self.tablero[celda].actualizar_valor(self.acumulador)

    def suma(self, celda): # 3 Suma el contenido de la celda al acumulador y lo deja en el acumulador
        self.acumulador = int(self.acumulador) + int(self.tablero[celda].obtener_valor())

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

