def primo(numero):
    i = 1
    if numero < 0:
        raise ValueError("Numero invalido")
    
    if numero <= 1:
        return False
    
    while i <= numero:
        divisao = numero % i
        if divisao == 0 and i != numero and i != 1:
            return False
        if i == numero:
            return True
        i *= 1  #Mutante += para *=