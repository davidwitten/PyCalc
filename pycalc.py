print("Welcome to the best calculator. To start, enter any expression")
print("For help, enter \"Help\".")
from math import *
def Commands():
    print("To quit, enter \"Quit\".")
    print("To find the square root of a number, enter \"/sqrt number \"")
    print("To determine whether a number is prime, enter \"/prime number\"")
    print("It will return a value of 1 or 0 (1 if true, 0 if not)")
    print("To find the sin, cos, or tan of a number enter \"sin/cos/tan number\"")
    print("To multiply/divide by the previous answer, just enter * or / number(if you have a previous answer)")
    print("To change settings type /settings, if you need help, type \"Help Settings\"")
def prime(number):
    for i in range(2, int(sqrt(number))+1):
        if number%i == 0:
            return 0
    return 1
def trig(command, yn):
    if "/sin" in command:
        wordl = command.split()
        if yn == 0:
            command = "sin(radians(" + wordl[-1] + "))"
        else:
            command = "sin(" + wordl[-1] + ")"
    elif "/cos" in command:
        wordl = command.split()
        if yn == 0:
            command = "cos(radians(" + wordl[-1] + "))"
        else:
            command = "cos(" + wordl[-1] + ")"
    elif "/tan" in command:
        wordl = command.split()
        if yn == 0:
            command = "tan(radians(" + wordl[-1] + "))"
        else:
            command = "tan(" + wordl[-1] + ")"
    return command
def right(choice):
    wordl = choice.split()
    if "/right" in choice:
        if "/right" == wordl[0]:
            wordl = wordl[1:]
            for i in range(3):
                wordl[i] = int(wordl[i])
            hypo = max(wordl)
            for i in range(3):
                if wordl[i-1] != hypo:
                    if (int(wordl[i]) ** 2) + (int(wordl[i-1]) ** 2) == hypo ** 2:
                        return True
                else:
                    if (wordl[i] ** 2) + (wordl[i - 2] ** 2) == hypo ** 2:
                        return True
    return False
def Settings(command,yn):
    if "/settings" in command:
        wordl = command.split()
        if len(wordl) > 1:
            if wordl[1:] == ["ch","trig"]:
                if yn == 1:
                    yn = 0
                else:
                    yn = 1
                print("Done")
            elif wordl[1:] == ["check","trig"]:
                if yn == 1:
                    print("Radians")
                else:
                    print("Degrees")
            elif wordl[1].lower() == "help":
                print("These are all of the commands for /settings (after the main part)")
                print("\n...ch trig\n\n\tChanges from degrees to radians, or vice versa")
                print("\n..check trig\n\n\tChecks if trigonometry is in radians or degrees.")
    return yn
rad = 1
answer = ""
while 1:
    choice = input()
    if "/sqrt" in choice:
        wordl = choice.split()
        if len(wordl) == 2:
            choice = "sqrt(" + wordl[-1] + ")"
        else:
            choice = "sqrt(" + str(answer) + ")"
    elif "/prime" in choice:
        wordl = choice.split()
        try:
            x = prime(int(wordl[-1]))
        except ValueError:
            if answer == "":
                print("Error")
            else:
                x = prime(int(answer))
        if x == 0:
            print("False")
        else:
            print("True")
        choice = "ERROR"
    rad = Settings(choice,rad)
    choice = trig(choice, rad)
    if right(choice) == True:
        print("Works")
        choice = "ERROR"
    elif right(choice) == False:
        print("Doesn't")
        choice = "ERROR"
    if choice == "":
        choice = "ERROR"
        print(choice)
    try:
        if choice != "ERROR" or "OKAY":
            try:
                print(eval(choice))
                answer = eval(choice)
            except SyntaxError:
                symbolist = ["*","/"]
                for i in range(2):
                    if symbolist[i] in choice:
                        x = choice.split()
                        try:
                            if x.index(symbolist[i]) == 0:
                                if answer == "":
                                    print("Erroneous")
                                else:
                                    answer = eval(str(answer) + str(symbolist[i]) + str(x[-1]))
                                    print(answer)
                        except ValueError:
                            print("\n")
    except NameError or SyntaxError or ValueError:
        if choice == "Help":
            Commands()
        elif choice == "Quit":
            break
        else:
            if choice != "ERROR":
                print("QUE")
            

