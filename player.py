from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setpos(0, -280)
        self.seth(90)

    def move_up(self):
        self.forward(20)
        # print(self.pos())

    def move_down(self):
        self.backward(20)
        # print(self.pos())
