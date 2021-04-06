import turtle 
import random

# Functions: a group of related statements that perform a specific task 
# functions help us breakdown our program into sections 
# DRY: Don't Repeat Yourself 
# Formula: 
# def functionName (parameters): 
#   BODY 
#   optional 'return' statement 

celine = turtle.Turtle() 
trevor = turtle.Turtle() 
aaron = turtle.Turtle()
emma = turtle.Turtle() 
arnav = turtle.Turtle() 

def drawTrack(length): 
  cameraMan = turtle.Turtle() 
  cameraMan.shape("triangle")

  cameraMan.penup() 
  cameraMan.goto(-175, 140)
  cameraMan.speed(0)

  for i in range(length): 
    cameraMan.write(i)
    cameraMan.right(90)
    cameraMan.forward(20)
    cameraMan.pendown() 
    cameraMan.forward(200)
    cameraMan.left(180)
    cameraMan.penup()
    cameraMan.forward(220)
    cameraMan.right(90)
    cameraMan.forward(20)
  cameraMan.hideturtle() 

def createTurtles(): 
  celine.shape("turtle")
  celine.penup() 
  celine.goto(-200, 100)
  celine.color("gold") 

  trevor.shape("turtle")
  trevor.penup() 
  trevor.goto(-200, 60)
  trevor.color("red") 
 
  aaron.shape("turtle")
  aaron.penup() 
  aaron.goto(-200, 20)
  aaron.color("blue") 

  emma.shape("turtle")
  emma.penup() 
  emma.goto(-200, -20)
  emma.color("yellow") 

  arnav.shape("turtle")
  arnav.penup() 
  arnav.goto(-200, -60)
  arnav.color("silver") 

def startRace(): 
  celine.pendown() 
  trevor.pendown()
  aaron.pendown() 
  emma.pendown() 
  arnav.pendown() 

  for i in range(40): 
    celine.forward(random.randint(1,15))
    trevor.forward(random.randint(1,15))
    aaron.forward(random.randint(1,15))
    emma.forward(random.randint(1,15))
    arnav.forward(random.randint(1,15))

drawTrack(16) # function call 
createTurtles()
startRace() 
