def media(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n <= 0: #Mutante < para <=
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)