from turtle import Turtle
ALIGN = "Center"
FONT = ('Courier', 15, 'normal')

file = open("high_score.txt")
highest_score = file.read()


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(highest_score)
        file.close()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt", mode="w") as file2:
            file2.write(str(self.high_score))
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
