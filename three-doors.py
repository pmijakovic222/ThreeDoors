print("Warning: kinda scary!")
print("Three doors game!")
print("")
print("You found yourself in front of 3 doors...")
print("left one is red and made of metal...")
print("one in the middle is blue and wooden...")
print("right one is all in blood and plastic...")
print("")
print("Which one do you pick?")

pick1 = input()
print("")

for i in range(10000):
    if pick1 == "left" or pick1 == "l":
        print("You are in future now...")
        print("you see ten people working in their office...")
        print("everybody starts looking at you...")
        print("turns out these are not people but robots...")
        print("")
        print("You can: escape through the door you came from, try to talk to robots or attack one of the robots.")
        print("What do you do?")
        pick2 = input()
        print("")
    
        if pick2 == "escape" or pick2 == "e":
            print("You are now back in your house...")
            print("robots followed you...")
            print("they kill you and everyone in house...")
            print("robotic take over happened 100 years before it should have happened...")
            print("because of you...")
            print("end")
            break
    
        elif pick2 == "talk" or pick2 == "t":
            print("You tried to talk to them...")
            print("one of them answered you...")
            print("but the others...")
            print("killed you...")
            print("end")
            break

        elif pick2 == "attack" or pick2 == "a":
            print("You attacked the first one you saw...")
            print("you successfully killed (or whatever you do to rebots) him...")
            print("but the others attacked you...")
            print("it's nine on one so they easily killed you...")
            print("end")

        else:
            print("Please, type in: 'escape', 'talk' or 'attack'!")
            print("")
            continue
    elif pick1 == "middle" or pick1 == "m":
        print("You are in past now...")
        print("you see ten people peacfully eating..")
        print("you ask them where are you...")
        print("instead of answer you get a question...")
        print("'What is behind you?', they ask...")
        print("you say you do not know...")
        print("they ask you to leave...")
        print("you: go back through the door you came from or just leave the house and go outside?")
        pick3 = input()
        print("")
        if pick3 == "back" or pick3 == "b":
            continue
        elif pick3 == "leave" or pick3 == "l":
            print("You found yourself in the woods...")
            print("wolf came and killed you...")
            print("end")
            break
        else:
            print("Please type in: 'back' or 'leave'")
            print("")
            continue

    elif pick1 == "right" or pick1 == "r":
        print("You probbably wanted adventure choosing this door...")
        print("which is why i do not give you it...")
        print("you are back to your normal life...")
        print("and nothing like this happens to you ever again")
        print("end")
        break

    elif pick1 == "stop" or pick1 == "s":
        print("Ok i will!")
        break
    
    else:
        print("Please type in 'left', 'middle', 'right' or 'stop'")
        continue
    
