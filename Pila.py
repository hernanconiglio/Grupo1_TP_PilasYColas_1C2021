class Pila:
  def __init__(self,entrada = None):
    self.pila = []
    if entrada:
      for i in entrada:
        self.pila.push(i)

  def vaciar(self):
    self.pila = []

  def push(self,elemento):
    self.pila.insert(0,elemento) ## inserta elemento en el tope de la pila

  def pop(self):
    if len(self.pila) > 0: ## valida si la pila tiene elementos
      return self.pila.pop(0) ## quita y retorna del tope de la pila el elemento

  def top(self):
    if len(self.pila) > 0: ## valida si la pila tiene elementos
      return self.pila[0] ## retorna del tope de la pila el elemento
      
  def clone(self,otraPila):
    for i in reversed(range(len(self.pila))): #bucle recorre inversa la pila index i
      otraPila.push(self.pila[i]) ## apila el elemento de indice i

  def size(self):
    return len(self.pila) ## retorna tamaño de la pila

  def empty(self):
    return len(self.pila) == 0 ## verdadero si la pila está vacía

  def __repr__(self):
    cadenaPrint = str(self.pila)
    return cadenaPrint