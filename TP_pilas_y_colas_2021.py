### TP Pilas y Colas Grupo 1 ###
import numpy as np
# importación de la librería enum
from enum import Enum
from Pila import Pila
from Cola import Cola
from CodigoLibro import CodigoLibro

## Enums ##
class GeneroLibro(int,Enum):
  Teatro = 0
  Poesia = 1
  Narracion = 2

class TipoLibro(int,Enum):
    Nacional = 0
    Internacional = 1


## VALIDACIONES Libro ##
## Valido Genero Libro
def validarGenero(genero):
  if not isinstance(genero,GeneroLibro): ## verifica si genero es instancia de GeneroLibro
    raise Exception("El genero de libro ingresado no es correcto")
  else:
    return genero

## Valido Tipo de Libro
def validarTipoLibro(tipoLib):
  if not isinstance(tipoLib,TipoLibro): ## verifica si tipoLib es instancia de TipoLibro
    raise Exception("El tipo de libro ingresado no es correcto")
  else:
    return tipoLib

## Valido Codigo de Libro ##
def validarCodigoLibro(codigoLib):
  if not isinstance(codigoLib,CodigoLibro): ## verifica si codigoLib es instancia de CodigoLibro
    raise Exception("El codigo de libro ingresado no es correcto")
  else:
    return codigoLib


## Funciones auxiliares ##
def libroEnPilaADeGenero(pila,generoDelLibro):
    encontrado = False
    libro = None
    auxPila = Pila()
    while not encontrado and not pila.empty():
      if pila.top().generoDelLibro() == generoDelLibro:
        encontrado = True
        libro = pila.pop()
      else:
        auxPila.push(pila.pop())
    while not auxPila.empty():
      pila.push(auxPila.pop())
    return libro

def buscarLibroEnPilaYRetira(pila,codigoDelLibro):
    encontrado = False
    libro = None
    auxPila = Pila()
    while not encontrado and not pila.empty():
      if pila.top().codigoDelLibro() == codigoDelLibro:
        encontrado = True
        libro = pila.pop()
      else:
        auxPila.push(pila.pop())
    while not auxPila.empty():
      pila.push(auxPila.pop())
    return libro

def buscarLibroEnPilaEInforma(pila,codigoDelLibro):
    encontrado = False
    libro = None
    auxPila = Pila()
    while not encontrado and not pila.empty():
      if pila.top().codigoDelLibro() == codigoDelLibro:
        encontrado = True
        libro = pila.top()
      else:
        auxPila.push(pila.pop())
    while not auxPila.empty():
      pila.push(auxPila.pop())
    return libro

def librosEnPilaDelGenero(pila,generoLibro):
  cantGen = 0
  auxP = Pila()
  pila.clone(auxP)
  while not auxP.empty():
    if auxP.pop().generoDelLibro() == generoLibro:
      cantGen += 1
  return cantGen

###################
#### TDA Libro ####
###################

class Libro:
    def __init__(self,codigoLibro=CodigoLibro("zzz","99999"),genero=GeneroLibro.Teatro,nacionalidad=TipoLibro.Nacional):
        self.codigoLibro = validarCodigoLibro(codigoLibro) ## llama a la función validarCodigoLibro para validar codigo
        self.genero = validarGenero(genero) ## llama a la función validarGenero para validar genero
        self.nacionalidad = validarTipoLibro(nacionalidad) ## llama a la función validarTipoLibro para validar nacionalidad

    def __repr__(self):
        cadenaPrintComp = str(self.codigoLibro) + "-" + str(self.genero.name) + "-" + str(self.nacionalidad.name)
        cadenaPrintS = str(self.codigoLibro) # hace un casteo de codigoLibro a string
        return cadenaPrintComp

    def esNacional(self):
        return self.nacionalidad == TipoLibro.Nacional

    def generoDelLibro(self):
      return self.genero

    def codigoDelLibro(self):
      return self.codigoLibro



########################
#### TDA Estanteria ####
########################


