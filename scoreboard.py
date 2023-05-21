from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.create()

    def create(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 16, 'bold'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align='center', font=('Arial', 16, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.create()

    def refresh(self):
        self.score += 1
        self.create()
