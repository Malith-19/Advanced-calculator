def select_op(choice):
    valid_operators = "+-*/^%#$"

    if choice not in valid_operators:
        return -2  # -2 is for invalid operation
    if choice == "#":
        return -1  # -1 is for terminate the program
    if choice == "$":
        return -3  # -3 is for reset the cal


# this function will return True for input string is a float. If not it will return false.
def isfloat(num):
    try:
        float_num = float(num)
        return True
    except:
        return False


def execute(operation, num1=None, num2=None):
    if not (num1):
        num1 = input("Enter first number: ")
        if "$" in num1:
            print("Resetting numbers. You can enter numbers again!")
            execute(operation)
        elif (isfloat(num1)):
            num1 = float(num1)
        else:
            print("Not a valid number. Please enter again.")
            execute(operation)
    if not (num2):
        num2 = input("Enter second number: ")

        if "$" in num2:
            print("Resetting numbers. You can enter numbers again!")
            execute(operation)
        elif (isfloat(num2)):
            num2 = float(num2)
        else:
            print("Not a valid number. Please enter again.")
            execute(operation, num1)
    
    answer = None #this will collect the answer by doing operation

    if operation == "+":
        answer =num1 + num2

    elif operation == "-":
        answer = num1 - num2

    elif operation == "*":
        answer = num1 * num2

    elif operation == "/":
        try:
            print(num1,operation,num2,"=",num1 / num2)
        except(ZeroDivisionError):
            print("float division by zero") #printing error

    elif operation == "^":
        answer = num1 ** num2

    elif operation == "%":
        answer = num1 % num2

    print(num1,operation,num2,"=",answer) #printing the answer
    return


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
    
    if select_op(choice) == -1:
        # program ends here
        print("Done. Terminating")
        exit()
    elif select_op(choice) == -2:
        print("Unrecognized operation")
    elif select_op(choice) == -3:
        print("resetting the cal")
        continue
    else:
        try:
            execute(choice)
        except:
            print("Something went wrong")
