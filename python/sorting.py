Slytherin = 0
Ravenclaw = 0
Gryffindor = 0
Hufflepuff = 0

start = '''
The strict proffesor in emerald green robes called names one by one, until she called your name. you walk up to the stool as the hat slips over your eyes.
"You shall be tested," a deep voice whispers in your ear, and suddenly, you were no longer in the great hall. You were in a room and the only thing in the
room was a door. After trying the door, you discover it to be locked. How do you open the door?
(you can knock, pick the lock, look for the key, or force the door.)'''


print(start)

user_input = input()
if user_input == "pick the lock":
    Slytherin = Slytherin + 1
    print("Using some paperclips in your pocket, you pick the lock. The door opens.")
elif user_input == "knock":
    Hufflepuff = Hufflepuff + 1
    print("You are not sure who opened the door, but you hear the click of a lock, and the door swings open.")
elif user_input == "look for the key":
    Ravenclaw = Ravenclaw + 1
    print("You feel around the door, and on top of the door molding, you find a key that was hidden from view. You use the key to leave the room.")
elif user_input == "force the door":
    Gryffindor = Gryffindor + 1
    print("You ram your body into the door until the door breaks and you are free of the room.")
else:
    print("You are forcefully ejected from the room and back into the Great Hall. The Hat then bellows that you are unworthy to attend Hogwarts and must leave. You are disgraced, and shamed the rest of your life.")
    
    
    
