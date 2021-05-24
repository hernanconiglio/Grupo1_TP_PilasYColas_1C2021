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
      
                
                
#### Tests 

estanteria1 = Estanteria(10)
estanteria2 = Estanteria(20)
estanteria3 = Estanteria(30)

libro10 = Libro(CodigoLibro('abc','00010'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro11 = Libro(CodigoLibro('abc','00011'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro12 = Libro(CodigoLibro('abc','00012'),GeneroLibro.Poesia,TipoLibro.Internacional)
libro13 = Libro(CodigoLibro('abc','00013'),GeneroLibro.Poesia,TipoLibro.Internacional)
libro14 = Libro(CodigoLibro('abc','00014'),GeneroLibro.Poesia,TipoLibro.Internacional)
libro15 = Libro(CodigoLibro('abc','00015'),GeneroLibro.Poesia,TipoLibro.Internacional)
libro16 = Libro(CodigoLibro('abc','00016'),GeneroLibro.Poesia,TipoLibro.Internacional)
libro17 = Libro(CodigoLibro('abc','00017'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro18 = Libro(CodigoLibro('abc','00018'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro19 = Libro(CodigoLibro('abc','00019'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro20 = Libro(CodigoLibro('abc','00020'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro21 = Libro(CodigoLibro('abc','00021'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro22 = Libro(CodigoLibro('abc','00022'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro23 = Libro(CodigoLibro('abc','00023'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro24 = Libro(CodigoLibro('abc','00024'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro25 = Libro(CodigoLibro('abc','00025'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro26 = Libro(CodigoLibro('abc','00026'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro27 = Libro(CodigoLibro('abc','00027'),GeneroLibro.Teatro,TipoLibro.Nacional)
libro28 = Libro(CodigoLibro('abc','00028'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro29 = Libro(CodigoLibro('abc','00029'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro30 = Libro(CodigoLibro('abc','00030'),GeneroLibro.Poesia,TipoLibro.Nacional)
libro31 = Libro(CodigoLibro('abc','00031'),GeneroLibro.Poesia,TipoLibro.Nacional)


estanteria1.guardarLibro(libro10) 
estanteria1.guardarLibro(libro11) 
estanteria1.guardarLibro(libro12) 
estanteria1.guardarLibro(libro13) 
estanteria1.guardarLibro(libro14) 
estanteria1.guardarLibro(libro15) 
estanteria1.guardarLibro(libro16) 
estanteria1.guardarLibro(libro17) 
estanteria2.guardarLibro(libro18) 
estanteria2.guardarLibro(libro19) 
estanteria2.guardarLibro(libro20) 
estanteria2.guardarLibro(libro21) 
estanteria2.guardarLibro(libro22) 
estanteria2.guardarLibro(libro23) 
estanteria2.guardarLibro(libro24) 
estanteria3.guardarLibro(libro25) 
estanteria3.guardarLibro(libro26) 
estanteria3.guardarLibro(libro27) 
estanteria3.guardarLibro(libro28) 
estanteria3.guardarLibro(libro29) 
estanteria3.guardarLibro(libro30) 
estanteria3.guardarLibro(libro31) 


biblioteca = EscritorioDeAtencion(5,6)
biblioteca.establecerEstanteria(1,3,estanteria1)
biblioteca.establecerEstanteria(3,5,estanteria2)
biblioteca.establecerEstanteria(4,1,estanteria3)
print(biblioteca)

libro682 = Libro(CodigoLibro('abc','00682'),GeneroLibro.Narracion,TipoLibro.Internacional)
libro683 = Libro(CodigoLibro('abc','00683'),GeneroLibro.Narracion,TipoLibro.Internacional)
libro684 = Libro(CodigoLibro('abc','00684'),GeneroLibro.Narracion,TipoLibro.Internacional)
libro685 = Libro(CodigoLibro('abc','00685'),GeneroLibro.Narracion,TipoLibro.Internacional)
libro686 = Libro(CodigoLibro('abc','00686'),GeneroLibro.Narracion,TipoLibro.Internacional)
libro687 = Libro(CodigoLibro('abc','00687'),GeneroLibro.Narracion,TipoLibro.Internacional)

colaLibros1 = Cola()
colaLibros1.push(libro682)
colaLibros1.push(libro683)
colaLibros1.push(libro684)
colaLibros1.push(libro685)
colaLibros1.push(libro686)
colaLibros1.push(libro687)

biblioteca.guardarLibros(colaLibros1)
print("imprimo biblioteca luego de guardarLibros")
print(biblioteca)
colaCodLibros1 = Cola()
colaCodLibros1.push("abc00015")
colaCodLibros1.push("abc00021")
colaCodLibros1.push("abc00010")
colaCodLibros1.push("AAA09873")
colaCodLibros1.push("AAA09872")

print(estanteria1)
print(estanteria2)
print(estanteria3)
print("biblioteca deposito 1,3 busco libro que está primero en la cola colaCodLibros1")
print(biblioteca.deposito[1][3].buscarLibro(colaCodLibros1.top()))   #.buscarLibro(colaCodLibros1.top()))

pilaSacadosBibl=Pila()
pilaSacadosBibl = biblioteca.sacarLibros(colaCodLibros1)
print("vuelvo a imprimir biblioteca")
print(biblioteca)
print("\n")
print("Imprimo la pila de los sacados")
print(pilaSacadosBibl)
print("\n")
print("#######################################################################################")
print(biblioteca)
print("--------------------------------------------------------------------------------------------")
print("AHORA MUEVO EL LIBRO abc00011")
print("--------------------------------------------------------------------------------------------")
biblioteca.moverLibro("abc00011",10,30)
print(biblioteca)
