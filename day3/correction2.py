name = input("Find out who is contesting for President: ").capitalize()

contestant = ["Buhari", "Atiku", "Sowore", "Donald Duke"]

if name in contestant:
    print(name + " is contesting for President")
else:
    print(name + " is not contesting for President here is the list of contestant")
    for name in contestant:
        print(name)
