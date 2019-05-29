def office(name, color="Blue"):
    result = "The name of my office is "+name+" and the color is "+color
    print(result)
office("Alabian")
office("MTN", "Yellow")

def add_range(num2, num1=1):
    total = 0
    for num1 in range(num1, num2+1):
        total += num1
    print(total)

add_range(10)
add_range(10, 5)
