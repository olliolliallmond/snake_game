from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=260)
        self.color("white")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.color("white")
        self.hideturtle()
        self.goto(x=0,y=0)
        self.write(f"Game Over.\nFinal Score: {self.score}", align=ALIGNMENT, font=FONT)

# END OF FILE
