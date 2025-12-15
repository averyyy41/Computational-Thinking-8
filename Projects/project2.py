ponyboy_points=0
johnny_points=0
dally_points=0
soda_points=0
steve_points=0
two_bit_points=0

answer1=input("what is the best activity? A reading B being with your friends C causing trouble D riding horses E eating or F watching tv?")
if answer1 == "A" or answer1 == "a":
    ponyboy_points += 1
elif answer1 == "B" or answer1 == "b": 
    johnny_points += 1
elif answer1 == "C" or answer1 == "c":
    dally_points += 1
elif answer1 == "D" or answer1 == "d":
    soda_points += 1
elif answer1 == "E" or answer1 == "e":
    steve_points += 1
elif answer1 == "F"or answer1 == "f":
    two_bit_points += 1

answer2=input("Do you like to fight? A yes and B no")
if answer2 == "A" or answer2 == "a" or answer2 == "no":
    dally_points += 1
    soda_points += 1
    steve_points += 1
    two_bit_points += 1
elif answer2 == "B" or answer2 == "b" or answer2 == "yes":
    ponyboy_points += 1
    johnny_points += 1

answer3= input("What word describes you the best? A smart B kind C tough D beautiful E hungry or F silly")
if answer3 == "A" or answer3 == "a":
    ponyboy_points += 1
elif answer3 == "B" or answer3 == "b": 
    johnny_points += 1
elif answer3 == "C" or answer3== "c":
    dally_points += 1
elif answer3 == "D" or answer3 == "d":
    soda_points += 1
elif answer3 == "E" or answer3 == "e":
    steve_points += 1
elif answer3 == "F"or answer3 == "f":
    two_bit_points += 1

answer4=input("What food is the best? A Diet coke B burgers C soda D pancakes E chocolate cake")
if answer4 == "A" or answer4 == "a":
    ponyboy_points += 1
elif answer4 == "B" or answer4 == "b": 
    johnny_points += 1
elif answer4 == "C" or answer4 == "c":
    dally_points += 1
elif answer4 == "D" or answer4 == "d":
    soda_points += 1
elif answer4 == "E" or answer4 == "e":
    steve_points += 1
    two_bit_points += 1

answer5=input("What is your favorite color? A sunset colors B Gold C whats color? D red E blue or F RAINBOW")
if answer5 == "A" or answer5 == "a":
    ponyboy_points += 1
elif answer5 == "B" or answer5 == "b": 
    johnny_points += 1
elif answer5 == "C" or answer5== "c":
    dally_points += 1
elif answer5 == "D" or answer5 == "d":
    soda_points += 1
elif answer5 == "E" or answer5 == "e":
    steve_points += 1
elif answer5 == "F"or answer5 == "f":
    two_bit_points += 1

print(f"your score is {ponyboy_points} ponyboy, {johnny_points} johnny, {dally_points} dallas, {soda_points} sodapop, {steve_points} steve, and {two_bit_points} two bit!")

if ponyboy_points > johnny_points and ponyboy_points > dally_points and ponyboy_points > soda_points and ponyboy_points > steve_points and ponyboy_points > two_bit_points:
    print("u are most like Pony!!")
elif johnny_points > ponyboy_points and johnny_points > dally_points and johnny_points > soda_points and johnny_points > steve_points and johnny_points > two_bit_points:
    print("u are most like Johnny!!")
elif dally_points > ponyboy_points and dally_points > johnny_points and dally_points > soda_points and dally_points > steve_points and dally_points > two_bit_points:
    print("u are most like Dally!!")
elif soda_points > ponyboy_points and soda_points > johnny_points and soda_points > dally_points and soda_points > steve_points and soda_points > two_bit_points:
    print("u are most like Soda!!")
elif steve_points > ponyboy_points and steve_points > johnny_points and steve_points > dally_points and steve_points > soda_points and steve_points > two_bit_points:
    print("u are most like Steve!!")
elif two_bit_points > ponyboy_points and two_bit_points > johnny_points and two_bit_points > dally_points and two_bit_points > soda_points and two_bit_points > steve_points:
    print ("u are most like Two Bit!!")
else:
    print("u are a perfect combo of all the characters!!")
          
