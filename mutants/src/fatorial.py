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
def fatorial(numero):
    args = [numero]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_fatorial__mutmut_orig, x_fatorial__mutmut_mutants, args, kwargs, None)
def x_fatorial__mutmut_orig(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_1(numero):
    fatorial = None
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_2(numero):
    fatorial = 2
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_3(numero):
    fatorial = 1
    if numero <= 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_4(numero):
    fatorial = 1
    if numero < 1:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_5(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError(None)
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_6(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("XXNumero negativoXX")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_7(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("numero negativo")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_8(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("NUMERO NEGATIVO")
    
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_9(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(None, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_10(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, None):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_11(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_12(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, ):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_13(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(2, numero + 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_14(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero - 1):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_15(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 2):
        fatorial *= i
    return fatorial
def x_fatorial__mutmut_16(numero):
    fatorial = 1
    if numero < 0:
        raise ValueError("Numero negativo")
    
    for i in range(1, numero + 1):
        fatorial = i
    return fatorial
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