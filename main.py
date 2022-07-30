import random
import time
from turtle import Screen
from player import Player
from car import car_controller, create_cars
cars = []
level = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()


def create_board(car_cnt, lvl):
    lvl = lvl
    car_cnt = car_cnt
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    create_cars(car_cnt, lvl)


def detect_collision():
    for turtle in screen.turtles():
        if turtle != player:
            if player.distance(turtle) <=5:
                print("Hit")
            # print(turtle.shapesize()[1])
    return True


create_board(2 * level, level)


game_on = True
while game_on:
    car_controller()
    time.sleep(0.1)
    screen.update()
    game_on = detect_collision()

    if player.ycor() > 300:
        game_on = False
        level += 1
        screen.clearscreen()
        screen.tracer(0)
        player = Player()
        create_board(level * 3 + 10, level)
        game_on = True


screen.exitonclick()
