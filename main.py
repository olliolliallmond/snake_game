from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Retro Classic: Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
sb = ScoreBoard()

RANGE = 280
# Listen to keystrokes
screen.listen()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    # Body collision
    for seg in range(len(snake.body) - 1, 1, -1):
        seg_x = snake.body[seg].xcor()
        seg_y = snake.body[seg].ycor()

        hx = snake.head.xcor()
        hy = snake.head.ycor()

        if hx == seg_x and hy == seg_y:
            game_is_on = False
            food.reset()
            for s in range(len(snake.body - 1), 0, -1):
                snake.body[s].hideturtle()
            snake.head.hideturtle()
            screen.update()
            sb.game_over()

    # Food Collision
    if snake.head.distance(food) <= 15:
        # print("nom nom nom")
        snake.add_segment()
        sb.update_score()
        food.refresh()

    # Wall Collision
    if snake.head.xcor() > RANGE or snake.head.xcor() < -RANGE or snake.head.ycor() > RANGE or snake.head.ycor() < -RANGE:
        game_is_on = False
        print("Crashed into wall.")
        food.reset()
        for seg in range(len(snake.body) - 1, 0, -1):
            snake.body[seg].hideturtle()
        snake.head.hideturtle()
        screen.update()
        sb.game_over()
    # END OF WHILE LOOP
# food.reset()
# for seg in range(len(snake.body-1), 0, -1):
#     snake.body[seg].hideturtle()
# screen.update()
# sb.game_over()

screen.exitonclick()

# END OF FILE
