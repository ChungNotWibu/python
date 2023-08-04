# === Bài 6 ===
import turtle 
num = int(input("Enter number plz: "))
pen = turtle.Turtle()
d = 180 - ( num - 2 )*180 / num  
for i in range (num):
    pen.forward(100)
    pen.left(d)

turtle.done
