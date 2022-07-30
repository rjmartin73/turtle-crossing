import time
from turtle import Screen
from player import Player
from car import car_controller, create_cars
from scoreboard import LevelBoard, GameOverBoard
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
    LevelBoard(level=lvl)
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_right, "Right")
    screen.onkey(player.move_left, "Left")
    create_cars(car_cnt, lvl)


def detect_collision():
    for t in screen.turtles():
        if t != player:
            if t.distance(player) < 20:
                print("Splat")
                GameOverBoard()
                return False
    return True


create_board(2 * level + 6, level)
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
