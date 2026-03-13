import pytest

@pytest.fixture
def casos_validos():
    return [
        (1.0, "mesma_regiao", 100.0, 10.0),
        (3.0, "outra_regiao", 100.0, 22.5),
        (10.0, "internacional", 100.0, 50.0),
        (3.0, "mesma_regiao", 250.0, 0.0),
    ]