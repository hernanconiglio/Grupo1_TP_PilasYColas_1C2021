from TP_pilas_y_colas_2021 import *
from CodigoLibro import *
from Cola import *
from Pila import *

################################################################################
###########################SCRIPT DE PRUEBA#####################################
################################################################################

#############################IMPORTANTE!!!!!!###################################
#############COSAS PARA CONTROLAR ANTES DE EJECUTAR ESTA PRUEBA#################
#############################IMPORTANTE!!!!!!###################################

#Si usan Enums, los tienen que definir asi (respetar nombres y numeros asociados a cada uno):
#class GeneroLibro(int,Enum):
#  Teatro = 0
#  Poesia = 1
#  Narracion = 2
#class TipoLibro(int,Enum):
#  Nacional = 0
#  Internacional = 1

#En la parte donde se cargan los datos de las Estanterías: Comenten o descomenten los
#bloques de codigo indicados, segun usen o no usen Enums en sus implementaciones

#Orden de variables en constructores (__init__):
#TDA Libro: self, codigo, genero, tipo
#TDA Estanteria: self, numero, cantCritica
#TDA EscritorioDeAtencion: self, cantFilas, cantColumnas

#Mantengan nombres de TDAs, operaciones y orden de parametros en las operaciones
#segun lo que esta definido en el enunciado

#Para ver mejor la salida pueden comentar la parte que imprime cuando la Estanteria 
#llega a la cantidad critica en la operacion guardarLibro

########################Definicion de variables#################################
#################IMPORTANTE: NO MODIFICAR ESTAS VARIABLES!!!!!!!!!!!!!!!!!!!!!!!
nroFilas = 10
nroColumnas = 10
generos = ["Teatro","Poesia","Narracion"]
tipos = ["Nacional","Internacional"]
estanteriasData = {}
primerosLibrosPorEstanteria = {}
primerosLibrosDeNarracion = {}

################################################################################
###########Creacion de escritorio y carga de estanterias########################
################################################################################

####################Lectura de archivo con datos de libros######################
librosFile = open('TP_pilasColas_datosPrueba_2021.csv', encoding="utf8")
for libro in librosFile:
  libroData = libro[:-1].split(',')
  numero = int(libroData[0])
  if numero in estanteriasData:
    estanteriasData[numero][1].append(libroData[4:7])
  else:
    estanteriasData[numero] = []
    estanteriasData[numero].append(libroData[1:4])
    estanteriasData[numero].append([libroData[4:7]])
librosFile.close() 

################################################################################

######################Creacion de escritorio####################################
escritorioDeAtencion = EscritorioDeAtencion(nroFilas, nroColumnas)
################################################################################

######################Carga de estanterias######################################
for numero in estanteriasData:
  estanteriaData = estanteriasData[numero][0]
  cantCritica = int(estanteriaData[0])
  nroFila = int(estanteriaData[1])
  nroColumna = int(estanteriaData[2])

  ############Creacion de estanteria################
  estanteria = Estanteria(numero, cantCritica)
  
  ############Carga de libros a estanteria########
  for libroData in estanteriasData[numero][1]:
    codigo = libroData[0]
    
    ###################Para uso con Enum########################################
    genero = GeneroLibro(generos.index(libroData[2]))                           ###Comentar si usan strings 
    tipo = TipoLibro(tipos.index(libroData[1]))                                 ###Comentar si usan strings
    ############################################################################

    ###################Para uso con strings#####################################
    #genero = libroData[2]                                                      ###Comentar si usan Enums
    #tipo = libroData[1]                                                        ###Comentar si usan Enums
    ############################################################################

    ##############Creacion de libro#########################
    #libro = Libro(codigo, genero, tipo)                                         ###Comentar si usan TDA para codigo
    libro = Libro(CodigoLibro(codigo[0:3],codigo[3:8]), genero, tipo)          ###Comentar si usan string para codigo
    ##############Guardo libro en estanteria##################
    estanteria.guardarLibro(libro)
  
  ################Ubicacion de estanteria en deposito####################
  escritorioDeAtencion.establecerEstanteria(nroFila, nroColumna, estanteria)



  ##############################################################################
  ##########Ejecucion de pruebas de operaciones de TDA Estanteria###############
  ##############################################################################

  ##########################primerLibroDisponible###############################
  primerosLibrosPorEstanteria[numero] = estanteria.primerLibroDisponible()

  ##########################libroParaRecomendar#################################
  #####################Para uso con Enum########################################
  libroARecomendar = estanteria.libroParaRecomendar(GeneroLibro(generos.index("Narracion")))      ###Comentar si usan strings
  ##############################################################################

  #####################Para uso con strings#####################################
  #libroARecomendar = estanteria.libroParaRecomendar("Narracion")                                 ###Comentar si usan Enums
  ##############################################################################

  primerosLibrosDeNarracion[numero] = libroARecomendar
  estanteria.guardarLibro(libroARecomendar)
################################################################################

#####################Impresion de escritorio de atencion########################
print("Depósito de estanterías de escritorio de atención:\n")
print(escritorioDeAtencion)
print("-----------------------------------------------------------------------\n")

################################################################################
############Impresion de pruebas de operaciones de TDA Estanteria###############
################################################################################

for numero in primerosLibrosPorEstanteria:
  ##########################primerAuxilioAEnviar################################
  print("Primer libro disponible en estanteria", numero, ":", primerosLibrosPorEstanteria[numero])
  
  ##########################libroParaRecomendar#################################
  print("Libro de género Narracion para recomendar en estanteria", numero, ":", primerosLibrosDeNarracion[numero])

print("-----------------------------------------------------------------------\n")
  
################################################################################
#############Prueba de operaciones de TDA EscritorioDeAtencion##################
################################################################################

#######################cantidadDeEstanteriasCriticas###############################
print("\n\nCantidad de estanterias criticas en cada fila del depósito:\n")
for nroFila in range(nroFilas):
  print("Fila",nroFila,":",escritorioDeAtencion.cantidadDeEstanteriasCriticas(nroFila))  
print("-----------------------------------------------------------------------")

#########################estanteriaMenosRecargada###############################
print("\n\nEstantería menos recargada del depósito:\n")
print(escritorioDeAtencion.estanteriaMenosRecargada())  
print("-----------------------------------------------------------------------")

#########################buscaEstanteria########################################
print("\n\nUbicación de cada estantería en el depósito:\n")
for numero in estanteriasData:
  print("Número",numero,":",escritorioDeAtencion.buscaEstanteria(numero))  
print("-----------------------------------------------------------------------")

##########################moverLibro############################################
print("\n\nMovimiento de libros de la estantería 104 (fila 5) a la estantería 103 (fila 1):\n")
print("Cantidad de estanterías criticas en la fila 1 antes:",escritorioDeAtencion.cantidadDeEstanteriasCriticas(1))
print("Cantidad de estanterías criticas en la fila 5 antes:",escritorioDeAtencion.cantidadDeEstanteriasCriticas(5))

for libroData in estanteriasData[104][1]:
  codigo = libroData[0]
  #escritorioDeAtencion.moverLibro(codigo,104,103)                               ###Comentar si usan TDA para codigo
  escritorioDeAtencion.moverLibro(CodigoLibro(codigo[0:3],codigo[3:8]),104,103) ###Comentar si usan string para codigo

print("\nCantidad de estanterías criticas en la fila 1 despues:",escritorioDeAtencion.cantidadDeEstanteriasCriticas(1))
print("Cantidad de estanterías criticas en la fila 5 despues:",escritorioDeAtencion.cantidadDeEstanteriasCriticas(5))
print("-----------------------------------------------------------------------")
