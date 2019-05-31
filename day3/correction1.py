
numbers = [10, 20, 30, 40, 50, 60]

# total = 0
#
# for x in numbers:
#     total += x
#
# print(total)

def my_avg(total_avg):
    sum = 0
    for x in total_avg:
        sum += x
    return sum

step_five = [5, 10, 15, 20, 25, 30]
result1 = my_avg(step_five)
print("The average of the step_five is " + str(result1))
step_ten = [10, 20, 30, 40, 50, 60]
result2 = my_avg(step_ten)
print("The average of the step_five is " + str(result2))
