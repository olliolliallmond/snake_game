from turtle import Turtle
import random

RANGE = 270


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("violet")
        self.speed("fastest")
        self.refresh()

        # rand_x = random.randint(-RANGE, RANGE)
        # rand_y = random.randint(-RANGE, RANGE)
        # self.goto(x=rand_x, y=rand_y)

    def refresh(self):
        rand_x = random.randint(-RANGE, RANGE)
        rand_y = random.randint(-RANGE, RANGE-25)
        self.goto(x=rand_x, y=rand_y)

# End of file
