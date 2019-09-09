# Calculator file

def interface():
    print("Caluculator Program:")
    print("Options Menu:")
    print("Quit = 9")
    menuFlag = True
    
    while menuFlag:
        menuChoice = input("Enter menu option: ")
        if menuChoice == '9':
            menuFlag = False
            return
        else:
            print("Input is not an option. Try again.")
        
if __name__ == "__main__":
    interface()
    