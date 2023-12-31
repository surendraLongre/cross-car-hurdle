from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto_start()

    def move_up(self):
        self.forward(20)

    def is_at_finish_line(self):
        return self.ycor()>560

    def goto_start(self):
        self.goto(0, -580)

