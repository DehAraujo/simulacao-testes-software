def calcular_frete(peso, destino, valor_pedido):
    #tratamentos de erros
    if peso <= 0 or peso > 20:
        raise ValueError("Peso inválido")

    if destino not in ["mesma_regiao", "outra_regiao", "internacional"]:
        raise ValueError("Destino inválido")

    if valor_pedido < 0:
        raise ValueError("Valor do pedido inválido")
    #peso
    if peso <= 1:
        frete = 10.0
    elif peso <= 5:
        frete = 15.0
    else:
        frete = 25.0

    #destino
    if destino == "outra_regiao":
        frete = frete + (frete * 50) / 100
    elif destino == "internacional":
        frete *= 2

    #pedido
    if valor_pedido > 200:
        return 0.0

    return frete

