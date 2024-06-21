from turtle import Turtle

START = 0
STEP = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.color("purple")

    def create_segment(self, xcor, ycor):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        seg.setposition(x=xcor,
                        y=ycor)  # !! goto and setpos / setposition are aliases - they all do the same thing
        self.body.append(seg)

    def create_snake(self):
        x_cor = START
        for _ in range(3):
            self.create_segment(x_cor, START)
            x_cor -= STEP

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            nx = self.body[seg_num - 1].xcor()
            ny = self.body[seg_num - 1].ycor()

            self.body[seg_num].goto(x=nx, y=ny)
        self.head.forward(STEP)

    def add_segment(self):
        # last_seg_pos = len(self.body) - 1
        # last_seg = self.body[last_seg_pos]
        # print(last_seg)
        # nx = self.body[last_seg - 1].xcor()
        # ny = self.body[last_seg - 1].ycor()
        nx = self.body[len(self.body) - 1].xcor()
        ny = self.body[len(self.body) - 1].ycor()
        self.move()
        self.create_segment(xcor=nx, ycor=ny)

        # self.create_segment(xcor=nx, ycor=ny)

        # Redundant code - reformat later
        # seg = Turtle(shape="square")
        # seg.color("white")
        # seg.penup()
        # seg.setposition(x=nx, y=ny)
        # self.body.append(seg)

    # heading
    # 0 - right/east
    # 90 - up/north
    # 180 - left/west
    # 270 - down/south
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

# snake = []
# x_cor = 0
# for _ in range(3):
#     seg = Turtle(shape="square")
#     seg.color("white")
#     seg.penup()
#     seg.setposition(x=x_cor, y=0)  # !! goto and setpos / setposition are aliases - they all do the same thing
#     snake.append(seg)
#     x_cor -= 20
#
#
# class Snake:
#     def __init__(self):
#         self.segments = snake
#
#     def move(self):
#         for seg_num in range(len(snake) - 1, 0, -1):
#             nx = snake[seg_num - 1].xcor()
#             ny = snake[seg_num - 1].ycor()
#
#             snake[seg_num].goto(x=nx, y=ny)
#         snake[0].forward(20)
