# x = 1
# total = 0
# for x in range(31):
#     total += x
# print(total)

def add_range(num1, num2):
    total = 0
    for num1 in range(num1, num2+1):
        total += num1
    print(total)
    
add_range(3, 20)

def even_number(number1, number2):
    if number2 % 2 != 0:
        print("Please supply an even number")
    else:
        while number1 <= number2:
            if number1 % 2 == 0:
                print(number1)
            number1 += 1

var1 = int(input("Enter start number: "))
var2 = int(input("Enter stop number: "))
even_number(var1, var2)
