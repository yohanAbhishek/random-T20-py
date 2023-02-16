import finalizeGame  # |
import game  # Custom modules
import initialize  # |

import time

commence = False

while not commence:  # initial phase, needs to complete and can't run after starting the matches
    try:
        option = int(input("------------------------\n1. Add player \n2. View player profiles \n3. "
                           "Edit player profiles \n4. Commence game \n5. Exit program\n\nEnter option: "))  # Main menu

        if option == 1:  # Add profiles
            if initialize.terminate():
                print("\nAll profiles created successfully, Enter 4 to commence! ")
            else:
                initialize.addProfile()

        elif option == 2:  # View profile
            initialize.viewProfile()

        elif option == 3:  # Edit profiles
            initialize.editProfile()

        elif option == 4:  # Start game
            validation = input("\nYou won't be able to do any changes here on.\nEnter y if you still wish to continue: ")
            if validation.upper() == "Y":
                if initialize.terminate():
                    print('\n' * 50)
                    print("\n-- Game started --")
                    commence = True
                else:
                    print("\nPlease add all profiles to commence the game!")
                    commence = False

        elif option == 5:  # Exit program
            exit("You exited the program!")

        else:  # For option out of range 1-5
            print("Option out of range!")

    except ValueError:  # If a value is not a given data type
        print("Please enter a number!")

while True:
    menu = input("\n1. Start game\n2. View current top 5 batsman\n3. View current top 5 bowlers\n4. View tournament "
                 "standings\n5. Match summary\n6. Exit game\n\nEnter option: ")

    if menu == '1':
        if not finalizeGame.checkEnd():
            matchID = game.selectTeam()  # To select which teams to start match
            tossWin = game.toss(matchID)
            print(f"{tossWin[0]} won, and chose to {tossWin[2]}. {tossWin[1]} lost.")
            print(
                "\nThe game will start in 20 seconds and the match summary will be at the bottom. Scroll up if you wish"
                " to view each over individually.")
            time.sleep(20)
            game.executeGame(matchID, tossWin[0], tossWin[1])
            print("\n -- Second innings -- \n")
            game.executeGame(matchID, tossWin[1], tossWin[0])
            finalizeGame.summary(matchID)
        else:
            print('>> All matches have been played')

    elif menu == '2':
        finalizeGame.highestScoredBatsman()
    elif menu == '3':
        finalizeGame.highestWicketBowlers()
    elif menu == '4':
        finalizeGame.tournamentStanding()
    elif menu == '5':
        ID = finalizeGame.selectIdForSummary()
        finalizeGame.summary(ID)
        while True:
            Repeat = input("\nEnter y to view another summary: ")
            if Repeat.upper() == "Y":
                ID = finalizeGame.selectIdForSummary()
                finalizeGame.summary(ID)
            else:
                break
    elif menu == '6':
        exit('\n>> You exited the game')
    else:
        print("Invalid option")
