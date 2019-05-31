
def multiplication(multiply_by, start=1, stop=12):
    while start <= stop:
        print(multiply_by, " X ", start, " = ", multiply_by * start)
        start += 1

var1 = int(input("Enter Multiplication number : "))
var2 = int(input("Enter start : "))
var3 = int(input("Enter stop : "))
multiplication(var1, var2, var3)