class Estanteria:
    def __init__(self,numero=0,cantCritica=50):
        self.pilaNac = Pila() ## define variable de tipo Pila para pila de libros Nacionales
        self.pilaInternac = Pila() ## define variable de tipo Pila para pila de libros Internacionales
        self.cantCritica = cantCritica #define variable cantCritica
        if numero < 0 or numero > 999: ## Valida si el número de estantería está entre 0 y 999
            raise Exception("El número de estantería debe ser un entero entre 0 y 999")
        else:
            self.numero = numero # define variable cantCritica

    def __repr__(self):
        cadenaPrintComp = "Pila Nacionales: " + str(self.pilaNac) + "\n" + "Pila Internacionales: " + str(self.pilaInternac)
        cadenaPrintS = str(self.pilaNac) + str(self.pilaInternac)
        cadenaPrintN = str(self.numero) + str(self.librosPorTipo()) # castea y concatena
        return cadenaPrintN

    def nroDeEstanteria(self):
        return self.numero

    def guardarLibro(self,libro):
        if libro.esNacional(): ## valida si el name de la variable nacionalidad,
        ## que es de tipo Enum, es igual al valor "Nacional"
            self.pilaNac.push(libro) ## pone el libro en el tope de la pila pilaNac
            if self.pilaNac.size() > self.cantCritica: ## valida si el tamaño de la pilaNac es 
            ## mayor que el valor de cantCritica de la estantería.  
                print("Superado cantidad crítica pila Nacional, Estant/cant:",self.numero, "/", self.pilaNac.size())
        else:
            self.pilaInternac.push(libro) ## pone el libro en el tope de la pilaInternac
            if self.pilaInternac.size() > self.cantCritica: ## valida si el tamaño de la pilaNac es
            ## mayor que el valor de cantCritica de la estantería.
                print("Superado cantidad crítica pila Internacional, Estant/cant:",self.numero, "/", self.pilaInternac.size())

    def primerLibroDisponible(self):
        
        if self.pilaNac.empty() and self.pilaInternac.empty(): ## valida si ambas pilas están vacías
          primerLibro = "No hay ningún libro en ninguna de las pilas de la estanteria"
          #raise Exception("No hay ningún libro en ninguna de las pilas de la estanteria")
        elif not self.pilaNac.empty(): ## valida si la pilaNac está vacía...
          primerLibro = self.pilaNac.top() ## le asigna el valor de la referencia del libro que está
          ## en el tope de la pilaNac a la variable primerLibro
        else: ## si no
          primerLibro = self.pilaInternac.top() ## le asigna el valor de la referencia del libro que está
          ## en el tope de la pilaInternac a la variable primerLibro
        return primerLibro ## la función retorna la variable primerLibro con la referencia al libro


    def libroParaRecomendar(self,generoDeLibro):
        ## se inicializan variables
        libro = libroEnPilaADeGenero(self.pilaNac,generoDeLibro)
        if libro == None:
          libro = libroEnPilaADeGenero(self.pilaInternac,generoDeLibro)
        return libro


    def buscarLibro(self,codigoLibro):
      ## se inicializan variables
        libro = buscarLibroEnPilaEInforma(self.pilaNac,codigoLibro)
        if libro == None:
          libro = buscarLibroEnPilaEInforma(self.pilaInternac,codigoLibro)
        return libro

    def prestarLibro(self,codigoLibro):
        libro = buscarLibroEnPilaYRetira(self.pilaNac,codigoLibro)
        if libro == None:
          libro = buscarLibroEnPilaYRetira(self.pilaInternac,codigoLibro)
        return libro
   
    def librosPorTipo(self):
      return self.pilaNac.size(), self.pilaInternac.size() ## retorna tupla con el valor del tamaño de la pilaNac
      ## y el valor de tamaño de la pilaInternac

    def cantidadTotalLibros(self):
      return sum(self.librosPorTipo()) ## retorna la suma del tamaño de las pilas pilaNac y pilaInternac

    def esCritica(self):
      return self.pilaNac.size() > self.cantCritica or self.pilaInternac.size() > self.cantCritica ## retorna True
      ## si el tamaño de la pilaNac o el tamaño de pilaInternac (alguno o ambos) es mayor a cantCritica

    def librosPorGenero(self,generoLibro):
        ## se inicializan variables
        cantGen = librosEnPilaDelGenero(self.pilaNac,generoLibro) + librosEnPilaDelGenero(self.pilaInternac,generoLibro)
        return cantGen


