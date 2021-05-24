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
  if not isinstance(genero,GeneroLibro):
    raise Exception("El genero de libro ingresado no es correcto")
  else:
    return genero

## Valido Tipo de Libro
def validarTipoLibro(tipoLib):
  if not isinstance(tipoLib,TipoLibro):
    raise Exception("El tipo de libro ingresado no es correcto")
  else:
    return tipoLib


class Libro:
    def __init__(self,codigoLibro=CodigoLibro("zzz","99999"),genero=GeneroLibro.Teatro,nacionalidad=TipoLibro.Nacional):
        self.codigoLibro = codigoLibro
        self.genero = validarGenero(genero)
        self.nacionalidad = validarTipoLibro(nacionalidad)
#    def __repr__(self):
#        cadenaPrint = "Código de libro: " + str(self.codigoLibro) + " con genero " + str(self.genero.name) + " y nacionalidad " + str(self.nacionalidad.name)
#        return cadenaPrint

    def __repr__(self):
        cadenaPrintComp = str(self.codigoLibro) + "-" + str(self.genero.name) + "-" + str(self.nacionalidad.name)
        cadenaPrintS = str(self.codigoLibro)
        return cadenaPrintS



class Estanteria:
    def __init__(self,numero=0,cantCritica=50):
        self.pilaNac = Pila()
        self.pilaInternac = Pila()
        self.cantCritica = cantCritica
        if numero < 0 or numero > 999:
            raise Exception("El número de estantería debe ser un entero entre 0 y 999")
        else:
            self.numero = numero

    def __repr__(self):
        cadenaPrintComp = "Pila Nacionales: " + str(self.pilaNac) + "\n" + "Pila Internacionales: " + str(self.pilaInternac)
        cadenaPrintS = str(self.pilaNac) + str(self.pilaInternac)
        cadenaPrintN = str(self.numero)
        return cadenaPrintS

    def guardarLibro(self,libro):
        if libro.nacionalidad.name == "Nacional":
            self.pilaNac.push(libro)
            if self.pilaNac.size() > self.cantCritica:
                print("Superado cantidad crítica pila Nacional, (Estant/cant:",self.numero, "/", self.pilaNac.size())
        else:
            self.pilaInternac.push(libro)
            if self.pilaInternac.size() > self.cantCritica:
                print("Superado cantidad crítica pila Internacional, Estant/cant:",self.numero, "/", self.pilaInternac.size())

    def primerLibroDisponible(self):
        
        if self.pilaNac.empty() and self.pilaInternac.empty():
          primerLibro = "No hay ningún libro en ninguna de las pilas de la estanteria"
          #raise Exception("No hay ningún libro en ninguna de las pilas de la estanteria")
        elif not self.pilaNac.empty():
          primerLibro = self.pilaNac.top()
        else:
          primerLibro = self.pilaInternac.top()
        return primerLibro

    def libroParaRecomendar(self,generoDeLibro):
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()

        while not encontrado and not self.pilaNac.empty():
          if self.pilaNac.top().genero == generoDeLibro:
            encontrado = True
            libro = self.pilaNac.pop()
          else:
            auxPNac.push(self.pilaNac.pop())
        
        while not auxPNac.empty():
          self.pilaNac.push(auxPNac.pop())

        while not encontrado and not self.pilaInternac.empty():
          if self.pilaInternac.top().genero == generoDeLibro:
            encontrado = True
            libro = self.pilaInternac.pop()
          else:
            auxPInt.push(self.pilaInternac.pop())
        
        while not auxPInt.empty():
          self.pilaInternac.push(auxPInt.pop())
        
        return libro
    
    def buscarLibro(self,codigoLibro):
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()
        self.pilaNac.clone(auxPNac)
        self.pilaInternac.clone(auxPInt)

        while not encontrado and not auxPNac.empty():
          if str(auxPNac.top().codigoLibro) == str(codigoLibro):
            encontrado = True
            libro = auxPNac.top()
          else:
            auxPNac.pop()

        while not encontrado and not auxPInt.empty():
          if str(auxPInt.top().codigoLibro) == str(codigoLibro):
            encontrado = True
            libro = auxPInt.top()
          else:
            auxPInt.pop()

        return libro

    def prestarLibro(self,codigoLibro):
        encontrado = False
        libro = None
        auxPNac = Pila()
        auxPInt = Pila()

        while not encontrado and not self.pilaNac.empty():
          if str(self.pilaNac.top().codigoLibro) == str(codigoLibro):
            encontrado = True
            libro = self.pilaNac.pop()
          else:
            auxPNac.push(self.pilaNac.pop())
        
        while not auxPNac.empty():
          self.pilaNac.push(auxPNac.pop())

        while not encontrado and not self.pilaInternac.empty():
          if str(self.pilaInternac.top().codigoLibro) == str(codigoLibro):
            encontrado = True
            libro = self.pilaInternac.pop()
          else:
            auxPInt.push(self.pilaInternac.pop())
        
        while not auxPInt.empty():
          self.pilaInternac.push(auxPInt.pop())

        return libro

   
    def librosPorTipo(self):
      return self.pilaNac.size(), self.pilaInternac.size()

    def cantidadTotalLibros(self):
      return sum(self.librosPorTipo())

    def esCritica(self):
      return self.pilaNac.size() > self.cantCritica or self.pilaInternac.size() > self.cantCritica

    def librosPorGenero(self,generoLibro):
        cantGen = 0
        auxPNac = Pila()
        auxPInt = Pila()
        self.pilaNac.clone(auxPNac)
        self.pilaInternac.clone(auxPInt)  

        while not auxPNac.empty():
          if auxPNac.pop().genero == generoLibro:
            cantGen +=1

        while not auxPInt.empty():
          if auxPInt.pop().genero == generoLibro:
            cantGen +=1
        return cantGen 


