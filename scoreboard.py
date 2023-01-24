from turtle import Turtle

class Scoreboard:
    def __init__(self, min_width, max_width, max_height):
        # Set Score
        self.text = Turtle()
        self.text.hideturtle()
        self.text.goto(x=min_width + 5, y=max_height)
        self.text.color("white")
        self.text.write("Score: 0", align="left", font=("Cooper Black", 15))

        # Set Line
        self.line = Turtle()
        self.line.hideturtle()
        self.line.color("white")
        self.line.penup()
        self.line.goto(x=min_width, y=max_height - 10)
        self.line.pendown()
        self.line.goto(x=max_width, y=max_height - 10)

    def change_score(self, new_score):
        self.text.clear()
        self.text.write(f"Score: {new_score}", align="left", font=("Cooper Black", 15))

    def game_over(self, end_score):
        self.text.clear()
        self.text.color("yellow")
        self.text.write(
            f"Score: {end_score}. GAME OVER!",
            align="left",
            font=("Cooper Black", 20))