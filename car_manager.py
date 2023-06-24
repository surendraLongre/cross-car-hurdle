from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=2, stretch_len=5)
            new_car.penup()
            new_car.color(random.choice(COLORS))

            random_y=random.randint(-550, 550)
            new_car.goto(550, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def get_all_cars(self):
        return self.all_cars;

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT

