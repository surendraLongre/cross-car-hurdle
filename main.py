import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=1200)
screen.tracer(0)
player=Player()

game_is_on = True

# add key bindings
screen.listen()
screen.onkey(key="Up", fun=player.move_up)

#initialize car module
car=CarManager()

#initialize scoreboard
score=Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    #detect collision with the car
    for bus in car.all_cars:
        if bus.distance(player) < 40:
            game_is_on=False
            score.game_over()
    
    #detect successful cross
    if player.is_at_finish_line():
        player.goto_start()
        car.level_up()
        score.score_up()


screen.exitonclick()
