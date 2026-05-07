def validar_cpf(cpf):
    valida_cpf = []
    soma_1 = 0
    soma_2 = 0
    cont = 10
    cont2 = 11
    contador = 1
    #Garante que seja numero
    #Verifica se string está vazia
    if not cpf:
        return False
    
    for digito in cpf:
        if(digito not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            return False
        else:
            valida_cpf.append(digito)

    #Garante que tenha 11 dígitos
    if(len(valida_cpf) != 11):
        return False
    
    #Garante que não são números repetidos 11111...
    if(cpf == valida_cpf[0] * 11):
        return False
    
    #Calculo do primeiro dígito verificador
    for digito in valida_cpf:
        if(cont >= 2 and cont <= 10):
            mult = int(digito) * cont
            soma_1 += mult
            cont -= 1
        else:
            break
    resto = soma_1 % 11
    
    if(resto < 2):
        if(int(valida_cpf[9]) != 0):
                return False
    else:
        if(int(valida_cpf[9]) !=  (11 - resto)):
            return False
    
    #Calculo do segundo dígito verificador
    for digito in valida_cpf:
        if(cont2 >= 2 and cont2 <= 11):
            mult = int(digito) * cont2
            soma_2 += mult
            cont2 -= 1
        else:
            break

    resto = soma_2 % 11

    if(resto < 2):
        if(int(valida_cpf[10]) != 0):
            return False
        else:
            return True
    else:
        if(int(valida_cpf[10]) !=  (11 - resto)):
            return False
        else:
            return True
 
def formatar_cpf(cpf):
    if(validar_cpf(cpf) == True):
        return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    else:
        raise ValueError("CPF inválido")

