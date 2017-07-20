start = '''
You're running through the forest. There are wolves chasing you. There are two paths ahead of you, one goes left, and the other right. Which path do you choose?
'''


print(start)


#print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You run down the left path. Further down the path you see a mountain of rocks blocking the way. You can either climb the mountain on run through the trees.")
    use = input()
    if use == "climb the mountain":
        print("You scale up the mountain. When you reach the top you notice the sound of the wolves has gotten quieter. You look down and realise, wolves can't climb! You have escaped!")

    elif use == "run through the trees":
        print("You dash into the trees without looking, and you trip over a root that is sticking out of the ground. The Wolves surrond you and tear you apart. You have died!")

    else:
        print("You died because you put the wrong thing. Try either climb the mountain or run through the trees")

 
elif user_input == "right":
    print("You choose to go right and you see a giant lake. You can either swim through the lake, or go around.")
    use = input()
    if use == "swim through the lake":
        print("you dive into the lake and swim as fast as you can, but the wolves don't follow you. Wolves can't swim! You live!")

    elif use == "go around":
        print("You were too slow. You were eaten by the wolves.")

    else:
        print("You died because you put in the wrong thing. Try either go around or swim through the lake.")


else:
    print("You died because you put the wrong thing. Try either left or right")
