x = 1

while x <= 10:
    print(x)
    # x = x + 1
    x += 1
states = ["Imo", "Anambra", "Akwa Ibom", "Lagos", "Edo"]

x = 0

while x < len(states):
    print(states[x])
    x += 1

# THE BREAK STATEMENT
# y = 1
# while y < 6:
#     print(y)
#     if y == 3:
#         break
#     y += 1
# THE CONTINUE STATEMENT
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
