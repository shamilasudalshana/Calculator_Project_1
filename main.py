
##All the calculation operations were defined here
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

##exception is used to stop to code error when zero division is performed
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("float division by zero")


def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b


# -------------------------------------

## defined the select option and check with almost all the possiblities
def select_op(choice):
    if choice == '#':
        return -1

    if choice == "$":
        return 1

    elif choice in ('+', '-', '*', '/','^','%'):

        # taking the 1st number for the user and making sure it is a number
        while True:
            first_number = input("Enter first number: ")
            print(first_number)

            reset_parameter = str(first_number).find("$")  #to check whether $ symbol there to reset
            exit_parameter  = str(first_number).find("#")  #to check whether # symbol there to exit

            if  reset_parameter != -1:
                break

            if exit_parameter != -1:
                break

            try:
                first_number_F = float(first_number)
                break

            except:
                print("Not a valid number,please enter again")
                continue


        # taking the 2nd number for the user and making sure it is a number
        while (reset_parameter == -1 and exit_parameter == -1):
            second_number = input("Enter second number: ")
            print(second_number)

            reset_parameter = str(second_number).find("$") #to check whether $ symbol there to reset
            exit_parameter = str(second_number).find("#")  # to check whether # symbol there to exit

            if reset_parameter != -1:
                break

            if exit_parameter != -1:
                break

            try:
                second_number_F = float(second_number)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        if reset_parameter != -1:
            return 1 # this is just to exit from the if close because of reset option $

        if exit_parameter != -1:
            return -1 # this is just to exit from the if close because of reset option $

        else:
        #make the operation for the given two numbers
            if choice == "+":
                print(first_number_F, "+", second_number_F, "=", add(first_number_F,second_number_F))

            if choice == "-":
                print(first_number_F, "-", second_number_F, "=", substract(first_number_F,second_number_F))

            if choice == "*":
                print(first_number_F, "*", second_number_F, "=", multiply(first_number_F,second_number_F))

            if choice == "/":
                print(first_number_F, "/", second_number_F, "=", divide(first_number_F,second_number_F))

            if choice == "^":
                print(first_number_F, "*", second_number_F, "=", power(first_number_F,second_number_F))

            if choice == "%":
                print(first_number_F, "*", second_number_F, "=", remainder(first_number_F,second_number_F))

            else:
                print("Something Went Wrong")

    else:
        print("Unrecognized operation")



# End the select_op(choice) function here
# -------------------------------------
# This is the main loop.

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()