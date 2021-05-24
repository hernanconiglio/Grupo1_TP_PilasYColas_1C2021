class CodigoLibro:
    def __init__(self,codLetras="",codNumero=""):
        if codLetras.isalpha() and len(codLetras)==3:
            self.codLetras = codLetras
        else:
            raise Exception("El código debe comenzar con 3 letras")
        if codNumero.isdigit() and len(codNumero)==5:
            self.codNumero = codNumero
        else:
            raise Exception("El código debe tener 5 números luego de las 3 letras")
    
    def __repr__(self):
        cadenaPrint = self.codLetras + self.codNumero
        return cadenaPrint
