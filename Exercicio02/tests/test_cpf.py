import pytest
from Exercicio02.src.cpf import validar_cpf, formatar_cpf

#Teste fixture cpfs válidos
def test_validar_cpfs_validos(cpfs_validos):
    for cpf in cpfs_validos:
        assert validar_cpf(cpf) is True

#Teste fixture cpfs inválidos
def test_cpfs_invalidos_invalidos(cpfs_invalidos):
    for cpf in cpfs_invalidos:
        assert validar_cpf(cpf) is False

#Testes parametrizacao cpfs validos
@pytest.mark.parametrize("cpf, esperado ", [
    ("52998224725", True),
    ("16899535009" , True),
    ("45317828791", True),
    ("71460238001", True),
    ("39053344705", True),
    ("07353036656", True),
    ("20408790644", True),
    ("34114590854", True),
    ("23472448334", True),
])
def test_cpfs_parametrizados_validos(cpf, esperado):
    assert validar_cpf(cpf) is esperado

#Testes parametrizado cps validos com zero
@pytest.mark.parametrize("cpf, esperado", [
    ("07353036656", True),
    ("20408790644", True),
    ("34114590854", True),
    ("72429941600", True),
])
def test_cpf_parametrizados_comzero(cpf, esperado):
    assert validar_cpf(cpf) is esperado

#Testes parametrizado digitos verificadores errados
@pytest.mark.parametrize("cpf, esperado", [
    ("07353036659", False),
    ("20408790604", False),
    ("34114590874", False),
    ("72429941610", False),
])
def test_cpfs_digitos_verificadores_invalidos(cpf, esperado):
    assert validar_cpf(cpf) is esperado

#Testes cpfs com todos os digitos iguais
@pytest.mark.parametrize("cpf, esperado", [
    ("00000000000", False),
    ("11111111111", False),
    ("22222222222", False),
    ("33333333333", False),
    ("44444444444", False),
    ("55555555555", False),
    ("66666666666", False),
    ("77777777777", False),
    ("88888888888", False),
    ("99999999999", False),
])
def test_cpf_todos_digitos_iguais(cpf, esperado):
    assert validar_cpf(cpf) is esperado

#Testes cpfs com menos de 11 digitos
@pytest.mark.parametrize("cpf, esperado", [
    ("1", False),
    ("12", False),
    ("123", False),
    ("1234", False),
    ("12345", False),
    ("123456", False),
    ("1234567", False),
    ("12345678", False),
    ("123456789", False),
    ("1234567890", False),
])
def test_cpfs_com_menos_de_11_digitos(cpf, esperado):
    assert validar_cpf(cpf) is esperado

#Testes cpfs com mais de 11 digitos
@pytest.mark.parametrize("cpf, esperado", [
    ("123456789012", False),
    ("1234567890123", False),
    ("529982247251", False),
    ("168995350091", False),
    ("453178287911", False),
    ("714602380011", False),
    ("390533447051", False),
    ("821746530601", False),
])
def test_cpfs_parametrizados_invalidos(cpf, esperado):
    assert validar_cpf(cpf) == esperado

#Testes cpfs com letras
@pytest.mark.parametrize("cpf, esperado", [
    ("abcdefghijk", False),
    ("1234567890a", False),
    ("a2345678901", False),
    ("12345b78901", False),
    ("5299822472x", False),
    ("x2998224725", False),
    ("16899a35009", False),
    ("ABCDEF12345", False),
    ("123ABC78901", False),
    ("cpf12345678", False),
])
def test_cpfs_com_letras(cpf, esperado):
    assert validar_cpf(cpf) is False

#Testes formatação de cpfs válidos
@pytest.mark.parametrize("cpf, esperado", [
    ("52998224725", "529.982.247-25"),
    ("16899535009", "168.995.350-09"),
    ("45317828791", "453.178.287-91"),
    ("71460238001", "714.602.380-01"),
    ("39053344705", "390.533.447-05"),
    ("07353036656", "073.530.366-56"),
    ("20408790644", "204.087.906-44"),
    ("34114590854", "341.145.908-54"),
    ("23472448334", "234.724.483-34"),
])
def test_cpfs_validos_formatados(cpf, esperado):
    assert formatar_cpf(cpf) == esperado

#Teste formatação de cpf inválido
@pytest.mark.parametrize("cpf, esperado", [
    ("123456789012", False),
    ("1234567890123", False),
    ("000000000000", False),
    ("111111111111", False),
    ("529982247251", False),
    ("168995350091", False),
    ("453178287911", False),
    ("714602380011", False),
    ("390533447051", False),
    ("821746530601", False),
])
def test_cpfs_formatacao_invalida(cpf, esperado):
    with pytest.raises(ValueError):
        formatar_cpf(cpf)

#Teste cpf None
@pytest.mark.parametrize("cpf", [None])
def test_cpf_string_None(cpf):
    assert validar_cpf(cpf) is False
    
#Teste cpf string vazia
@pytest.mark.parametrize("cpf, esperado", [
('', False),
])
def test_cpf_string_vazia(cpf, esperado):
    assert validar_cpf('') is esperado