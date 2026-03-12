def fatorial(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial