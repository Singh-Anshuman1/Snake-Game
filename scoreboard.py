from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())


        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 268)
        self.write(f"Score: {self.score} High Score:{self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset1(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.reset1()
        self.write(f"GAME OVER   ", align="center", font=("Arial", 14, "normal"))
