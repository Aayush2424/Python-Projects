print("Welcome to the Calculator!")
print(" 1.Addition\n", "2.Subtraction\n", "3.Multiplication\n", "4.Division\n", "5.Exponent\n")

try:
    a = int(input("Choose the operation: "))
except ValueError:
    print("Please enter a correct option number")
    
try:
    n1 = int(input("Enter the first no.: "))
    n2 = int(input("Enter the second no.: "))
except ValueError:
    print("Please enter a correct value!")
        
try:
    if a == 1:
        sum = n1 + n2
        print("Result: ", sum)
    elif a == 2:
        difference = n1 - n2
        print("Result: ", difference)
    elif a == 3:
        product = n1 * n2
        print("Result: ", product)
    elif a == 4:
        quotient = n1 / n2
        remainder = n1 % n2
        print("The quotient is: ", quotient, " and the remainder is: ", remainder)
    elif a == 5:
        result = n1 ** n2
        print(n1, " to the power ", n2, " is ", result)
    else:
        print("Please enter a valid option")
except NameError:
    print("Error! Invalid operator")