##################################
#### TDA EscritorioDeAtencion ####
##################################

class EscritorioDeAtencion:
    def __init__(self,nroFilas=0, nroColumnas=0):
      ## se define depósito como un arreglo bidimensional de nroFilas por nroColumnas de tipo None
      self.deposito = np.full((nroFilas,nroColumnas),None)

    def __repr__(self):
      cadenaPrint = str(self.deposito) + "\n"
      return cadenaPrint

    def establecerEstanteria(self, nroFila, nroColumna, estanteria):
      self.deposito[nroFila][nroColumna] = estanteria ## asigna la referencia a la estantería pasada por 
      # parámetro en la ubicación nroFila,nroColumna de la matriz.


    def cantidadDeEstanteriasCriticas(self,nroFila,columna=0):
      cantCrit = 0 ## inicializa variable contador de cantidad de estanterías críticas
      if columna < len(self.deposito[nroFila]): # valida que no sea caso de borde, es decir, que el valor del 
      ## indice de columna sea menor que el largo del arreglo pasado por parámetro. El caso de borde sería cuando
      ## el valor de columna sea igual al largo del arreglo (el índice del último elemento siempre es largo-1)
        estant = self.deposito[nroFila][columna] ## asigna a variable estant el elemento de la matriz para
        ## simplifica el código.
        if isinstance(estant,Estanteria) and estant.esCritica(): ## valida si el elemento estant es instancia
        ## de Estanteria y además por medio de la llamada a la función esCritica() si supera la cantidad crítica
        ## de la estantería.
          cantCrit += 1 ## suma 1 al valor de cantCrit
        cantCrit = cantCrit + self.cantidadDeEstanteriasCriticas(nroFila,columna+1) ## asigna al contador cantCrit
        ## el resultado de si mismo más el resultado de llamar recursivamente a la misma función, pero sumando 1 al
        ## número de columna (o índice del arreglo), para ir recorriendo todos los elementos del arreglo e ir
        ## actualizando el contador cantCrit
      return cantCrit ## retorna el valor del contador cantCrit

    def cantidadDeEstanteriasCriticasIterativa(self,nroFila):
      cantCrit = 0
      for i in range(len(self.deposito[nroFila])):
        estant = self.deposito[nroFila][i]
        if isinstance(estant,Estanteria) and estant.esCritica():
          cantCrit += 1 
      return cantCrit


    def estanteriaMenosRecargada(self):
      nFila = nCol = None ## inicializa en cero las variables nFila y nCol
      minEstant = None ## inicializa en None el valor del minEstant
      for i in range(len(self.deposito)): ## bucle for para recorrer las filas del depósito
        for j in range(len(self.deposito[i])): ## bucle for para recorrer los elementos de cada fila del depósito
          if isinstance(self.deposito[i][j],Estanteria): # valida si el elemento del depósito es instancia de Estantería
            if minEstant == None:
              minEstant = self.deposito[i][j].librosPorTipo()[0]
            if self.deposito[i][j].librosPorTipo()[0] < minEstant: # valida si la cantidad de librosPorTipo es menor que
            ## el mínimo actual
              minEstant = self.deposito[i][j].librosPorTipo()[0] ## asigna el valor de la cantidad de librosPorTipo a 
              ## la variable minEstant
              nFila = i; nCol = j ## asigna a las variables nFila y nCol los valores de los índices i, j actuales del bucle
      return nFila,nCol ## retorna los números de nFila y nCol donde está la estantería menos recargada

        
    def buscaEstanteria(self,nroEstanteria):
      nFila = nCol = None ## inicializa en cero las variables nFila y nCol
      for i in range(len(self.deposito)): ## bucle for para recorrer las filas del depósito
        for j in range(len(self.deposito[i])): ## bucle for para recorrer los elementos de cada fila del depósito
          if isinstance(self.deposito[i][j],Estanteria): # valida si el elemento del depósito es instancia de Estantería
            if self.deposito[i][j].nroDeEstanteria() == nroEstanteria: # valida si el numero de la estantería del depósito actual
            ## coincide con el nroEstanteria pasado por parámetro
              nFila = i; nCol = j ## asigna a las variables nFila y nCol los valores de los índices i, j actuales del bucle
      return nFila,nCol ## retorna los números de nFila y nCol del nroEstanteria

    def guardarLibros(self,colaDeLibros):
      while not colaDeLibros.empty(): # bucle while no está vacía la colaDeLibros (pasada por parámetro)
        nFila,nCol = self.estanteriaMenosRecargada() ## asigna a las variables nFila y nCol los valores de fila
        # y columna de la estantería menos recargada en ese momento
        self.deposito[nFila][nCol].guardarLibro(colaDeLibros.pop()) ## desencola el libro de la colaDeLibros y lo
        ## apila en la estantería correspondiente a la fila nFila y columna nCol que obtuvo en el paso anterior

    def sacarLibros(self,colaCodLibros):
      pilaSacados = Pila() ## se define una variable de tipo Pila
      while not colaCodLibros.empty(): ## bucle while no esté vacía la cola colaCodLibros pasada por parámetro
        for i in range(len(self.deposito)): ## bucle for para recorrer las filas del depósito
          for j in range(len(self.deposito[i])): ## bucle for para recorrer los elementos de cada fila del depósito
            if isinstance(self.deposito[i][j],Estanteria): # valida si el elemento del depósito es instancia de Estantería
              if self.deposito[i][j].buscarLibro(colaCodLibros.top()) != None: ## valida si no es None el resultado de
              ## ejecutar la función buscarLibro en la estantería actual del depósito
                pilaSacados.push(self.deposito[i][j].prestarLibro(colaCodLibros.top())) ## coloca en el tope de la pila 
                ## pilaSacados la referencia al libro que está prestando.
        colaCodLibros.pop() ## desencola el primer elemento de la cola
      return pilaSacados ## retorna la pila conteniendo las referencias a los libros sacados


    def moverLibro(self, codigoLibro, nroEstanteriaOrigen, nroEstanteriaDestino):
      ## rescatamos las "coordenadas" de las estanterias origen y destino
      nroFilaO, nroColO = self.buscaEstanteria(nroEstanteriaOrigen)
      nroFilaD, nroColD = self.buscaEstanteria(nroEstanteriaDestino)
      ## validamos en unas variables que las estanterias existen en el deposito
      origenValido = nroFilaO != None and nroColO != None
      destinoValido = nroFilaD != None and nroColD != None
      if origenValido and destinoValido:
        ## si las estanterias son validas entonces intentamos retirar el libro de la estanteria origen
        libro = self.deposito[nroFilaO][nroColO].prestarLibro(codigoLibro)
        ## si el libro se encuentra en la estanteria origen entonces queda almacenado en la variable libro
        if libro != None:
          ## Guardamos el libro en la estanteria destino
          self.deposito[nroFilaD][nroColD].guardarLibro(libro)
        else:
          print("El libro no se encontro en la estanteria origen.")
        ## si el libro no se encontraba en la estanteria origen entonces no va a suceder nada
        ## ya q no se va a intentar guardar el libro.
      elif not origenValido and not destinoValido:
        print("Las estanterias origen y destino no son validas")
      elif origenValido and not destinoValido:
        print("La estanteria destino no es valida")        
      else:
        print("La estanteria origen no es valida")

