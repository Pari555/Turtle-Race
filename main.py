import turtle

cameraMan = turtle.Turtle()
cameraMan.shape("triangle")

cameraMan.penup()
cameraMan.goto(-175, 140)
cameraMan.speed(0)

for i in range(16):
  cameraMan.write(i)
  cameraMan.pendown()
  cameraMan.right(90)
  cameraMan.forward(200)
  cameraMan.left(180)
  cameraMan.forward(200)
  cameraMan.right(90)
  cameraMan.penup()
  cameraMan.forward(20)

