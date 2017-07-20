
import turtle

sides = input("Number sides ?")
x = 0

print(type(sides))

for x in range(int(sides)):
    x+1
    turtle.forward(100)
    turtle.left(360/(int(sides)))
