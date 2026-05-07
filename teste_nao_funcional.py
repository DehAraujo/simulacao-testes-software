import time
import requests


# =========================================
# TESTE DE DESEMPENHO
# =========================================

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


# =========================================
# TESTE DE SEGURANÇA
# =========================================

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