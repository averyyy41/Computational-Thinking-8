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
    #not higher than 14 or 15 so this one will be slower
    x2 += 12
    #not higher than 14 or 15 so this one will be slower
    x3 += 14
    #this one is usually the fastest but 1 out of 15 times will lose
    x4 += random.randint(5,15)
    #usually the slowest but if 15 is picked it will win 

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)
# the blue fish is the most likely to win bc 14 is larger than 10 and 12 but if the green fish goes to 15 instead instead of a more common lower number which is a one out of 15 chance, the green fish will win. 
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

turtle.exit_on_click()