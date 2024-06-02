import simpy
import random


class Fork:
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.resource = simpy.Resource(env, capacity=1)


class Philosoph:
    def __init__(self, env, id, left_chopstick, right_chopstick, lambda_i, mi, deterministic=True):
        self.env = env
        self.id = id
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.lambda_i = lambda_i
        self.mi = mi
        self.deterministic = deterministic
        self.unsuccessful_attempts = 0
        self.eating_times = []
        self.request_times = []
        self.action = env.process(self.run())

    def eat(self):
        eating_duration = self.mi if self.deterministic else random.expovariate(1/self.mi)
        self.eating_times.append(eating_duration)
        yield self.env.timeout(eating_duration)

    def run(self):
        while True:
            inter_arrival_time = self.lambda_i if self.deterministic else random.expovariate(1/self.lambda_i)
            yield self.env.timeout(inter_arrival_time)
            self.request_times.append(self.env.now)
            with self.left_chopstick.resource.request() as left_req, self.right_chopstick.resource.request() as right_req:
                result = yield left_req | right_req
                if left_req in result and right_req in result:
                    yield self.env.process(self.eat())
                else:
                    self.unsuccessful_attempts += 1
                    if left_req in result:
                        self.left_chopstick.resource.release(left_req)
                    if right_req in result:
                        self.right_chopstick.resource.release(right_req)