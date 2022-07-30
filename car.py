from turtle import Turtle
import random

colors = [("red", "black"), ("black", "purple"), ("green", "pink"), ("black", "red"), ("blue", "yellow")]
y_positions = [x for x in range(-220, 240, 20)]
speeds = [x for x in range(5, 20)]
cars = []


class Car(Turtle):

    def __init__(self, level):
        super(Car, self).__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=.9, stretch_len=random.randint(2, 4))
        self.color(*random.choice(colors))
        self.sety(random.choice(y_positions))
        self.setx(360)
        self.level = level
        self.velocity = random.choice(speeds * self.level)

    def move_car(self):
        self.seth(180)
        self.forward(self.velocity)
        # print(self.pos())


def create_cars(num_cars, level):
    cars.clear()
    for x in range(num_cars):
        car = Car(level)
        cars.append(car)
    print(len(cars))


def car_controller():
    for car in cars:
        car.move_car()
        if car.xcor() < -300:
            car.hideturtle()
            car.clear()
            cars.remove(car)
            car = Car(car.level)
            cars.append(car)

