import os

# Functions
# Clear the screen
def clear():
    os.system('cls')
    main()

# Pause the activity
def pause():
    os.system('pause')

# Getting Log In Details as variables
def getUsername():
    with open("store.txt", "r") as data:
        for line in data:
            usrnm, pswrd = line.split(" : ")
    data.close()
    return usrnm

def getPassword():
    with open("store.txt", "r") as data:
        for line in data:
            usrnm, pswrd = line.split(" : ")
    data.close()
    return pswrd

# What happens after you gain access
def StartApp():
    print("You have obtained Access!")
    pause()
    clear()

# What happens if you are wrong
def LoadRetry():
    print("FAILED!!")
    pause()
    clear()

# Login Function
def Login():
    nameGiven = input("Enter Username : ")
    passwordGiven = input("Enter Password : ")

    username = getUsername()
    password = getPassword()

    if (nameGiven == username and passwordGiven == password):
        StartApp()
    else:
        LoadRetry()

# Signup Function
def Signup():
    newUsername = input("Create a Username : ")
    newPassword = input("Create a Password : ")

    # Open File with Log In Details
    file = open("store.txt", "a")

    file.write(newUsername)
    file.write(" : ")
    file.write(newPassword)
    file.close()

    print("Account Created!!!")
    
    pause()
    clear()

# Main Code Loop
# Giant login systems text done with "http://patorjk.com/software/taag/"
def main():
    print("===========================================Welcome to the Test=====================================================")

    print(" /$$                           /$$                  /$$$$$$                        /$$                            ")
    print("| $$                          |__/                 /$$__  $$                      | $$                            ")
    print("| $$        /$$$$$$   /$$$$$$  /$$ /$$$$$$$       | $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$ ")
    print("| $$       /$$__  $$ /$$__  $$| $$| $$__  $$      |  $$$$$$ | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$")
    print("| $$      | $$  \ $$| $$  \ $$| $$| $$  \ $$       \____  $$| $$  | $$|  $$$$$$   | $$    | $$$$$$$$| $$ \ $$ \ $$")
    print("| $$      | $$  | $$| $$  | $$| $$| $$  | $$       /$$  \ $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$ | $$ | $$")
    print("| $$$$$$$$|  $$$$$$/|  $$$$$$$| $$| $$  | $$      |  $$$$$$/|  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$ | $$ | $$")
    print("|________/ \______/  \____  $$|__/|__/  |__/       \______/  \____  $$|_______/    \___/   \_______/|__/ |__/ |__/")
    print("                     /$$  \ $$                               /$$  | $$                                            ")
    print("                    |  $$$$$$/                              |  $$$$$$/                                            ")
    print("                     \______/                                \______/                                             ")

    print("==================================================================================================================")

    print("                                        1. Login to established Account")
    print("                                            2. Create a New Account")
    choice = input("\n Choose 1 or 2 : ")
    if choice == "1":
        Login()
    elif choice == "2":
        Signup()
    else:
        print("You Down Bad Man!")
    pass

main()
