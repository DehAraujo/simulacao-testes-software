from locust import HttpUser, task, between
from locust import constant_pacing


# =========================================
# TESTE DE CARGA
# =========================================

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


# =========================================
# TESTE DE ESTRESSE
# =========================================

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