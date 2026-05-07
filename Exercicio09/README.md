<html>
<body>
<!--StartFragment--><html><head></head><body><h2></h2><h2> Testes Orientados a Objetos e Componentes</h2><p><strong>Disciplina:</strong> Simulação e Teste de Software (CC8550)<br><strong>Curso:</strong> Ciência da Computação – FEI<br><strong>Professor:</strong> Luciano Rossi</p><hr><h2> Objetivo do Exercício</h2><p>Desenvolver um sistema simples de gerenciamento de tarefas em Python e aplicar conceitos de testes orientados a objetos e componentes.</p><p>O foco é validar:</p><ul><li><p>Mudanças de estado dos objetos</p></li><li><p>Interação entre métodos</p></li><li><p>Uso de fixtures</p></li><li><p>Isolamento de dependências com mocks e stubs</p></li></ul><hr><h2> Conceitos Aplicados</h2><ul><li><p> Testes de Estado (verificar atributos)</p></li><li><p> Setup e Teardown com pytest (fixtures)</p></li><li><p> Testes de Ciclo de Vida do Objeto</p></li><li><p> Testes de Interação entre Métodos</p></li><li><p> Mock e Stub</p></li><li><p> Testes Unitários vs Testes de Componente</p></li></ul><hr><h2> Estrutura do Projeto</h2><pre><code class="language-id=&quot;estrutura09&quot;">task_manager/
│
├── task.py              # Classe Task (modelo da tarefa)
├── storage.py           # Armazenamento em memória
├── repository.py        # Lógica de persistência
├── service.py           # (Bônus) regras de negócio
│
├── tests/
│   ├── test_task.py     # Testes unitários da classe Task
│   ├── test_repository.py # Testes de componente (com mock)
│
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação
</code></pre><hr><h2> Descrição dos Arquivos</h2><h3>🔹 task.py</h3><p>Contém a classe principal do sistema.</p><p>Responsável por:</p><ul><li><p>Representar uma tarefa</p></li><li><p>Validar dados (título e prazo)</p></li><li><p>Controlar o estado (status)</p></li></ul><p>Inclui:</p><ul><li><p>Enum <code inline="">Priority</code></p></li><li><p>Enum <code inline="">Status</code></p></li><li><p>Classe <code inline="">Task</code></p></li></ul><hr><h3>🔹 storage.py</h3><p>Responsável por armazenar os dados em memória.</p><p>Implementa:</p><ul><li><p>add() → adiciona item</p></li><li><p>get() → busca item</p></li><li><p>get_all() → retorna todos</p></li><li><p>delete() → remove item</p></li><li><p>clear() → limpa tudo</p></li></ul><hr><h3>🔹 repository.py</h3><p>Gerencia a persistência das tarefas.</p><p>Responsável por:</p><ul><li><p>Atribuir ID às tarefas</p></li><li><p>Salvar tarefas</p></li><li><p>Buscar por ID</p></li><li><p>Listar todas</p></li><li><p>Remover tarefas</p></li></ul><hr><h3>🔹 service.py (Bônus)</h3><p>Camada opcional com regras de negócio.</p><p>Exemplo:</p><ul><li><p>Criar tarefa</p></li><li><p>Atualizar status</p></li><li><p>Listar tarefas</p></li></ul><hr><h2> Testes Implementados</h2><h3> test_task.py (Testes Unitários)</h3><ul><li><p>Verifica estado inicial</p></li><li><p>Valida título inválido</p></li><li><p>Valida prazo inválido</p></li><li><p>Testa mudança de status</p></li><li><p>Testa ciclo de vida da tarefa</p></li></ul><p> Sem uso de mock<br> Foco na classe isolada</p><hr><h3> test_repository.py (Testes de Componente)</h3><ul><li><p>Verifica atribuição de ID</p></li><li><p>Verifica chamada de métodos (mock)</p></li><li><p>Testa busca por ID</p></li><li><p>Testa sequência (save + find)</p></li><li><p>Testa lista vazia</p></li></ul><p> Usa <code inline="">Mock</code> para simular storage<br>Testa interação entre componentes</p><hr><h2> Tecnologias Utilizadas</h2><ul><li><p>Python 3</p></li><li><p>pytest</p></li><li><p>pytest-mock</p></li></ul><hr><h2> Instalação</h2><pre><code class="language-id=&quot;instalar09&quot;">pip install -r requirements.txt
</code></pre><hr><h2> Execução dos Testes</h2><pre><code class="language-id=&quot;executar09&quot;">pytest -v
</code></pre><hr><h2> Diferença Importante</h2>
Tipo de Teste | Descrição
-- | --
Unitário | Testa classe isolada
Componente | Testa interação com dependências

<hr><h2> Resultado Esperado</h2><p>Todos os testes devem passar:</p><pre><code class="language-id=&quot;resultado09&quot;">10+ passed
</code></pre><hr><h2> Conclusão</h2><p>Este projeto demonstra a aplicação prática de testes em sistemas orientados a objetos, garantindo confiabilidade, isolamento de dependências e validação correta do comportamento do sistema.</p><hr></body></html><!--EndFragment-->
</body>
</html>