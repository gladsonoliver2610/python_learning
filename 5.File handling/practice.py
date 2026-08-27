# import turtle
# import math
# import random
# screen = turtle.Screen()
# screen.bgcolor("black")
# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.pensize(1)
# colors = ["red", "blue", "lime",
#            "yellow", "cyan", "magenta", "orange",
#            "pink"]
# for i in range(120):
#     t.penup()
#     t.goto(0, 40)
#     angle = (math.pi * 2) / 120
#     x = 16 * (math.sin(angle) ** 3) * 15
#     y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
#     c = random.choice(colors)
#     t.color(c)
#     t.pendown()
#     t.goto(x, y)
#     for _ in range(8):
#        t.forward(6)
#        t.backward(6)
#        t.right(45)
# turtle.done()

# import turtle
# import math
# import random

# screen = turtle.Screen()
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()
# t.pensize(1)

# colors = ["red", "blue", "lime",
#           "yellow", "cyan", "magenta", "orange",
#           "pink"]

# for i in range(120):
#     t.penup()
#     t.goto(0, 40)
#     angle = (math.pi * 2) / 120
#     x = 16 * (math.sin(angle) ** 3) * 15
#     y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * 15
#     c = random.choice(colors)
#     t.color(c)
#     t.pendown()
#     t.goto(x, y)
#     for _ in range(8):
#         t.forward(6)
#         t.backward(6)
#         t.right(45)

# turtle.done()

# f=open("classwork.txt","w")
# f.write("Learning Python File Handling")
# f.close()
# with open("classwork.txt","r") as file:
#     content=file.readline(11)
#     print(content)
# with open("advice.txt","w") as file:
#     file.writelines(["1.save energy\n", "2.save earth\n", "3.save life"])


# with open("advice.txt","r") as file:
#     content=file.readlines()
#     # print(content)
#     for i in content[0:1]:
#         print(i)

numlist=[1,2,3,4,5,6,7,8]
print(numlist[3:5])