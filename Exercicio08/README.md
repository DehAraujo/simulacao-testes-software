# 🧪 Suíte de Testes para API REST

## 📌 API Escolhida

**Nome:** JSONPlaceholder
**Link:** https://jsonplaceholder.typicode.com/

---

## 🎯 Justificativa da Escolha

A API JSONPlaceholder foi escolhida por ser uma API pública, simples de usar e amplamente utilizada para testes. Ela permite realizar operações CRUD e validar diferentes cenários sem necessidade de autenticação complexa.

---

## ⚙️ Tecnologias Utilizadas

* Python
* requests
* pytest
* jsonschema

---

## 📦 Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. (Opcional) Crie um ambiente virtual:

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

---

## ▶️ Execução dos Testes

Para executar todos os testes:

```
pytest -v
```

Para executar e salvar o resultado:

```
pytest -v > resultado.txt
```

---

## 🧪 Testes Implementados

A suíte de testes cobre os seguintes cenários:

1. **GET coleção**

   * Verifica status code 200
   * Garante que a lista não está vazia

2. **GET recurso existente**

   * Verifica status 200
   * Valida o schema com jsonschema

3. **GET recurso inexistente**

   * Verifica retorno 404

4. **POST (Create)**

   * Cria novo recurso
   * Verifica status 201
   * Valida retorno com ID

5. **UPDATE (PUT/PATCH)**

   * Atualiza recurso existente
   * Verifica se o campo foi alterado

6. **DELETE**

   * Remove recurso
   * Verifica status 200 ou 204

7. **Validação de dados inválidos**

   * Envia dados incorretos
   * Espera erro 4xx

8. **Autenticação**

   * Testa acesso com e sem credenciais (quando aplicável)

9. **Uso de Fixture**

   * Criação e remoção automática de dados de teste

10. **Performance**

* Verifica se o tempo de resposta é menor que 2 segundos

---

## 📁 Estrutura do Projeto

```
Exercicio08/
│── test_api.py
│── requirements.txt
│── README.md
```

---

## ⚠️ Observações

* Não foram utilizadas ferramentas gráficas (Postman/Insomnia)
* Todos os testes foram implementados em Python
* Cada teste possui docstring explicando sua função
* Não foi utilizado `time.sleep()` sem justificativa

---

## 🚀 Conclusão

Esta suíte de testes garante a validação de funcionalidades essenciais de uma API REST, incluindo comportamento correto, tratamento de erros, desempenho e estrutura dos dados.

---
