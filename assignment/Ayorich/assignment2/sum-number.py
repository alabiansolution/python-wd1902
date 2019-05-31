def add_range( num1, num2):
    total = 0
    for num1 in range(num1, num2+1):
        total += num1
    print("Sum of numbers from", start_range, "to", end_range, "is", total)
start_range = int(input("Enter start of range: "))
end_range = int(input("Enter end of range: "))
add_range(start_range, end_range)