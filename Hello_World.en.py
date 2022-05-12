class bcolors:
    Green = '\033[92m'  # GREEN
    Yellow = '\033[93m'  # YELLOW
    Red = '\033[91m'  # RED
    LIGHT_BLUE = "\033[1;34m"  # Light Blue
    RESET = '\033[0m'  # RESET COLOR


def main():
    print("\"" + bcolors.Green + "Hello World!" + bcolors.RESET + "\"\n")

    is_exit = input(bcolors.Yellow + "Do you want to continue or end it here?"
                    + bcolors.LIGHT_BLUE + " (True or False): " + bcolors.RESET)
    print("\n")

    if is_exit is False:
        exit(1)

    pass


def checks():
    print(bcolors.Green + "Hello World!" + bcolors.LIGHT_BLUE
          + " (For the second time, you entered a world within a world)\n" + bcolors.RESET)

    name = input(bcolors.Yellow + "Can you type your name for the program?: " + bcolors.RESET)

    if name is None:
        print(bcolors.Yellow
              + "You have to type something! So for your laziness,"
              + " you are gonna have to restart the program to continue!"
              + bcolors.RESET)
        return False

    y_or_n = str(input(bcolors.Yellow + "\nYour name is " + bcolors.Green + name + bcolors.Yellow + ", correct?"
                       + bcolors.LIGHT_BLUE + " (y or n): " + bcolors.RESET))

    if y_or_n.lower() == "y" or y_or_n.lower() == "yes":
        return True

    if y_or_n.lower() == "n" or y_or_n.lower() == "non":
        return False

    print(bcolors.Yellow + "What you typed wasn't 'y' nor 'n', but '" + bcolors.Green + y_or_n
          + bcolors.Yellow + "', this answer isn't supported...\n\n")
    return False

    pass


global menu_choices
# Add the number of options when you add them, here, or it isn't going to work
menu_choices = [1]


def calculator_menu():
    print(bcolors.Yellow
          + "Fell yourself lucky, you can choose between 1 type of calculation with two numbers, make your choice")

    print(bcolors.LIGHT_BLUE + "1." + bcolors.Yellow + " Addition" + bcolors.RESET)

    calculator_choice()
    pass


def calculator_choice():
    choice = input(bcolors.Yellow + "Make your choice (ex: 1 or 2): " + bcolors.RESET)

    print("\n")

    choice_location = int(choice) - 1

    if int(choice) == menu_choices[choice_location]:
        if choice_location == 0:
            calculator_add()
            return True
        if choice_location == 1:
            # Pout être étendue dessus à un autre temps
            return True

    print("What you typed wasn't an option")
    return False
    pass


def calculator_add():
    number1 = input(bcolors.Yellow
                    + "This is a basic calculator test which will ask you for two numbers and add them together \n"
                    + "First number: ")

    number2 = input("Second number: " + bcolors.RESET)

    result = float(number1) + float(number2)

    print(result)
    return result
    pass


main()

if checks() is True:
    print(bcolors.Yellow + "\nEverything worked like I hoped, great\n" + bcolors.RESET)
    pass

elif checks() is False:
    print("\n" + "Something didn't work... Or you just said no" + "\n")
    exit(0)

calculator_menu()

exit(1)
