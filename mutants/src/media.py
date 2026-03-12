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
def media(numeros):
    args = [numeros]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_media__mutmut_orig, x_media__mutmut_mutants, args, kwargs, None)
def x_media__mutmut_orig(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_1(numeros):
    soma = None
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_2(numeros):
    soma = 1
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_3(numeros):
    soma = 0
    if numeros != []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_4(numeros):
    soma = 0
    if numeros == []:
        raise ValueError(None)
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_5(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("XXLista vaziaXX")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_6(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_7(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("LISTA VAZIA")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_8(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n <= 0:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_9(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 1:
            raise ValueError("Valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_10(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError(None)
        soma += n
    return soma / len(numeros)
def x_media__mutmut_11(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("XXValor inválidoXX")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_12(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("valor inválido")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_13(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("VALOR INVÁLIDO")
        soma += n
    return soma / len(numeros)
def x_media__mutmut_14(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma = n
    return soma / len(numeros)
def x_media__mutmut_15(numeros):
    soma = 0
    if numeros == []:
        raise ValueError("Lista vazia")
    
    for n in numeros:
        if n < 0:
            raise ValueError("Valor inválido")
        soma -= n
    return soma / len(numeros)
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