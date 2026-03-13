# =========================
# FUNÇÃO 1 - classificar
# =========================
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def classificar(numero):
    args = [numero]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_classificar__mutmut_orig, x_classificar__mutmut_mutants, args, kwargs, None)
def x_classificar__mutmut_orig(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_1(numero):
    if numero <= 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_2(numero):
    if numero < 1:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_3(numero):
    if numero < 0:
        return "XXnegativoXX"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_4(numero):
    if numero < 0:
        return "NEGATIVO"
    elif numero > 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_5(numero):
    if numero < 0:
        return "negativo"
    elif numero >= 0:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_6(numero):
    if numero < 0:
        return "negativo"
    elif numero > 1:
        return "positivo"
    else:
        return "zero"
def x_classificar__mutmut_7(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "XXpositivoXX"
    else:
        return "zero"
def x_classificar__mutmut_8(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "POSITIVO"
    else:
        return "zero"
def x_classificar__mutmut_9(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "XXzeroXX"
def x_classificar__mutmut_10(numero):
    if numero < 0:
        return "negativo"
    elif numero > 0:
        return "positivo"
    else:
        return "ZERO"

x_classificar__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_classificar__mutmut_1': x_classificar__mutmut_1, 
    'x_classificar__mutmut_2': x_classificar__mutmut_2, 
    'x_classificar__mutmut_3': x_classificar__mutmut_3, 
    'x_classificar__mutmut_4': x_classificar__mutmut_4, 
    'x_classificar__mutmut_5': x_classificar__mutmut_5, 
    'x_classificar__mutmut_6': x_classificar__mutmut_6, 
    'x_classificar__mutmut_7': x_classificar__mutmut_7, 
    'x_classificar__mutmut_8': x_classificar__mutmut_8, 
    'x_classificar__mutmut_9': x_classificar__mutmut_9, 
    'x_classificar__mutmut_10': x_classificar__mutmut_10
}
x_classificar__mutmut_orig.__name__ = 'x_classificar'


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def fatorial(numero):
    args = [numero]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_fatorial__mutmut_orig, x_fatorial__mutmut_mutants, args, kwargs, None)


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_orig(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_1(numero):
    fatorial = None

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_2(numero):
    fatorial = 2

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_3(numero):
    fatorial = 1

    if numero <= 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_4(numero):
    fatorial = 1

    if numero < 1:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_5(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError(None)

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_6(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("XXNumero negativoXX")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_7(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("numero negativo")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_8(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("NUMERO NEGATIVO")

    for i in range(1, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_9(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(None, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_10(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, None):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_11(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_12(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, ):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_13(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(2, numero + 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_14(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero - 1):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_15(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 2):
        fatorial *= i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_16(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial = i

    return fatorial


# =========================
# FUNÇÃO 2 - fatorial
# =========================
def x_fatorial__mutmut_17(numero):
    fatorial = 1

    if numero < 0:
        raise ValueError("Numero negativo")

    for i in range(1, numero + 1):
        fatorial /= i

    return fatorial

x_fatorial__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_fatorial__mutmut_1': x_fatorial__mutmut_1, 
    'x_fatorial__mutmut_2': x_fatorial__mutmut_2, 
    'x_fatorial__mutmut_3': x_fatorial__mutmut_3, 
    'x_fatorial__mutmut_4': x_fatorial__mutmut_4, 
    'x_fatorial__mutmut_5': x_fatorial__mutmut_5, 
    'x_fatorial__mutmut_6': x_fatorial__mutmut_6, 
    'x_fatorial__mutmut_7': x_fatorial__mutmut_7, 
    'x_fatorial__mutmut_8': x_fatorial__mutmut_8, 
    'x_fatorial__mutmut_9': x_fatorial__mutmut_9, 
    'x_fatorial__mutmut_10': x_fatorial__mutmut_10, 
    'x_fatorial__mutmut_11': x_fatorial__mutmut_11, 
    'x_fatorial__mutmut_12': x_fatorial__mutmut_12, 
    'x_fatorial__mutmut_13': x_fatorial__mutmut_13, 
    'x_fatorial__mutmut_14': x_fatorial__mutmut_14, 
    'x_fatorial__mutmut_15': x_fatorial__mutmut_15, 
    'x_fatorial__mutmut_16': x_fatorial__mutmut_16, 
    'x_fatorial__mutmut_17': x_fatorial__mutmut_17
}
x_fatorial__mutmut_orig.__name__ = 'x_fatorial'


# =========================
# FUNÇÃO 3 - maior
# =========================
def maior(a, b):
    args = [a, b]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_maior__mutmut_orig, x_maior__mutmut_mutants, args, kwargs, None)


# =========================
# FUNÇÃO 3 - maior
# =========================
def x_maior__mutmut_orig(a, b):
    if a > b:
        return a
    else:
        return b


# =========================
# FUNÇÃO 3 - maior
# =========================
def x_maior__mutmut_1(a, b):
    if a >= b:
        return a
    else:
        return b

x_maior__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_maior__mutmut_1': x_maior__mutmut_1
}
x_maior__mutmut_orig.__name__ = 'x_maior'


# =========================
# FUNÇÃO 4 - media
# =========================
def media(numeros):
    args = [numeros]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_media__mutmut_orig, x_media__mutmut_mutants, args, kwargs, None)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_orig(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_1(numeros):
    soma = None

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_2(numeros):
    soma = 1

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_3(numeros):
    soma = 0

    if numeros != []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_4(numeros):
    soma = 0

    if numeros == []:
        raise ValueError(None)

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_5(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("XXLista vaziaXX")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_6(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_7(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("LISTA VAZIA")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_8(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n <= 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_9(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 1:
            raise ValueError("Valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_10(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError(None)

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_11(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("XXValor inválidoXX")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_12(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("valor inválido")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_13(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("VALOR INVÁLIDO")

        soma += n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_14(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma = n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_15(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma -= n

    return soma / len(numeros)


# =========================
# FUNÇÃO 4 - media
# =========================
def x_media__mutmut_16(numeros):
    soma = 0

    if numeros == []:
        raise ValueError("Lista vazia")

    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")

        soma += n

    return soma * len(numeros)

x_media__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_media__mutmut_1': x_media__mutmut_1, 
    'x_media__mutmut_2': x_media__mutmut_2, 
    'x_media__mutmut_3': x_media__mutmut_3, 
    'x_media__mutmut_4': x_media__mutmut_4, 
    'x_media__mutmut_5': x_media__mutmut_5, 
    'x_media__mutmut_6': x_media__mutmut_6, 
    'x_media__mutmut_7': x_media__mutmut_7, 
    'x_media__mutmut_8': x_media__mutmut_8, 
    'x_media__mutmut_9': x_media__mutmut_9, 
    'x_media__mutmut_10': x_media__mutmut_10, 
    'x_media__mutmut_11': x_media__mutmut_11, 
    'x_media__mutmut_12': x_media__mutmut_12, 
    'x_media__mutmut_13': x_media__mutmut_13, 
    'x_media__mutmut_14': x_media__mutmut_14, 
    'x_media__mutmut_15': x_media__mutmut_15, 
    'x_media__mutmut_16': x_media__mutmut_16
}
x_media__mutmut_orig.__name__ = 'x_media'


# =========================
# FUNÇÃO 5 - primo
# =========================
def primo(numero):
    args = [numero]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_primo__mutmut_orig, x_primo__mutmut_mutants, args, kwargs, None)


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_orig(numero):
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


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_1(numero):
    i = None

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


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_2(numero):
    i = 2

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


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_3(numero):
    i = 1

    if numero <= 0:
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


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_4(numero):
    i = 1

    if numero < 1:
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


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_5(numero):
    i = 1

    if numero < 0:
        raise ValueError(None)

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_6(numero):
    i = 1

    if numero < 0:
        raise ValueError("XXNumero invalidoXX")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_7(numero):
    i = 1

    if numero < 0:
        raise ValueError("numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_8(numero):
    i = 1

    if numero < 0:
        raise ValueError("NUMERO INVALIDO")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_9(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero < 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_10(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 2:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_11(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return True

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_12(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i < numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_13(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = None

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_14(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero / i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_15(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero or i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_16(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 or i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_17(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao != 0 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_18(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 1 and i != numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_19(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i == numero and i != 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_20(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i == 1:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_21(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 2:
            return False

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_22(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return True

        if i == numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_23(numero):
    i = 1

    if numero < 0:
        raise ValueError("Numero invalido")

    if numero <= 1:
        return False

    while i <= numero:
        divisao = numero % i

        if divisao == 0 and i != numero and i != 1:
            return False

        if i != numero:
            return True

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_24(numero):
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
            return False

        i += 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_25(numero):
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

        i = 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_26(numero):
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

        i -= 1


# =========================
# FUNÇÃO 5 - primo
# =========================
def x_primo__mutmut_27(numero):
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

        i += 2

x_primo__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_primo__mutmut_1': x_primo__mutmut_1, 
    'x_primo__mutmut_2': x_primo__mutmut_2, 
    'x_primo__mutmut_3': x_primo__mutmut_3, 
    'x_primo__mutmut_4': x_primo__mutmut_4, 
    'x_primo__mutmut_5': x_primo__mutmut_5, 
    'x_primo__mutmut_6': x_primo__mutmut_6, 
    'x_primo__mutmut_7': x_primo__mutmut_7, 
    'x_primo__mutmut_8': x_primo__mutmut_8, 
    'x_primo__mutmut_9': x_primo__mutmut_9, 
    'x_primo__mutmut_10': x_primo__mutmut_10, 
    'x_primo__mutmut_11': x_primo__mutmut_11, 
    'x_primo__mutmut_12': x_primo__mutmut_12, 
    'x_primo__mutmut_13': x_primo__mutmut_13, 
    'x_primo__mutmut_14': x_primo__mutmut_14, 
    'x_primo__mutmut_15': x_primo__mutmut_15, 
    'x_primo__mutmut_16': x_primo__mutmut_16, 
    'x_primo__mutmut_17': x_primo__mutmut_17, 
    'x_primo__mutmut_18': x_primo__mutmut_18, 
    'x_primo__mutmut_19': x_primo__mutmut_19, 
    'x_primo__mutmut_20': x_primo__mutmut_20, 
    'x_primo__mutmut_21': x_primo__mutmut_21, 
    'x_primo__mutmut_22': x_primo__mutmut_22, 
    'x_primo__mutmut_23': x_primo__mutmut_23, 
    'x_primo__mutmut_24': x_primo__mutmut_24, 
    'x_primo__mutmut_25': x_primo__mutmut_25, 
    'x_primo__mutmut_26': x_primo__mutmut_26, 
    'x_primo__mutmut_27': x_primo__mutmut_27
}
x_primo__mutmut_orig.__name__ = 'x_primo'