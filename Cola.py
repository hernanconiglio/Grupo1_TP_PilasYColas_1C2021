class Cola:
  def __init__(self):
    self.cola = []
  
  def vaciar(self):
    self.cola = []

  def push(self,elemento):
    self.cola.append(elemento)

  def pop(self):
    if len(self.cola) > 0:
        return self.cola.pop(0)

  def top(self):
    if len(self.cola) > 0:
        return self.cola[0]

  def clone(self,otraCola):
    for i in range(len(self.cola)):
      otraCola.push(self.cola[i])
  
  def size(self):
    return len(self.cola)

  def empty(self):
    return len(self.cola) == 0


  def __repr__(self):
    cadenaPrint = str(self.cola)
    return cadenaPrint