class EscritorioDeAtencion:
    def __init__(self,nroFilas=0, nroColumnas=0):
      #self.deposito = np.empty((nroFilas,nroColumnas))
      ## inicializo la matriz con None ##
      self.deposito = np.zeros((nroFilas,nroColumnas),Estanteria)
      for i in range(nroFilas):
        for j in range(nroColumnas):
          self.deposito[i][j] = None

#    def __repr__(self):
#      cadenaPrint = str(self.deposito)
#      return cadenaPrint

    def __repr__(self):
      cadenaPrint = str(self.deposito) + "\n"
      return cadenaPrint

    def establecerEstanteria(self, nroFila, nroColumna, estanteria):
      self.deposito[nroFila][nroColumna] = estanteria

    def cantidadDeEstanteriasCriticas(self,nroFila):
      cantCrit = 0
      for i in range(len(self.deposito[nroFila])):
        estant = self.deposito[nroFila][i]
        if isinstance(estant,Estanteria) and estant.esCritica():
          cantCrit += 1 
      return cantCrit

    def cantidadDeEstanteriasCriticasR(self,nroFila):
      cantCrit = 0
      if len(self.deposito[nroFila]) == 0:
        cantCrit = 0
      else:
        estant = self.deposito[nroFila][len(self.deposito[nroFila])-1]
        if isinstance(estant,Estanteria) and estant.esCritica():
          cantCrit += 1
        cantCrit += self.deposito[nroFila][:len(self.deposito[nroFila])-1]
      return cantCrit


    def estanteriaMenosRecargada(self):
      nFila = nCol = 0
      minEstant = 999999
      for i in range(len(self.deposito)):
        for j in range(len(self.deposito[i])):
          if isinstance(self.deposito[i][j],Estanteria):
            if self.deposito[i][j].librosPorTipo()[0] < minEstant:
              minEstant = self.deposito[i][j].librosPorTipo()[0]
              nFila = i; nCol = j
      return nFila,nCol

        
    def buscaEstanteria(self,nroEstanteria):
      nFila = nCol = 0
      encontrado = False
      for i in range(len(self.deposito)):
        for j in range(len(self.deposito[i])):
          if isinstance(self.deposito[i][j],Estanteria):
            if self.deposito[i][j].numero == nroEstanteria:
              nFila = i; nCol = j
              encontrado = True
      if encontrado:
        return nFila,nCol
      else:
        raise Exception("No se encontró la estantería con Nro",nroEstanteria)

    def guardarLibros(self,colaDeLibros):
      while not colaDeLibros.empty():
        nFila,nCol = self.estanteriaMenosRecargada()
        self.deposito[nFila][nCol].guardarLibro(colaDeLibros.pop())

    def sacarLibros(self,colaCodLibros):
      pilaSacados = Pila()
      while not colaCodLibros.empty():
        for i in range(len(self.deposito)):
          for j in range(len(self.deposito[i])):
            if isinstance(self.deposito[i][j],Estanteria):
              if self.deposito[i][j].buscarLibro(colaCodLibros.top()) != None:
                pilaSacados.push(self.deposito[i][j].prestarLibro(colaCodLibros.top()))
              #else:
        colaCodLibros.pop()
      return pilaSacados

    def moverLibro(self, codigoLibro, nroEstanteriaOrigen, nroEstanteriaDestino):
      encontrado = False
      ubicado = False
      nFila, nCol = self.deposito.shape
      f = 0
      libro = Libro()
      while not encontrado and f < nFila:
        c = 0
        while not encontrado and c < nCol:
          if isinstance(self.deposito[f][c],Estanteria) and self.deposito[f][c].numero == nroEstanteriaOrigen:
            if self.deposito[f][c].buscarLibro(codigoLibro) != None:
              libro = self.deposito[f][c].prestarLibro(codigoLibro)
              encontrado = True
          c += 1
        f += 1
      f = 0
      while not ubicado and f < nFila:
        c = 0
        while not ubicado and c < nCol:
          if isinstance(self.deposito[f][c],Estanteria) and self.deposito[f][c].numero == nroEstanteriaDestino:
            self.deposito[f][c].guardarLibro(libro)
            ubicado = True
          c += 1
        f += 1
      if not encontrado:
        print("No se encontró el código de libro o la EstanteríaOrigen o la EstanteríaDestino")
      
                
                
