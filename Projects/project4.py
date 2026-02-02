from re import I
import turtle, time, random
from utils import *
# the goal of the game is to fuel your body so you hve a lot of energy. 
# Section 1 - setup
# TODO - set a background using 
set_background("pilates")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
protein_bar = 0
energy_drinks = 0
energy = 5
talker1 = create_sprite("alien", -250, 200)
talker1.write(f"protein bar:{protein_bar}",font = ("Arial", 40, "normal"))
talker1.hideturtle()
talker2 = create_sprite("alien", -250, 150)
talker2.write(f"energy:{energy}",font = ("Arial", 40, "normal"))
talker2.hideturtle()
talker3 = create_sprite("alien", -250, 100)
talker3.write(f"energy drinks:{energy_drinks}",font = ("Arial", 40, "normal"))
talker3.hideturtle()




# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_protein_bar():
    global protein_bar
    protein_bar += 1
    x = random.randint (-200,200)
    y = random.randint (-200,200)
    create_sprite("protein_bar",x,y)
window.onkeypress(get_protein_bar,"p")
# When the p key is pressed you can get more protein bars to support your immune system and support your muscles

def get_energy_drinks():
    global energy_drinks, energy
    if energy <= 10:
        energy_drinks +=  1
        energy += 1
        x = random.randint (-200,200)
        y = random.randint (-200,200)
        create_sprite("energy_drinks",x,y)
window.onkeypress(get_energy_drinks,"e")
# When the e key is pressed you can get an energy drink to keep you focused and energized for the workout. 


        
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    talker1.clear()
    talker1.write(f"protein bar:{protein_bar}",font = ("Arial", 40, "normal"))
    talker2.clear()
    talker2.write(f"energy:{energy}",font = ("Arial", 40, "normal"))
    talker3.clear()
    talker3.write(f"energy drinks:{energy_drinks}",font = ("Arial", 40, "normal"))
    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()
    if i % 100 == 0:
        energy -= 1