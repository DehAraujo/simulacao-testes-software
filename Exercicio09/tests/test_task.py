import pytest
from datetime import datetime, timedelta
from task_manager.task import Task, Priority, Status

@pytest.fixture
def task_valida():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Estudar", "Python", Priority.ALTA, prazo)

def test_estado_inicial(task_valida):
    task_valida.validar()
    assert task_valida.status == Status.PENDENTE

def test_titulo_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()

def test_prazo_invalido():
    prazo = datetime.now() - timedelta(days=1)
    task = Task(None, "Teste", "desc", Priority.BAIXA, prazo)
    with pytest.raises(ValueError):
        task.validar()

def test_mudar_status(task_valida):
    task_valida.status = Status.EM_PROGRESSO
    assert task_valida.status == Status.EM_PROGRESSO