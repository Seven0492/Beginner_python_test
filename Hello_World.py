def main():
    print("\"Hello World!\"" + "\n")

    # liist = "[0] second [1] Nothing" liiist = liist.split() print(liiist[0] + liiist[1] + "\n" + liiist[2] + liist[
    # 3] + "\n") function = input("Within these local functions, which do you want to execute? (number or 'the final
    # number' if " "you want to end the main function)): ") print(function + "this is a test for now")

    is_exit = input("Do you want to continue testing or end it here? (True or False): ")
    print("\n")

    if is_exit is False:
        exit(1)

    pass


global y_or_n


def second():
    print("Hello World! (For the second time, you have entered a world within a world)" + "\n")
    name = input("Can you state your name for the program?: ")

    if name is None:
        print("You have to type something! So for your laziness you now have to start the program again if you want "
              "to continue")
        return False

    else:
        y_or_n = str(input("\n" + "Your name is " + name + ", correct? (y or n): "))

    if len(y_or_n) != 1 and len(y_or_n) > 3:
        print("You said it was neither 'y' nor 'n', but '" + y_or_n + "', this answer isn't supported..." + "\n" + "\n")
        return False

    if y_or_n == "y" or y_or_n == "Y" or y_or_n.lower == "yes":
        return True

    elif y_or_n == "n" or y_or_n == "N" or y_or_n.lower == "no":
        return False

    pass


def calculator_add():
    number1 = input("This is a basic calculator test which will ask you for two numbers and add them together \n"
                    "First number: ")
    number2 = input("Second number: ")
    result = float(number1) + float(number2)

    print(result)
    pass


main()

if second() is True:
    print("\n" + "Everything worked as I expected, as I hoped, marvelous" + "\n")
    pass

elif second() is False:
    print("\n" + "Something probably went wrong... Or you just said no" + "\n")
    exit(0)

calculator_add()

exit(1)
