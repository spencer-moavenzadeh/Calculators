# Calculator file

def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline Low"
    else: 
        return "Low"
        
def cholesterol_interface():
    print("Checking Cholesterol Results:")
    cholInput = input("Enter your cholesterol test results (in format 'test=result' with test options HDL or LDL): ")
    cholData = cholInput.split("=")
    if cholData[0] == "HDL":
        print("Your HDL result is {}".format(cholData[1]))
        print(check_HDL(int(cholData[1])))

def interface():
    print("Caluculator Program:")
    print("Options Menu:")
    print("Cholesterol Check = 1")
    print("Quit = 9")
    menuFlag = True
    
    while menuFlag:
        menuChoice = input("Enter menu option: ")
        if menuChoice == '9':
            menuFlag = False
            return
        elif menuChoice == '1':
            menuFlag = False
            cholesterol_interface()
        else:
            print("Input is not an option. Try again.")
        
if __name__ == "__main__":
    interface()
    