class Cola:
  def __init__(self):
    self.cola = []
  
  def vaciar(self):
    self.cola = []

  def push(self,elemento):
    self.cola.append(elemento) ## agrega elemento al final de la cola

  def pop(self):
    if len(self.cola) > 0: ## si la cola tiene elementos
        return self.cola.pop(0) ## quita y retorna la referencia al primer
        ## elemento de la cola

  def top(self):
    if len(self.cola) > 0: ## si la cola tiene elementos
        return self.cola[0] ## retorna la referencia al primer
        ## elemento de la cola

  def clone(self,otraCola):
    for i in range(len(self.cola)): ## bucle for para recorrer la cola con index i
      otraCola.push(self.cola[i]) ## encola en otraCola el elemento i de la cola
  
  def size(self):
    return len(self.cola) ## retorna el largo de la cola

  def empty(self):
    return len(self.cola) == 0 ## retorna verdadero si la cola está vacía


  def __repr__(self):
    cadenaPrint = str(self.cola)
    return cadenaPrint