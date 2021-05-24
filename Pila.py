class Pila:
  def __init__(self,entrada = None):
    self.pila = []
    if entrada:
      for i in entrada:
        self.pila.push(i)
  def vaciar(self):
    self.pila = []
  def push(self,elemento):
    self.pila.insert(0,elemento)
  def pop(self):
    if len(self.pila) > 0:
      return self.pila.pop(0)
  def top(self):
    if len(self.pila) > 0:
      return self.pila[0]
  def clone(self,otraPila):
    for i in reversed(range(len(self.pila))):
      otraPila.push(self.pila[i])
  def size(self):
    return len(self.pila)
  def empty(self):
    return len(self.pila) == 0
  def __repr__(self):
    cadenaPrint = str(self.pila)
    return cadenaPrint