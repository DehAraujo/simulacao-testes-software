import pytest
from unittest.mock import Mock
from datetime import datetime, timedelta
from task_manager.task import Task, Priority
from task_manager.repository import TaskRepository

@pytest.fixture
def mock_storage():
    return Mock()

@pytest.fixture
def repo(mock_storage):
    return TaskRepository(mock_storage)

@pytest.fixture
def task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "Teste", "desc", Priority.BAIXA, prazo)

def test_save_atribui_id(repo, task):
    result = repo.save(task)
    assert result.id == 1

def test_save_chama_storage(repo, task, mock_storage):
    repo.save(task)
    mock_storage.add.assert_called_once()

def test_find_by_id(repo, task, mock_storage):
    mock_storage.get.return_value = task
    result = repo.find_by_id(1)
    assert result == task

def test_find_all_vazio(repo, mock_storage):
    mock_storage.get_all.return_value = []
    assert repo.find_all() == []