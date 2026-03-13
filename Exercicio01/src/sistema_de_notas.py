def validar_nota(nota): 
    if nota >= 0 and nota <= 10: 
        return True 
    else: 
        return False
        
def calcular_media(notas): 
    soma = 0 
    notas_validas = [] 
    notas_invalidas = [] 
    if not notas: 
        raise ValueError("Não há notas para calcular a média") 
    else: 
        for nota in notas: 
            if validar_nota(nota) == True: 
                notas_validas.append(nota) 
            else: 
                notas_invalidas.append(nota)
                if(nota < 0 or nota > 10): 
                    raise ValueError("Valor inválido")

    if len(notas_invalidas) == len(notas):
        raise ValueError("Não há notas válidas para calcular média")
    else:
        for nota in notas_validas:
            soma += nota
                           
        media = soma / len(notas_validas)
        return media

def obter_situacao(media): 
    if media >= 7 and media <= 10: 
        return "aprovado" 
    elif(media >= 5 and media < 7): 
        return "recuperacao" 
    elif(media >= 0 and media < 5): 
        return "reprovado" 
    else: 
        raise ValueError("Média inválida")

def calcular_estatisticas(notas):
    aprovados = 0 
    recuperacao = 0
    reprovados = 0
    notas_validas = []

    media = calcular_media(notas) 
        
    for nota in notas:
        if(validar_nota(nota) == True):
            notas_validas.append(nota)
            if(obter_situacao(nota) == "aprovado"):
                aprovados += 1
            elif(obter_situacao(nota) == "recuperacao"):
                recuperacao += 1
            elif(obter_situacao(nota) == "reprovado"):
                reprovados += 1
         
    maior = max(notas_validas) 
    menor = min(notas_validas)

    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "recuperacao": recuperacao,
        "reprovados": reprovados
    }

def normalizar_notas(notas, nota_maxima = 10):
    notas_normalizadas = []
 
    if nota_maxima <= 0:
        raise ValueError("Valor invalido")
    if not notas:
        return []
    for nota in notas:
        if nota < 0 or nota > nota_maxima:
            raise ValueError("Nota inválida")
        else:
            nota_normalizada =((nota / nota_maxima) * 10)
            notas_normalizadas.append(nota_normalizada)
    
    return notas_normalizadas

