name = input("Ooo the one who seeks tell me your name :")
print(f"Welcome {name} to the land of the death")
level = input(f"Ooo Seeker {name} choose between these levels (easy,medium,hard)  :").lower()
if level == "easy":
    print(f"Welcome {name} as thought you will be here ;")
    choise =input("you have choice btw the village or the town deceide where you want to go :")
    if choise == "village":
        print(f"welcome {name} you are in the village now ")
        beginner_quest=input(f"you are given two quests you can choose between them (finding chicken or fixing shed)")
        if beginner_quest=="finding chicken":
            print(f"you have found the chicken {name}")
        elif beginner_quest=="fixing shed":
             print(f"you have fixed the shed {name}")

    else:
        print(f"welcome {name} you are in the town now ")

if level == "medium":
    print(f"Welcome {name} glad to see you here ;")
    choice = input(f"Now  then {name} you have two choices either you can go to border or yoy can goto army") 
    if choice == "border":
        print(f"welcome {name} you are in the border now ")
    else:
         print(f"welcome {name} you are in the army now ")
if level == "hard":
    print(f"Welcome {name} good to know you are not a chicken anymore  ;")
    choie=input(f"Now then {name} if you have chosen to be here you have only one choise  (main quest)") 
    if choie == "main quest":
        print(f"welcome {name} you have choosen the main quest now you have to go look for the sword of death :")
    