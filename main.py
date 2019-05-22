import random

print('''welcome to the favourite game of the century :Rock-Paper-Scissor\n
Winning Rules of the Rock-paper-scissor game as follows:
# Rock vs paper->paper wins'
# Rock vs scissor->Rock wins
# paper vs scissor->scissor wins''')

ch = 'y'
ch2 = 'y'
while (ch == 'y' or ch == 'Y'):
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
    choice = int(raw_input("choose your option: "))
    while (choice > 3 or choice < 1):
        print("invalid choice")
        ch2 = raw_input("To continue playing press y and to end game press any other button ")
        if (ch2 == 'y' or ch2 == 'Y'):
            choice = int(raw_input("choose your option: "))
        else:
            break
    if (str.lower(ch2) != 'y'):
        break
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    print('you choose ' + choice_name)
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        print('computer choose ' + 'Rock')
    elif comp_choice == 2:
        print('computer choose ' + 'paper')
    elif comp_choice == 3:
        print('computer choose ' + 'scissor')
    if (choice == 1 and comp_choice == 3):
        print('you won')
    elif (choice == 2 and comp_choice == 1):
        print('you won')
    elif (choice == 3 and comp_choice == 2):
        print('you won')
    elif (choice == comp_choice):
        print("draw")
    else:
        print('you loose')

    print("Do you want to play again? (press y for yes and any other character for no)")
    ch = raw_input()

print("\nThanks for playing")
