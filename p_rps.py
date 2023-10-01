#project1; rock paper scissors

import random

while True:
    print("Enter your choice;\n 1- Rock \n 2- Paper\n 3- Scissors\n")

    choice = int(input("Enter your choice: \n"))

    while choice>3 or choice<1:
        choice = int(input("please enter a valid choice"))

    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"


    print(f"User choice is {choice_name}\n")



    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    elif comp_choice == 3:
        comp_choice_name = "Scissors"

    print(f"Computer choice is {comp_choice_name}\n")

    print(choice_name, "vs", comp_choice_name)

    if choice == comp_choice:
        print("Its a Draw", end="")
        result = "DRAW"
    

    if choice == 1:
        if comp_choice==3:
            print ("Rock wins\nYou win.")
        elif comp_choice==2:
            print ("Paper wins\nYou lost.")

    elif choice == 2:
        if comp_choice==1:
            print ("Paper wins\nYou win.")
        elif comp_choice==3:
            print ("Scissors wins\nYou lost.")

    elif choice == 3:
        if comp_choice==2:
            print ("Scissors wins\nYou win.")
        elif comp_choice==1:
            print ("Rock wins\nYou lost.")

    print("Do you wanna play again? (y/n)")
    ans = input()
    if ans == "n":
        break