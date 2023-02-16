group = team = name = uniformNum = age = val = ""


# ------- Sub functions --------
def grpInp():
    global group, team
    group = ""
    while group not in ["A", "B"]:
        group = input("Enter group (A or B): ").upper()
        if group not in ["A", "B"]:
            print("Invalid group!")
    team = ""
    while team not in ["1", "2", "3", "4"]:
        team = input("Enter team (1,2,3,4): ")
        if team not in ["1", "2", "3", "4"]:
            print("Invalid team!")


def displayProfile(data):
    print('\n\n')
    print("_" * 84)
    print("| {:15}| {:30}| {:15}| {:15}|".format('Team ID', 'Player name', 'Uniform number', 'Age'))
    print("_" * 84)

    for profile in data:
        print("| {:15}| {:30}| {:15}| {:15}".format(profile.split(',')[0], profile.split(',')[1], profile.split(',')[2],
                                                    profile.split(',')[3]))
    print('\n\n')


def checkEmpty(check, item):
    while len(check) == 0:
        check = input(f"Enter valid {item}: ")


def inputForProfile():
    global name, uniformNum, age

    while True:
        name = input("Player name: ")
        if len(name) > 1:
            if all(word.isalpha() or word.isspace()for word in name):
                break
            
            else:
                print("Please enter only letters!\n")
        else:
            print("Please enter a valid name!")

    uniformNum = input("Uniform number: ")
    checkEmpty(uniformNum, "uniform number")

    while True:
        age = input("Age: ")
        if age.isalpha():
            print("Please enter only numbers!")
        elif int(age) < 15 or int(age) > 60:
            print("Please enter a valid age!")
        else:
            break

    checkEmpty(age, "age")


def saveProfile1(fileObject, largest, playerCount):  # after deleting profile
    if (int(largest) + 1) > 10:  # save input
        fileObject.write(
            f"{group + team + (str(playerCount + 1))},{name},{uniformNum},{age}\n")
    else:
        fileObject.write(
            f"{group + team + (str(playerCount + 1))},{name},{uniformNum},{age}\n")
    print(f"{name} added successfully!")
    fileObject.close()


def saveProfile2(fileObject, largest):  # normal
    if (int(largest) + 1) >= 10:  # save input
        fileObject.write(
            f"{group + team + (str(int(largest) + 1))},{name},{uniformNum},{age}\n")
    else:
        fileObject.write(
            f"{group + team + '0' + (str(int(largest) + 1))},{name},{uniformNum},{age}\n")
    print(f"{name} added successfully!")
    fileObject.close()


def editPlayer(toFind, toReplace):
    fo = open(f"Storage/Group{group}_profile/team_{team}.txt", "r")
    data = fo.read()
    data = data.replace(toFind, toReplace)
    fo.close()
    fo = open(f"Storage/Group{group}_profile/team_{team}.txt", "w")
    fo.write(data)
    fo.close()
    print("Edit successful!")


def terminate():
    global val
    for num in range(1, 5):
        fo1 = open(f"Storage/GroupA_profile/team_{num}.txt", "r")
        fo2 = open(f"Storage/GroupB_profile/team_{num}.txt", "r")

        data1 = fo1.readlines()
        data2 = fo2.readlines()

        if len(data1) >= 11 and len(data2) >= 11:
            val = True
        else:
            val = False
            break

    return val


# -------- Main functions --------
def addProfile():
    repeat = "Y"

    grpInp()  # Get input for group and team

    while repeat == "Y":
        fo = open(f"Storage/Group{group}_profile/team_{team}.txt", "r+")
        fo.seek(0)
        totalLines = fo.readlines()
        largest = 0
        for i in totalLines:
            playerNum = i[2:4]
            if int(playerNum) > int(largest):
                largest = playerNum
        fo.seek(0)
        playerCount = len(fo.readlines())
        if playerCount <= int(largest):
            if playerCount < 11 and repeat.upper() == "Y":  # Get input
                inputForProfile()
                saveProfile2(fo, largest)
        else:
            if playerCount < 11 and repeat.upper() == "Y":
                inputForProfile()
                saveProfile1(fo, largest, playerCount)

        if playerCount < 10:  # If player limit isn't reached ask to add other profiles
            repeat = input("Enter y to add another player: ").upper()

        else:  # If the maximum player count has reached exit loop
            print("Player limit reached!")
            break

    if terminate():
        print("\nAll profiles created successfully, Enter 4 to commence! ")


def editProfile():
    valid_ID = 0
    repeat = "Y"
    while repeat == "Y":
        item = 0
        grpInp()

        fo = open(f"Storage/Group{group}_profile/team_{team}.txt", "r")
        totalLines = fo.readlines()

        if len(totalLines) > 0:
            displayProfile(totalLines)
            ID = input("Enter team ID to edit: ").upper()
            checkEmpty(ID, "player ID")

            for line in totalLines:  # Search file for the player with the above ID
                item = line.split(",")
                if item[0] == ID:
                    valid_ID = True
                    break

            if valid_ID:
                subOption = int(input("1. Edit name \n2. Edit uniform number \n3. Edit age\n""4. Delete profile \n"
                                      "-->"))

                if subOption == 1:  # Edit name
                    old = item[1]
                    new = input("Enter new name: ")
                    toFind = f"{item[0]},{old},{item[2]},{item[3]}"
                    toReplace = f"{item[0]},{new},{item[2]},{item[3]}"
                    editPlayer(toFind, toReplace)

                elif subOption == 2:  # Edit uniform number
                    old = item[2]
                    new = input("Enter new uniform number: ")
                    toFind = f"{item[0]},{item[1]},{old},{item[3]}"
                    toReplace = f"{item[0]},{item[1]},{new},{item[3]}"
                    editPlayer(toFind, toReplace)

                elif subOption == 3:  # Edit age
                    old = item[3]
                    new = input("Enter new age: ")
                    toFind = f"{item[0]},{item[1]},{item[2]},{old}"
                    toReplace = f"{item[0]},{item[1]},{item[2]},{new}\n"
                    editPlayer(toFind, toReplace)

                elif subOption == 4:  # Delete profile
                    editPlayer(f"{str(item[0])},{str(item[1])},{str(item[2])},{str(item[3])}", "")

                else:
                    print("Invalid option!")
                repeat = input("Enter y to edit another profile: ").upper()
            else:
                print("Invalid ID!")
        else:
            print("No profiles added yet!")


def viewProfile():
    repeat = "Y"
    while repeat.upper() == "Y":
        grpInp()
        fo = open(f"Storage/Group{group}_profile/team_{team}.txt", "r")
        data1 = fo.readlines()
        if len(data1) == 0:
            print("\nNo profiles created yet!")
        else:
            displayProfile(data1)
        repeat = input("Enter y to view another team: ")
