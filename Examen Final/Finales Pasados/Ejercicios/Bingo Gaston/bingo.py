import random

class Bingo:
    def __init__(self, bigger_ball, bombo, balls_left, last_ball, leng_carton):
        self.bigger_ball = bigger_ball
        self.bombo = bombo
        self.balls_left = balls_left
        self.last_ball = last_ball
        self.leng_carton = leng_carton

    def random_ball(self):
        ball = random.choice(self.bombo)
        self.balls_left.append(ball)
        self.bombo.remove(ball)
        return ball


