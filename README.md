# Locust

<aside>
💡 Locust是一款Python技术栈的开源的性能测试工具。Locust直译为蝗虫，寓意着它能产生蝗虫般成千上万的并发用户：
Locust是开源、使用Python开发、基于事件、支持分布式并且提供Web UI进行测试执行和结果展示的性能测试工具。

Locust使用Python代码定义测试场景，目前支持Python 2.7以上版本。它自带一个Web UI,用于定义用户模型，发起测试，实时测试数据，错误统计等，在最新未正式发布的v0.8a2(当前最新发布版本v0.8a1)，还提供QPS、评价响应时间等几个简单的图表。

</aside>

## 安装

1. 安装Python3.8及以上版本
2. pip install locust
3. locust -V , 目前是2.8.4版本

## 组件构成

<aside>
💡 Locust：如果说框架进行压力测试的方式是用一群蝗虫进行进攻，那么Locust类相当于一个蝗虫模板，而每一个locust实例就相当于其中的一个蝗虫，也就是一个用户、一个线程......。因此当我们使用框架进行压力测试时，*至少*需要存在一个Locust类，在指定了模拟用户的个数后，框架就会实例化相应多的Locust对象，从而实现对用户的模拟。

- TaskSet：测试场景，是由一系列的任务组成。我们需要使用一群蝗虫来进攻网站，但是如果蝗虫不知道进攻谁怎么进攻那也是白费力气，因此对蝗虫（模拟用户）我们需要告诉它们执行的任务是什么，也就是需要为每个Locust指定task_set
- HttpUser: 用于发送http请求，封装了get post delete等http常用命令
- task：任务，是TaskSet的一个最小单位
- client：客户端，由于框架主要是用于向website发动进攻，因此我们需要有一个客户端（可以是Http的，也可以是WebSocket等等）。客户端在Locust中被指定，然后会被传递到TaskSet中，因此在TaskSet可以直接使用self.client进行消息的发送和接收。
</aside>

## 参考教学视频

[https://www.youtube.com/watch?v=sPQjXbtIu68&ab_channel=PegasusWang](https://www.youtube.com/watch?v=sPQjXbtIu68&ab_channel=PegasusWang)

## 脚本代码（MVNO）

### 相关脚本项目文件：

[GitHub - kane1997/locust_scrypt](https://github.com/kane1997/locust_scrypt)

```python
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "https://konec-mvno-web-cpjfbnt2q-oppo-dev.vercel.app/"   #定义主机

    @task(1)
    def my_1_task(self):
        self.client.get("/support")   #请求support页面

    @task(2)
    def my_2_task(self):
        self.client.get("/plans")     #请求But a plan页面

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

    if __name__=='__main__':         #运行函数
        import os
        os.system('locust -f aaa.py')
```

### 测试脚本注释

- task_set：我们必须为每个蝗虫指定任务集，否则在这个蝗虫启动之后，它都不知道应该做什么，因此task_set属性是必须的
- min_wait、max_wait：每个任务执行后到下一个任务执行前的最小/最大等待时间
- host：客户端发送消息的主机地址
- wait_function：一个用于获取任务间等待时长的函数，默认是min_wait和max_wait中的随机值
- stop_timeout：Locust停止的秒数，如果为None，将不停止一直执行任务
- between：用于加载等待时间

## WEB.io 窗口

- 运行后进入web窗口进行测试：
- localhost:8089
- 或者：http://0.0.0.0:8089

![截屏2022-03-31 15.13.04.png](Locust%208fa1a/%E6%88%AA%E5%B1%8F2022-03-31_15.13.04.png)

## 测试结果展示

<aside>
💡 测试结果可以展示如下信息：
**Request, Fails, Median response time ,Average response time, min&max response time, Current RPS等信息**

</aside>

<aside>
💡 测试开始后，页面中会对消息请求进行统计，我们据此可获得被测网站的rps、响应时间等等，从而对被测系统进行性能上的分析。在Charts中可以看到图表化的数据趋势；在Failures和Exceptions中，能够看到消息发送失败或执行任务异常的具体信息；在Download Data中可以对统计结果进行下载。
****

</aside>

![Figure 3:Demo from Locust web.io](Locust%208fa1a/Untitled.png)

Figure 3:Demo from Locust web.io