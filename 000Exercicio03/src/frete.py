def validar_peso(peso):
    if(peso <= 0.0 or peso > 20.0):
        raise ValueError("Peso inválido")
        print(peso)
    elif peso <= 1:
        return 10.0
    elif(peso <= 5):
        return 15.0
    elif(peso <= 20):
        return 25.0
        
def validar_destino(destino):
    if destino not in ["mesma_regiao", "outra_regiao", "internacional"]:
        raise ValueError("Regiao invalida")
    return destino

def validar_valor_pedido(valor_pedido):
    if(valor_pedido <= 0):
        raise ValueError("Valor do pedido inválido")
    elif(valor_pedido < 200):
        return valor_pedido
    else:
        return 0.0
    
def calcular_frete(peso, destino, valor_pedido):
        if(validar_valor_pedido(valor_pedido) <= 200):
            if(validar_destino(destino) == "outra_regiao"):
                valor_frete = validar_peso(peso) + (validar_peso(peso) * 50) / 100
            elif(validar_destino(destino) == "internacional "):
                valor_frete = 2 * (validar_peso)

