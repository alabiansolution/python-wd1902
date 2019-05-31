nums = ["10", "20", "30", "40", "70", "200", "300"]
total = 0
i = 0
for nums[i] in nums:
    total += int(nums[i])
    i += 1
print("Sum is ", total)
average = total/7
print("Average is ",average)


# sum = {"0"}
# #sum.update(input("numbers of listed items: "))
# sum.update(input("numbers of listed items: "))
# total = 0 
# for x in sum:
#     total += int(x)
# print(total)