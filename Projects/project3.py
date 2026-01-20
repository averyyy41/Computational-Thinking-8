import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -100
y1 = 100
x2 = -100
y2 = 50
x3 = -100
y3 = 0
x4 = -100
y4 = -50


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("ocean_1")
t1 = create_sprite("fish_1",x1,y1)
t2 = create_sprite("fish_2",x2,y2)
t3 = create_sprite("fish_3",x3,y3)
t4 = create_sprite("fish_4",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(22):
    x1 += 10
    x2 += 12
    x3 += 14
    x4 += random.choice(5,5,5,5,5,5,5,16)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)
#the blue fish almost always wins because 14 is bigger than 10, 12, and 5 but on the off chance that the green fish wins, it is be 16 is the biggest possible number

# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print("player 3 wins!")
elif x4 >= x1 and x4 >= x3 and x4 >= x3:
    print("player 4 wins!")

turtle.exitonclick()