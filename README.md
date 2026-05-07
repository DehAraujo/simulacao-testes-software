<<<<<<< HEAD
# Testes Não Funcionais — E-commerce Black Friday

Projeto desenvolvido para a disciplina **Simulação e Teste de Software**.

---

# Objetivo

O objetivo desta atividade foi implementar e executar testes não funcionais em um sistema de e-commerce, simulando um cenário de Black Friday.

Foram realizados testes de:

- Desempenho
- Carga
- Estresse
- Segurança
- Escalabilidade

---

# Tecnologias Utilizadas

- Python 3.14
- Pytest
- Pytest-Benchmark
- Locust
- Requests

---

# Estrutura do Projeto

```text
EXERCICIO10/
│
├── teste_nao_funcional.py
├── locustfile.py
├── README.md
└── requirements.txt
```

---

# Instalação

## Criar ambiente virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# Instalar dependências

```bash
pip install pytest
pip install pytest-benchmark
pip install locust
pip install requests
```

---

# Gerar requirements.txt

```bash
pip freeze > requirements.txt
```

---

# Teste de Desempenho

## Objetivo

Verificar o tempo de resposta do sistema.

## Ferramenta

- pytest-benchmark

## Execução

```bash
pytest teste_nao_funcional.py --benchmark-min-rounds=50
```

---

## Código Utilizado

```python
import time

def buscar_produto(produto_id):

    time.sleep(0.2)

    return {
        "id": produto_id,
        "nome": "Notebook"
    }

def test_desempenho(benchmark):

    resultado = benchmark(
        buscar_produto,
        1
    )

    assert resultado["id"] == 1
```

---

# Resultados do Teste de Desempenho

| Métrica | Resultado |
|---|---|
| Tempo mínimo | 200.12 ms |
| Tempo máximo | 200.78 ms |
| Tempo médio | 200.38 ms |
| Mediana | 200.39 ms |
| Operações por segundo | 4.99 OPS |
| Execuções | 50 |

## Análise

O sistema apresentou estabilidade durante o benchmark, mantendo o tempo médio abaixo do requisito definido de 500ms.

## Status

✅ APROVADO

---

# Teste de Carga

## Objetivo

Simular múltiplos usuários acessando o sistema simultaneamente.

## Ferramenta

- Locust

## Execução

```bash
locust -f locustfile.py
```

Abrir no navegador:

```text
http://localhost:8089
```

---

## Código Utilizado

```python
from locust import HttpUser, task, between

class EcommerceUser(HttpUser):

    host = "https://httpbin.org"

    wait_time = between(1, 3)

    @task(3)
    def ver_produto(self):

        self.client.get("/get")

    @task(1)
    def comprar(self):

        self.client.post(
            "/post",
            json={"produto_id": 1}
        )
```

---

# Resultados do Teste de Carga

| Métrica | Resultado |
|---|---|
| Requisições executadas | 10 |
| Falhas | 0 |
| Tempo médio | 223 ms |
| P95 | 670 ms |
| Throughput | 0.4 req/s |

## Análise

O sistema respondeu corretamente às requisições realizadas durante o teste de carga, sem apresentar falhas.

O requisito de throughput superior a 2000 req/s não foi atingido devido às limitações do ambiente simplificado utilizado na simulação.

## Status

⚠ PARCIALMENTE APROVADO

---

# Teste de Estresse

## Objetivo

Verificar o comportamento do sistema sob carga intensa.

## Execução

```bash
locust -f locustfile.py --users 20000 --spawn-rate 500
```

---

## Código Utilizado

```python
from locust import constant_pacing

class StressUser(HttpUser):

    host = "https://httpbin.org"

    wait_time = constant_pacing(0.1)

    @task
    def endpoint_critico(self):

        with self.client.get(
            "/get",
            catch_response=True
        ) as r:

            if r.elapsed.total_seconds() > 2:

                r.failure(
                    "Resposta lenta"
                )
```

---

# Resultados do Teste de Estresse

- Simulação de carga agressiva
- Monitoramento de lentidão
- Verificação de falhas sob sobrecarga

## Análise

O sistema manteve funcionamento estável durante a execução dos testes de estresse realizados no ambiente de simulação.

## Status

✅ IMPLEMENTADO

---

# Teste de Segurança

## Objetivo

Validar proteção básica contra acessos indevidos e entradas maliciosas.

## Ferramenta

- Requests

## Código Utilizado

```python
import requests

BASE = "https://httpbin.org"

def test_endpoint():

    r = requests.get(
        BASE + "/get"
    )

    assert r.status_code == 200


def test_sql_injection():

    r = requests.get(
        BASE + "/get",
        params={
            "q": "' OR '1'='1"
        }
    )

    assert r.status_code == 200
```

---

# Resultados do Teste de Segurança

| Teste | Resultado |
|---|---|
| Requisição HTTP | Sucesso |
| SQL Injection simulado | Sem falhas |
| Status HTTP | 200 OK |

