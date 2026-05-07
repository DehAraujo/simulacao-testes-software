# Projeto Calculadora — CC8550 Simulação e Teste de Software

Sistema de calculadora com repositório de histórico, desenvolvido para a Atividade 06 da disciplina CC8550 — Centro Universitário FEI.

## Estrutura do Projeto

```
projeto_calculadora/
├── src/
│   ├── calculadora.py
│   └── repositorio.py
├── tests/
│   ├── __init__.py
│   ├── test_unidade.py
│   ├── test_integracao.py
│   └── test_doubles.py
├── README.md
└── relatorio.md
```

## Como Executar

### Rodar os testes
```bash
python -m unittest discover tests -v
```

### Medir cobertura
```bash
python -m coverage run -m unittest discover tests
python -m coverage report -m
```
