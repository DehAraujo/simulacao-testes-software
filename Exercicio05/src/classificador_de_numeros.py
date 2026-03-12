#Classifica número em: negativo, zero ou positivo
def classificar(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"