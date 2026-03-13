# =========================
# FUNÇÃO 1 - classificar
# =========================

# Mutante 1 (< -> >)
def classificar(numero):
    if numero > 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"


# Mutante 2 (> -> >=)
def classificar_m2(numero):
    if numero < 0:
        return "negativo"
    elif numero >= 0:
        return "positivo"
    else:
        return "zero"


# =========================
# FUNÇÃO 2 - fatorial
# =========================

# Mutante 1 (< -> <=)
def fatorial(numero):
    fatorial = 1

    if numero <= 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# Mutante 2 (* -> +)
def fatorial_m2(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial += i

    return fatorial


# =========================
# FUNÇÃO 3 - maior
# =========================

# Mutante 1 (> -> <)
def maior(a, b):
    if a < b:
        return a
    else:
        return b


# Mutante 2 (> -> >=)
def maior_m2(a, b):
    if a >= b:
        return a
    else:
        return b


# =========================
# FUNÇÃO 4 - media
# =========================

# Mutante 1 (+ -> -)
def media(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma -= n

    return soma / len(numeros)


# Mutante 2 (< -> <=)
def media_m2(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n <= 0:
            raise ValueError("Valor inválido")
        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 5 - primo
# =========================

# Mutante 1 (<= -> >=)
def primo(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero >= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# Mutante 2 (+= -> *=)
def primo_m2(numero):
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

        i *= 1