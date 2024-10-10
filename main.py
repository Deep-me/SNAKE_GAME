import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    #Detect collision with wall.
    if snake.head.xcor() >=295 or snake.head.xcor() <=-295 or snake.head.ycor() >=295 or snake.head.ycor() <=-295:
        score.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segment[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) <= 10:
            score.reset()
            snake.reset()
            

screen.exitonclick()