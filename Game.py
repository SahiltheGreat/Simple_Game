import turtle
import math
import random
import pygame
import time

#FOR  GENERATING SOUND ON HITTING TARGET
pygame.init()
pygame.mixer.music.load("point.wav")

#INITIALISING PLAYAREA
playarea= turtle.Screen()
playarea.bgcolor("black")

#SETTING BORDERS OF PLAYFIELD
borderpen = turtle.Turtle()
borderpen.penup()
borderpen.color("white")
borderpen.setposition(-300,-300)
borderpen.pendown()
borderpen.pensize(3)

for side in range(4):
    borderpen.forward(600)
    borderpen.left(90)
borderpen.hideturtle()


#INITIALISING THE PLAYER
player = turtle.Turtle()
player.color("green")
player.shape("triangle")
player.penup()
player.speed(0)


#INITIALISING THE TARGET
goal =turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))

#SETTING PLAYER SPEED
speed = 1


#DEFINING PLAYER FUNCTIONS
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed +=1

def decreasespeed():
    global speed
    speed -=1

def isCollision(p1,p2):
    d = math.sqrt(math.pow(p1.xcor()-p2.xcor(),2) + math.pow(p1.ycor()-p2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#FOR SCORE
score =0


#FOR USER INPUT
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")

#GAMEPLAY
while True:
    player.forward(speed)

    #CHECKING BORDER COLLISION
    if player.xcor()>300 or player.xcor()<-300:
        player.right(180)
    
    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)

    #CHECKING PLAYER-TARGET COLLISION
    if isCollision(player,goal):
        pygame.mixer.music.play()
        time.sleep(0)
        score +=1
        borderpen.undo()
        borderpen.penup()
        borderpen.color("yellow")
        borderpen.hideturtle()
        borderpen.setposition(-290,310)
        scorestring = "SCORE : %s" %score
        borderpen.write(scorestring,False, align="left", font =("Arial",14,"normal"))
        #print(score)
        goal.setposition(random.randint(-300,300),random.randint(-300,300))


