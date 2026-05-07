def verificar(n):
    if n > 0:
        if n % 2 == 0:
            return"ParPositivo"
        else:
            return"ImparPositivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Zero"

