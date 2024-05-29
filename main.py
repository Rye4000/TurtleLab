import turtle

#Change the background color to black
turtle.bgcolor("black")

#Adjust the speed of turtle
turtle.speed(2)

#List of colors
colors = ["#00ff9f", "#00b8ff", "#001eff", "#bd00ff", "#fcee0c"]

#Counter variables
colorNum = 0
size = 1

#Change this variable to control how many sides your shape will have
sides = 8
#Draw the square shape

#Draw the spiraling shape
#This loops forever
while (True):
  colorNum = colorNum + 1
  for i in range(sides):
    turtle.forward(size)
    turtle.right(360 / sides + .1)
    size = size + 1
  turtle.color(colors[colorNum % 5])
