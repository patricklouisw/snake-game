from turtle import Turtle

MOVE_SEGMENT = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self, length = 3):
        self.segments = []
        self.create_snake(3)
        self.head = self.segments[0]

    def create_snake(self, length):
        for i in range(length):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=0 - i * MOVE_SEGMENT, y=0)
            self.segments.append(new_segment)

    def grow_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_tail_x = self.segments[-1].xcor()
        new_tail_y = self.segments[-1].ycor()
        if self.head.heading() == UP:
            new_tail_y -= MOVE_SEGMENT
        elif self.head.heading() == DOWN:
            new_tail_y += MOVE_SEGMENT
        elif self.head.heading() == LEFT:
            new_tail_x += MOVE_SEGMENT
        else:
            new_tail_x -= MOVE_SEGMENT
        new_segment.goto(x=new_tail_x, y=new_tail_y)
        self.segments.append(new_segment)

    def check_if_snake_hit_self(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def move_forward(self):
        for i in range(len(self.segments) - 1, 0, -1):
            curr_segment = self.segments[i]
            new_X = self.segments[i-1].xcor()
            new_Y = self.segments[i-1].ycor()
            curr_segment.goto(x=new_X, y=new_Y)
        self.segments[0].forward(MOVE_SEGMENT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

