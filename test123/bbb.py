from locust import HttpUser, TaskSet, task, between

UserName = [
    ("qamile1@gmail.com", "qamile"),
    ("qamile2@gmail.com", "qamile"),
    ("qamile3@gmail.com", "qamile"),
    ("qamile4@gmail.com", "qamile"),
    ("qamile5@gmail.com", "qamile")
]


class User(HttpUser):
    wait_time = between(5, 10)

    @task(1)
    def my_first_task(self):
        self.client.get("")


class tasks(TaskSet):
    def on_start(self):
        self.userName = "Not_exist"
        self.password = "Not_exist"
        if len(UserName) > 0:
            self.userName, self.password = UserName.pop()

    @task(2)
    def login_post(self):
        print(self.userName)
        self.client.post("/login.php", data={"action": "process", "userName": self.userName,
                         "password": self.password, "login.x": "16", "login.y": "9"})
