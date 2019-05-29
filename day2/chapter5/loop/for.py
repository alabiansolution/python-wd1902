states = ["Imo", "Anambra", "Akwa Ibom", "Lagos", "Edo"]

for key in states:
    print(key)
print(range(6))

for x in range(6):
    print(x)

for y in range(1, 7):
    print(y)
states = {
    "Imo" : "Owerri",
    "Lagos" : "Ikeja",
    "Oyo" : "Ibadan",
    "Rivers" : "Port Harcourt",
    "Taraba" : "Yalingo"
}

for state in states:
    print(state)

for state, capital in states.items():
    print(state + " : "+capital)