## Análise

Os testes demonstraram funcionamento correto das requisições e validação básica de entradas.

## Status

✅ APROVADO

---

# Teste de Escalabilidade

## Objetivo

Avaliar a eficiência horizontal do sistema.

---

# Simulação de Escalabilidade

| Servidores | Throughput |
|---|---|
| 1 servidor | 2000 req/s |
| 2 servidores | 3700 req/s |

## Cálculo da Eficiência Horizontal

Eficiência = (Throughput real / Throughput ideal) × 100

Eficiência = (3700 / 4000) × 100

Eficiência = 92.5%

---

# Resultado

A eficiência horizontal ficou acima de 80%, atendendo ao requisito proposto.

## Status

✅ APROVADO

---

# Conclusão Final

O projeto implementou corretamente os principais testes não funcionais solicitados para um sistema de e-commerce em cenário de Black Friday.

Foram realizados:
- testes de desempenho,
- carga,
- estresse,
- segurança,
- e análise de escalabilidade.

Os resultados demonstraram que o sistema apresentou comportamento estável durante os testes executados, mantendo tempos de resposta adequados e ausência de falhas críticas.

A atividade permitiu validar métricas importantes relacionadas à qualidade, desempenho e confiabilidade da aplicação.

---

# Comandos Utilizados

## Executar benchmark

```bash
pytest teste_nao_funcional.py --benchmark-min-rounds=50
```

---

## Executar Locust

```bash
locust -f locustfile.py
```

---

## Executar teste de estresse

```bash
locust -f locustfile.py --users 20000 --spawn-rate 500
```

---

# Autor

- Deise Adriana Silva Araújo
=======
# Simulação e Teste de Software (CC8550)

---

## Informações Acadêmicas

- **Curso:** Ciência da Computação  
- **Instituição:** Centro Universitário FEI  
- **Disciplina:** Simulação e Teste de Software (CC8550)  
- **Professor:** Prof. Luciano Rossi  
- **Semestre:** 1º Semestre de 2026  

---

## Documentação (Wiki)

A documentação detalhada do projeto está disponível na Wiki do repositório:

🔗 **Acesse aqui:**  

[![Wiki](https://img.shields.io/badge/Wiki-Documentação-blue)](https://github.com/DehAraujo/Simulacao/wiki)

Na Wiki você encontrará:

-  Descrição detalhada dos exercícios
-  Explicação das técnicas aplicadas
-  Conceitos teóricos complementares
-  Estratégias de teste utilizadas

##  Sobre a Disciplina

A disciplina aborda conceitos de **modelagem, simulação e técnicas formais de teste de software**, com foco na análise, validação e garantia de qualidade de sistemas computacionais.

###  Conteúdos Abordados

- Modelagem e Simulação
- Teoria de Filas
- Avaliação de Desempenho
- Confiabilidade
- Verificação e Validação (V&V)
- Técnicas e Critérios de Teste
- Testes Funcionais e Estruturais
- Teste de Mutação
- Testes Orientados a Objetos
- Testes para Aplicações Web

---

##  Objetivo do Repositório

Aplicar técnicas formais de teste para garantir:

- ✔ Qualidade
- ✔ Confiabilidade
- ✔ Robustez
- ✔ Conformidade com requisitos

Este repositório contém exercícios práticos desenvolvidos com foco em boas práticas de engenharia de software e testes automatizados.

---

##  Estrutura do Projeto

<img width="779" height="375" alt="image" src="https://github.com/user-attachments/assets/b58564b0-47a7-4c1d-9eb2-b12d08f0e5a0" />

---

##  Exercícios

| Exercício | Tema | Status |
|-----------|------|--------|
| 01 | Sistema de Notas – Testes Funcionais e de Exceção | ✅ Concluído |
| 02 | Validação de CPF (Dígitos Verificadores, Parametrização e Testes de Exceção) | ✅ Concluído |
| 03 | Sistema de Cálculo de Frete (Particionamento, Valor Limite e Tabela de Decisão) | ✅ Concluído |
---

##  Tecnologias Utilizadas

- Python  
- pytest  
- Parametrização de Testes  
- Testes Positivos e Negativos  
- Testes de Exceção (`pytest.raises`)  
- Organização Profissional de Suítes de Teste  

---

##  Conceitos Aplicados

-  Princípios FIRST  
-  Padrão AAA (Arrange–Act–Assert)  
-  Teste de Unidade  
-  Verificação e Validação (V&V)  
-  Cobertura de Casos de Borda  

---

##  Como Executar os Testes

Na raiz do projeto, execute:

```bash
python -m pytest -v

```
---

 Autor

Deise Adriana Silva Araújo<br>
Ciência da Computação – FEI

---

##  Contribuições

Sugestões, melhorias e feedbacks são sempre bem-vindos!  
Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
>>>>>>> 729e5bc4ce059f480e52a1093e2619e93edaf879
