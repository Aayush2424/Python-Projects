print("Welcome to the Calculator")
print("1.Addition\n", "2.Subtraction\n", "3.Multiplication\n", "4.Division\n")
a = int(input("Choose the operation: "))

if a == 1:
    n1 = int(input("Enter the first no.: "))
    n2 = int(input("Enter the second no.: "))
    sum = n1 + n2
    print("Result: ", sum)

elif a == 2:
    n1 = int(input("Enter the first no.: "))
    n2 = int(input("Enter the second no.: "))
    sum = n1 - n2
    print("Result: ", sum)

elif a == 3:
    n1 = int(input("Enter the first no.: "))
    n2 = int(input("Enter the second no.: "))
    sum = n1 * n2
    print("Result: ", sum)

elif a == 4:
    n1 = int(input("Enter the first no.: "))
    n2 = int(input("Enter the second no.: "))
    sum = n1 // n2
    print("Result: ", sum)
