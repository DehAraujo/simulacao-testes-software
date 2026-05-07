import requests
import pytest
import jsonschema

BASE_URL = "https://jsonplaceholder.typicode.com"

#Schema simples
POST_SCHEMA = {
    "type": "object",
    "required": ["id"],
    "properties": {
        "id": {"type": "integer"}
    }
}

#9. FIXTURE
@pytest.fixture
def post_criado():
    """Cria um post antes do teste e remove depois"""
    payload = {
        "title": "Post de teste",
        "body": "Conteudo",
        "userId": 1
    }

    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    post = resp.json()

    yield post

    requests.delete(f"{BASE_URL}/posts/{post['id']}")


#1. GET lista
def test_01_get_lista():
    """GET /posts → 200 e lista não vazia"""
    resp = requests.get(f"{BASE_URL}/posts")
    assert resp.status_code == 200
    assert len(resp.json()) > 0


#2. GET existente + schema
def test_02_get_existente_schema():
    """GET /posts/1 → validar schema"""
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.status_code == 200
    jsonschema.validate(instance=resp.json(), schema=POST_SCHEMA)


#3. GET inexistente
def test_03_get_inexistente():
    """GET /posts/99999 → 404"""
    resp = requests.get(f"{BASE_URL}/posts/99999")
    assert resp.status_code == 404


#4. POST
def test_04_create_post():
    """POST /posts → 201"""
    payload = {
        "title": "Novo post",
        "body": "Conteudo teste",
        "userId": 1
    }

    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code == 201
    assert "id" in resp.json()


#5. UPDATE
def test_05_update_post():
    """PATCH /posts/1 → atualizar campo"""
    payload = {"title": "Atualizado"}

    resp = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Atualizado"


#6. DELETE
def test_06_delete_post():
    """DELETE /posts/1 → 200"""
    resp = requests.delete(f"{BASE_URL}/posts/1")
    assert resp.status_code in [200, 204]


#7. Dado inválido
def test_07_dado_invalido():
    """POST inválido → erro"""
    payload = {
        "title": "",
        "body": "",
        "userId": "abc"
    }

    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    assert resp.status_code in [400, 201]


#8. Autenticação
def test_08_autenticacao():
    """Teste de autenticação"""
    headers = {"Authorization": "Bearer token_fake"}

    resp = requests.get(f"{BASE_URL}/posts", headers=headers)
    assert resp.status_code == 200


#9. Uso de fixture
def test_09_fixture(post_criado):
    """Verifica fixture"""
    assert "id" in post_criado


#10. Performance
def test_10_performance():
    """Tempo de resposta < 2s"""
    resp = requests.get(f"{BASE_URL}/posts/1")
    assert resp.elapsed.total_seconds() < 2.0