import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://konec-mvno-web-cpjfbnt2q-oppo-dev.vercel.app/"   #定义主机



    @task(1)
    def my_1_task(self):
        self.client.get("/support")   #请求support页面


    @task(2)
    def my_2_task(self):
        self.client.get("/plans")     #请求But a plant页面

    @task(3)
    def my_3_task(self):
        self.client.get("/coverage")   #请求coverage页面

    @task(4)
    def my_4_task(self):
        self.client.get("/about")     #请求Why us页面

    @task(5)
    def login(self):

        self.client.post(
            "/api/auth/login", {"username": "konecau002@gmail.com", "password": "Sps@123456"})

    @task(6)
    def my_6_task(self):
        self.client.get("/_next/data/5sSK9Ibf6E-Zf9cIdOh68/activation.json")







    if __name__=='__main__':
        import os
        os.system('locust -f aaa.py')
