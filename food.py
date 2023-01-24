import random
from turtle import Turtle

FOOD_SIZE = 20

class Food:
    def __init__(self, min_height: int, max_height: int, min_width: int, max_width: int):
        self.min_width = min_width + FOOD_SIZE
        self.max_width = max_width - FOOD_SIZE
        self.min_height = min_height + FOOD_SIZE
        self.max_height = max_height - FOOD_SIZE

        self.coor_X = random.randrange(min_width + FOOD_SIZE, max_width - FOOD_SIZE, FOOD_SIZE)
        self.coor_Y = random.randrange(min_height + FOOD_SIZE, max_height - FOOD_SIZE, FOOD_SIZE)

        self.food = Turtle(shape="circle")
        self.food.color("salmon")
        self.food.resizemode("user")
        self.food.shapesize(.5, .5, .5)
        self.food.penup()
        self.food.goto(self.coor_X, self.coor_Y)

    def new_food_spawn(self):
        self.coor_X = random.randrange(self.min_width, self.max_width, FOOD_SIZE)
        self.coor_Y = random.randrange(self.min_height, self.max_height, FOOD_SIZE)
        self.food.goto(self.coor_X, self.coor_Y)
