from turtle import Turtle
import random

COLOR = ["gray", "purple", "sky blue", "yellow", "red", "blue", "orange"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Green")
        self.shapesize(1, 1)
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-285, 285)
        random_y = random.randint(-285, 285)
        self.color(random.choice(COLOR))
        self.goto(random_x, random_y)
