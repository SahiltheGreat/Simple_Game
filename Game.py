import turtle
import math
import random
import pygame
import time

#FOR  GENERATING SOUND ON HITTING TARGET AND GAME-OVER
pygame.init()
s1=pygame.mixer.Sound("point.wav")
s2=pygame.mixer.Sound("gameover.wav")
#s3=pygame.mixer.Sound("bump.wav")

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


#TRADEMARK
borderpen.penup()
borderpen.color("green")
borderpen.setposition(-340,350)
trademarkstring = "MADE BY SAHIL BHATT. TRADEMARK OF SAHILCORP"
borderpen.write(trademarkstring,False, align="center", font =("Arial",20,"normal"))

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

#FOR SCORE
score =0

borderpen.penup()
borderpen.color("yellow")
borderpen.hideturtle()
borderpen.setposition(-290,310)
scorestring = "SCORE : %s" %score
borderpen.write(scorestring,False, align="left", font =("Arial",14,"normal"))


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


#FOR TIMER
class Timer(turtle.Turtle):
    def __init__(self,x,y,c,sec):
        turtle.Turtle.__init__(self)
        self.sec = sec
        self.pensize = 14
        #self.action = action
        self.ht()
        self.color(c)
        self.penup()
        self.goto(x,y)
        self.write(time.strftime("%H:%M:%S",time.gmtime(self.sec)),False,align="center",font=("Arial",self.pensize,"bold"))
    
    def start(self):
        self.clear()
        self.write(time.strftime("%H:%M:%S",time.gmtime(self.sec)),False,align="center",font=("Arial",self.pensize,"bold"))
        self.sec -=1
        if self.sec !=-1:
            playarea.ontimer(self.start,1000)
        else:
            #borderpen.penup()
            borderpen.color("red")
            borderpen.hideturtle()
            borderpen.setposition(0,-350)
            s2.play()
            time.sleep(0)
            finalstring = "GAME OVER ! YOUR FINAL SCORE  IS : %s" %score
            borderpen.write(finalstring,False, align="center", font =("Arial",30,"normal"))
            time.sleep(6)
            turtle.bye()


timer = Timer(0,310,"red",120)
timer.start()



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
        #s3.play()
        #time.sleep(0)
    
    if player.ycor()>300 or player.ycor()<-300:
        player.right(180)
        #s3.play()
        #time.sleep(0)

    #CHECKING PLAYER-TARGET COLLISION
    if isCollision(player,goal):
        s1.play()
        time.sleep(0)
        #FOR SCORE COUNTING AND PRINTING
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


