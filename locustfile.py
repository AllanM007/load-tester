from locust import HttpUser, task


class LoadTester(HttpUser):
    @task
    def test_load(self):
        self.client.get("/")