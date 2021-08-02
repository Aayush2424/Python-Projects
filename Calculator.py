print("Welcome to the Calculator!")
print(" 1.Addition\n", "2.Subtraction\n", "3.Multiplication\n", "4.Division\n", "5.Exponent\n")

a = int(input("Choose the operation: "))

n1 = int(input("Enter the first no.: "))
n2 = int(input("Enter the second no.: "))

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
else:
    print("Please enter a valid option")
