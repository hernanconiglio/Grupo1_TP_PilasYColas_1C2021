class CodigoLibro: # TDA para definir el código de cada Libro
    def __init__(self,codLetras="",codNumero=""):
        if codLetras.isalpha() and len(codLetras)==3: ## valida si codLetras contiene solo letras
        ## y además el largo es igual a 3
            self.codLetras = codLetras ## asigna a self.codLetras el valor del parámetro codLetras
        else: # si no
            raise Exception("El código debe comenzar con 3 letras") ## arroja raise Exception
        if codNumero.isdigit() and len(codNumero)==5: ## valida si codNumero contiene solo dígitos
        ## o números y además el largo es igual a 5
            self.codNumero = codNumero ## asigna a self.codNumero el valor del parámetro codNumero
        else: # si no
            raise Exception("El código debe tener 5 números luego de las 3 letras") ## arroja Exception
    
    def __repr__(self):
        cadenaPrint = self.codLetras + self.codNumero
        return cadenaPrint
