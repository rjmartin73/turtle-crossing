from turtle import Turtle
import random

COLORS = [("red", "black"), ("black", "purple"), ("green", "pink"), ("black", "red"), ("blue", "yellow"),
          ("yellow", "blue"), ("orange", "green")]
Y_POSITIONS = [x for x in range(-220, 240, 20)]
SPEEDS = [x for x in range(5, 20)]
CARS = []


class Car(Turtle):

    def __init__(self, level):
        super(Car, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=.9, stretch_len=random.randint(2, 3))
        self.color(*random.choice(COLORS))
        self.sety(random.choice(Y_POSITIONS))
        self.setx(360)
        self.level = level
        self.velocity = random.choice(SPEEDS * self.level)

    def move_car(self):
        self.seth(180)
        self.forward(self.velocity)
        # print(self.pos())


def create_cars(num_cars, level):
    CARS.clear()
    for x in range(num_cars):
        car = Car(level)
        CARS.append(car)
    print(len(CARS))


def car_controller():
    for car in CARS:
        car.move_car()
        if car.xcor() < -300:
            car.hideturtle()
            car.clear()
            CARS.remove(car)
            car = Car(car.level)
            CARS.append(car)

