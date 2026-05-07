# Relatório — Atividade 06: Testes de Unidade e Integração

**Disciplina:** CC8550 — Simulação e Teste de Software  
**Professor:** Luciano Rossi  
**Centro Universitário FEI — 1º Semestre de 2026**

---

## 1. Resultados dos Testes

Todos os 11 testes foram executados com sucesso:

```
test_mock_argumento (test_doubles.TestDoubles) ... ok
test_mock_potencia_bug_corrigido (test_doubles.TestDoubles) ... ok
test_mock_salvar_chamado (test_doubles.TestDoubles) ... ok
test_operacoes_sequenciais (test_integracao.TestIntegracao) ... ok
test_dividir (test_unidade.TestUnidade) ... ok
test_divisao_zero (test_unidade.TestUnidade) ... ok
test_multiplicar (test_unidade.TestUnidade) ... ok
test_potencia (test_unidade.TestUnidade) ... ok
test_soma (test_unidade.TestUnidade) ... ok
test_subtrair (test_unidade.TestUnidade) ... ok
test_tipo_invalido (test_unidade.TestUnidade) ... ok

Ran 11 tests in 0.008s — OK
```

---

## 2. Cobertura de Código

```
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src\calculadora.py            43      4    91%   16, 24, 32, 42
src\repositorio.py            11      2    82%   9, 12
tests\test_doubles.py         16      0   100%
tests\test_integracao.py      13      0   100%
tests\test_unidade.py         23      0   100%
--------------------------------------------------------
TOTAL                        106      6    94%
```

### Linhas não cobertas

- **calculadora.py** — linhas 16, 24, 32, 42: correspondem aos ramos de tipagem (`isinstance`) para o segundo argumento em `subtrair`, `multiplicar`, `dividir` e `potencia`. Esses ramos não foram exercitados individualmente pois o teste de tipo inválido cobriu apenas a operação `somar`. Para atingir 100%, seria necessário adicionar testes de tipo inválido para cada operação.
- **repositorio.py** — linhas 9 e 12: correspondem aos métodos `listar()` e `limpar()`. O teste de integração não chamou `listar()` diretamente, e `limpar()` não foi exercitado nos testes existentes.

---

## 3. Bug Encontrado e Corrigido

### Descrição do bug

No método `potencia` de `calculadora.py`, a string salva no repositório usava o operador `*` em vez de `**`:

```python
# Código com bug
self.repositorio.salvar(f"{base} * {expoente} = {resultado}")
```

Isso fazia com que o histórico registrasse, por exemplo, `2 * 3 = 8` para uma potenciação, o que é semanticamente incorreto e pode confundir o usuário ao consultar o histórico.

### Correção aplicada

```python
# Código corrigido
self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")
```

### Como o bug foi detectado

O bug foi identificado por meio do teste mock `test_mock_potencia_bug_corrigido`, que verificou o argumento exato passado ao método `salvar()`:

```python
def test_mock_potencia_bug_corrigido(self):
    self.calc.potencia(2, 3)
    self.mock_repo.salvar.assert_called_with("2 ** 3 = 8")
```

---

## 4. Diferença entre Stub e Mock na Prática

**Stub** é um substituto simples que permite controlar o estado retornado por um componente. No projeto, o `MagicMock` foi usado como stub quando o objetivo era apenas isolar a `Calculadora` do repositório real, sem verificar como o repositório foi chamado. O stub garante que o teste não dependa da implementação do `HistoricoRepositorio`, tornando os testes de unidade independentes e mais rápidos.

**Mock** vai além: além de substituir o componente, permite verificar *se* e *como* ele foi chamado — com quais argumentos, quantas vezes, e em qual ordem. No projeto, o mock foi essencial para detectar o bug em `potencia`, pois permitiu verificar o argumento exato passado a `salvar()`. Sem o mock, o bug passaria despercebido nos testes de unidade, já que o resultado numérico da operação estava correto.

Em resumo: o stub serve para controlar entradas e isolar dependências; o mock serve para verificar comportamentos e interações entre componentes.
