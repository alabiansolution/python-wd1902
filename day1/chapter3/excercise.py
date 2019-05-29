num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

# We are a creating a program that shows greatest number among three numers
if num1 > num2 and num1 > num3:
    print(num1, "is greater than", num2, "and ", num3)
elif num2 > num1 and num2 > num3:
    print(num2, "is greater than ", num1, "and ", num3)
elif num3 > num1 and num3 > num2:
    print(num3, "is greater than ", num1, "and ", num2)
