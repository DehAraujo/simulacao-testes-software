class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def criar_tarefa(self, task):
        task.validar()
        return self.repository.save(task)

    def listar_todas(self):
        return self.repository.find_all()

    def atualizar_status(self, task, status):
        task.status = status
        return task