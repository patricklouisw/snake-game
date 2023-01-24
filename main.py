from time import sleep
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Global Variable
WIDTH = 600
HEIGHT = 600
min_height = -HEIGHT // 2
max_height = HEIGHT // 2 - 20
min_width = -WIDTH // 2
max_width = WIDTH // 2

# Set Screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Set Snake, Food, Scoreboard
snake = Snake()
food = Food(
    min_height=min_height,
    max_height=max_height,
    min_width=min_width,
    max_width=max_width,
)
scoreboard = Scoreboard(
    min_width=min_width,
    max_width=max_width,
    max_height=max_height
)

# Set Listener
screen.listen()
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="s", fun=snake.move_down)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

# Game Start
game_is_on = True
while game_is_on:
    screen.update()
    snake.move_forward()
    # If snake eat food
    if round(snake.head.xcor()) == food.coor_X and \
            round(snake.head.ycor()) == food.coor_Y:
        food.new_food_spawn()
        snake.grow_snake()

    # If snake hits wall or itself
    if round(snake.head.xcor()) == min_width or \
            round(snake.head.xcor()) == max_width or \
            round(snake.head.ycor()) == min_height or \
            round(snake.head.ycor()) == max_height or \
            snake.check_if_snake_hit_self():
        game_is_on = False
    scoreboard.change_score((len(snake.segments) - 3) * 10)
    sleep(0.12)

scoreboard.game_over((len(snake.segments) - 3) * 10)

screen.exitonclick()
