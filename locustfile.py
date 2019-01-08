import os
import string
import random
from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    # @task(1000)
    # def index(self):
    #     response = self.client.get("/community/weather/46")

    # This task will 3 times for every 1000 runs of the above task
    # @task(3)
    # def about(self):
    #     self.client.get("/blog")

    # This task will run once for every 1000 runs of the above task
    # @task(1)
    # def about(self):
    #     id = id_generator()
    #     self.client.post("/signup", {"email": "example@example.com", "name": "Test"})

    # @task(1)
    # def get_something_else(self):
    #     self.client.get("/community/weather/127")

    @task
    def outdex(self):
        self.client.get("/community/event/index?fromDate=2018-08-31T23:59:59-05:00&toDate=2018-07-20+20:21:39&universityId=7&userId=14922")

    @task
    def index(self):
        self.client.get("/community/event/index?fromDate=2018-08-31T23:59:59-05:00&toDate=2018-07-20+20:21:39&universityId=7&userId=6074")

    @task
    def get_two_things(self):
        self.outdex()
        self.index()

class MyLocust(HttpLocust):
    # host = os.getenv('TARGET_URL', "http://unibees-prod.ebmkyntrr4.us-west-2.elasticbeanstalk.com////")
    task_set = MyTaskSet
    min_wait = 45
    max_wait = 50
