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

###################
#### TDA Libro ####
###################

class Libro:
    def __init__(self,codigoLibro=CodigoLibro("zzz","99999"),genero=GeneroLibro.Teatro,nacionalidad=TipoLibro.Nacional):
        self.codigoLibro = codigoLibro
        self.genero = validarGenero(genero) ## llama a la función validarGenero para validar genero
        self.nacionalidad = validarTipoLibro(nacionalidad) ## llama a la función validarTipoLibro para validar nacionalidad

    def __repr__(self):
        cadenaPrintComp = str(self.codigoLibro) + "-" + str(self.genero.name) + "-" + str(self.nacionalidad.name)
        cadenaPrintS = str(self.codigoLibro) # hace un casteo de codigoLibro a string
        return cadenaPrintS


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

    def guardarLibro(self,libro):
        if libro.nacionalidad.name == "Nacional": ## valida si el name de la variable nacionalidad,
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
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()

        while not encontrado and not self.pilaNac.empty(): ## bucle mientras no encontrado y no está
        ## vacía la pilaNac
          if self.pilaNac.top().genero == generoDeLibro: # si el genero del libro que está en el tope 
          ## de la pilaNac es igual al valor que se pasó por parámetro en generoDeLibro
            encontrado = True ## setea en verdadero la variable encontrado
            libro = self.pilaNac.pop() ## asigna el valor de referencia del libro que está en el tope
            ## de la pilaNac y lo quita de la pila
          else: ## si no
            auxPNac.push(self.pilaNac.pop()) ## coloca en el tope de la pila auxPNac la referencia al 
            ## libro del tope de la pilaNac y lo quita de esa pila.
        
        while not auxPNac.empty(): ## bucle while no está vacía la pila auxPNac 
        ## es para volver a aplicar los libros de la pilaNac que se desapilaron en la auxPNac
          self.pilaNac.push(auxPNac.pop()) ## coloca en el tope de la pila pilaNac la referencia al
          ## libro del tope de la auxPNac y lo quita de esa pila.

        while not encontrado and not self.pilaInternac.empty(): ## bucle mientras no encontrado y no está
         ## vacía la pilaInternac
          if self.pilaInternac.top().genero == generoDeLibro: # si el genero del libro que está en el tope 
          ## de la pilaInternac es igual al valor que se pasó por parámetro en generoDeLibro
            encontrado = True ## setea en verdadero la variable encontrado
            libro = self.pilaInternac.pop() ## asigna el valor de referencia del libro que está en el tope
            ## de la pilaInternac y lo quita de la pila
          else: ## si no
            auxPInt.push(self.pilaInternac.pop()) ## coloca en el tope de la pila auxPInternac la referencia al 
            ## libro del tope de la pilaInternac y lo quita de es pila.
        
        while not auxPInt.empty(): ## bucle while no está vacía la pila auxPInternac 
        ## es para volver a aplicar los libros de la pilaInternac que se desapilaron en la auxPInternac
          self.pilaInternac.push(auxPInt.pop()) ## coloca en el tope de la pila pilaInternac la referencia al
          ## libro del tope de la auxPInternac y lo quita de esa pila.
        
        return libro ## la función retorna la variable libro que contiene la referencia al libro a recomendar


    def buscarLibro(self,codigoLibro):
      ## se inicializan variables
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()
        ## se clonan las pilas pilaNac y pilaInternac
        self.pilaNac.clone(auxPNac)
        self.pilaInternac.clone(auxPInt)

        while not encontrado and not auxPNac.empty(): ## bucle while no encontrado y no está
        ## vacía la pila auxPNac
          if str(auxPNac.top().codigoLibro) == str(codigoLibro): ## valida si el codigo del libro que
          ## está en el tope de la pila es igual al codigoLibro pasado por parámetro a la función.
            encontrado = True ## setea variable encontrado en verdadero
            libro = auxPNac.top() ## asigna el valor de referencia del libro que está en el tope
            ## de la pila auxPNac.
          else: ## si no
            auxPNac.pop() ## desapila el elemento del tope de la pila auxPNac

        while not encontrado and not auxPInt.empty(): ## bucle while no encontrado y no está
        ## vacía la pila auxPInternac
          if str(auxPInt.top().codigoLibro) == str(codigoLibro): ## valida si el codigo del libro que
          ## está en el tope de la pila es igual al codigoLibro pasado por parámetro a la función.
            encontrado = True ## setea variable encontrado en verdadero
            libro = auxPInt.top() ## asigna el valor de referencia del libro que está en el tope
             ## de la pila auxPInternac.
          else: ## si no
            auxPInt.pop() ## desapila el elemento del tope de la pila auxPNac

        return libro ## la función retorna la variable libro que contiene la referencia al libro buscado

    def prestarLibro(self,codigoLibro):
      ## se inicializan variables
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()

        while not encontrado and not self.pilaNac.empty(): ## bucle while no encontrado y no está
        ## vacía la pila pilaNac
          if str(self.pilaNac.top().codigoLibro) == str(codigoLibro): ## valida si el codigo del libro que
          ## está en el tope de la pila es igual al codigoLibro pasado por parámetro a la función.
            encontrado = True ##setea variable encontrado en verdadero
            libro = self.pilaNac.pop() ## asigna el valor de referencia del libro que está en el tope
            ## de la pilaNac y lo quita de la pila
          else: # si no
            auxPNac.push(self.pilaNac.pop()) ## coloca en el tope de la pila auxPNac la referencia al 
            ## libro del tope de la pilaNac y lo quita de esa pila.
        
        while not auxPNac.empty(): ## bucle while no está vacía la pila auxPNac 
        ## es para volver a aplicar los libros de la pilaNac que se desapilaron en la auxPNac
          self.pilaNac.push(auxPNac.pop()) ## coloca en el tope de la pila pilaNac la referencia al
          ## libro del tope de la auxPNac y lo quita de esa pila.

        while not encontrado and not self.pilaInternac.empty(): ## bucle while no encontrado y no está
        ## vacía la pila pilaInternac
          if str(self.pilaInternac.top().codigoLibro) == str(codigoLibro): # valida si el codigo del libro que
          ## está en el tope de la pila es igual al codigoLibro pasado por parámetro a la función.
            encontrado = True ##setea variable encontrado en verdadero
            libro = self.pilaInternac.pop() ## asigna el valor de referencia del libro que está en el tope
            ## de la pilaInternac y lo quita de la pila
          else: ## si no
            auxPInt.push(self.pilaInternac.pop()) ## coloca en el tope de la pila auxPInt la referencia al 
            ## libro del tope de la pilaInternac y lo quita de esa pila.
        
        while not auxPInt.empty(): ## bucle while no está vacía la pila auxPInt 
        ## es para volver a aplicar los libros de la pilaInternac que se desapilaron en la auxPInt
          self.pilaInternac.push(auxPInt.pop()) ## coloca en el tope de la pila pilaInternac la referencia al
          ## libro del tope de la auxPInt y lo quita de esa pila.

        return libro ## la función retorna la variable libro que contiene la referencia al libro prestado

   
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
        cantGen = 0 ## contador
        auxPNac = Pila()
        auxPInt = Pila()
        ## se clonan las pilas pilaNac y pilaInternac
        self.pilaNac.clone(auxPNac)
        self.pilaInternac.clone(auxPInt)  

        while not auxPNac.empty(): ## bucle while no está vacía la pila auxPNac
          if auxPNac.pop().genero == generoLibro: ## valida si el genero del libro que desapila de la auxPNac es
          ## igual al generoLibro pasado por parámetro.
            cantGen +=1 ## suma 1 al contador de cantidad de libros por genero

        while not auxPInt.empty(): ## bucle while no está vacía la pila auxPInt
          if auxPInt.pop().genero == generoLibro: ## valida si el genero del libro que desapila de la auxPInt es
          ## igual al generoLibro pasado por parámetro.
            cantGen +=1 ## suma 1 al contador de cantidad de libros por genero
        return cantGen ## retorna el valor de la cantidad de libros por genero


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
      nFila = nCol = 0 ## inicializa en cero las variables nFila y nCol
      minEstant = 999999 ## inicializa en 999999 el valor del minEstant
      for i in range(len(self.deposito)): ## bucle for para recorrer las filas del depósito
        for j in range(len(self.deposito[i])): ## bucle for para recorrer los elementos de cada fila del depósito
          if isinstance(self.deposito[i][j],Estanteria): # valida si el elemento del depósito es instancia de Estantería
            if self.deposito[i][j].librosPorTipo()[0] < minEstant: # valida si la cantidad de librosPorTipo es menor que
            ## el mínimo actual
              minEstant = self.deposito[i][j].librosPorTipo()[0] ## asigna el valor de la cantidad de librosPorTipo a 
              ## la variable minEstant
              nFila = i; nCol = j ## asigna a las variables nFila y nCol los valores de los índices i, j actuales del bucle
      return nFila,nCol ## retorna los números de nFila y nCol donde está la estantería menos recargada

        
    def buscaEstanteria(self,nroEstanteria):
      nFila = nCol = 0 ## inicializa en cero las variables nFila y nCol
      encontrado = False ## setea variable encontrado en falso
      for i in range(len(self.deposito)): ## bucle for para recorrer las filas del depósito
        for j in range(len(self.deposito[i])): ## bucle for para recorrer los elementos de cada fila del depósito
          if isinstance(self.deposito[i][j],Estanteria): # valida si el elemento del depósito es instancia de Estantería
            if self.deposito[i][j].numero == nroEstanteria: # valida si el numero de la estantería del depósito actual
            ## coincide con el nroEstanteria pasado por parámetro
              nFila = i; nCol = j ## asigna a las variables nFila y nCol los valores de los índices i, j actuales del bucle
              encontrado = True ## setea en verdadero la variable encontrado
      if encontrado: ## valida si fue encontrada la estantería
        return nFila,nCol ## retorna los números de nFila y nCol del nroEstanteria
      else: ## si no informa Exception
        raise Exception("No se encontró la estantería con Nro",nroEstanteria)

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
      ## se inicializan variables
      encontrado = False
      ubicado = False
      nFila, nCol = self.deposito.shape ## se obtiene en nFila, nCol la forma con las dimensiones de la matriz deposito
      f = 0 ## se inicializa en cero el indice de filas
      libro = Libro()
      while not encontrado and f < nFila: ## bucle while no encontrado y f es menor a nFila (contiene cantidad de filas)
        c = 0 ## se inicializa en cero el indice de columnas
        while not encontrado and c < nCol: ## bucle while no encontrado y el indice c de columnas es menor que nCol (cant columnas)
          if isinstance(self.deposito[f][c],Estanteria) and self.deposito[f][c].numero == nroEstanteriaOrigen: ## valida si 
          ## el elemento de la matriz es instancia de Estanteria y si el número de estantería coincide con el parámetro
          ## nroEstanteriaOrigen
            if self.deposito[f][c].buscarLibro(codigoLibro) != None: ## valida si no es None el resultado de
              ## ejecutar la función buscarLibro en la estantería actual del depósito para el parámetro codigoLibro
              libro = self.deposito[f][c].prestarLibro(codigoLibro) ## asigna el valor de referencia del libro que retorna
              ## la función prestarLibro (y lo quia de la estantería Origen), con el codigoLibro pasado por parámetro.
              encontrado = True ## setea en verdadero el valor de encontrado.
          c += 1 ## le suma 1 al indice que recorre por columna
        f += 1 ## le suma 1 al índice que recorre por fila
      f = 0 ## se inicializa en cero el indice de filas para iniciar el recorrido para ubicar el libro retirado 
      ## de nroEstanteriaOrigen
      while not ubicado and f < nFila: ## bucle while no ubicado libro y f es menor a nFila (contiene cantidad de filas)
        c = 0 ## se inicializa en cero el indice de columnas
        while not ubicado and c < nCol: ## bucle while no encontrado y el indice c de columnas es menor que nCol (cant columnas)
          if isinstance(self.deposito[f][c],Estanteria) and self.deposito[f][c].numero == nroEstanteriaDestino: ## valida si 
          ## el elemento de la matriz es instancia de Estanteria y si el número de estantería coincide con el parámetro
          ## nroEstanteriaDestino
            self.deposito[f][c].guardarLibro(libro) ## guarda la referencia al libro en la estantería correspondiente
            ## llamando a la función guardarLibro
            ubicado = True ## setea en verdadero la variable ubicado
          c += 1 ## le suma 1 al indice que recorre por columna
        f += 1 ## le suma 1 al índice que recorre por fila
      if not encontrado: ## valida si no fue encontrado el libro, arroja mensaje print.
        print("No se encontró el código de libro o la EstanteríaOrigen o la EstanteríaDestino")
      



