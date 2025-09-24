from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())

        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.update_scoreboard()

    with open("highscore.txt", mode="r") as file:
        content = file.read()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode= "w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
