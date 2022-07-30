from turtle import Turtle

LEVEL_BOARD_POS = (-280, 260)
FONT = ("Consolas", 18, "normal")

class LevelBoard(Turtle):
    def __init__(self, level):
        super(LevelBoard, self).__init__()
        self.clear()
        self.level = level
        self.penup()
        self.goto(LEVEL_BOARD_POS)
        self.hideturtle()
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

class GameOverBoard(Turtle):
    def __init__(self):
        super(GameOverBoard, self).__init__()
        self.penup()
        self.hideturtle()
        self.write("GAME OVER", False, align="center", font=FONT)
