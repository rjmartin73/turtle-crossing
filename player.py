from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POS)
        self.seth(90)

    def move_up(self):
        self.seth(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.seth(90)
        self.backward(MOVE_DISTANCE)
        # print(self.pos())

    def move_right(self):
        self.setheading(0)
        if self.xcor() < 280:
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.seth(180)
        if self.xcor() > -280:
            self.forward(MOVE_DISTANCE)
