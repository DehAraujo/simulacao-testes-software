# =========================
# FUNÇÃO 1 - classificar
# =========================
def classificar(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def fatorial(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 3 - maior
# =========================
def maior(a, b):
    if a > b:
        return a
    else:
        return b


# =========================
# FUNÇÃO 4 - media
# =========================
def media(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 5 - primo
# =========================
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

        i += 1