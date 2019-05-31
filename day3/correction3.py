def in_list(var1):
    change_case = var1.capitalize()
    contestant = ["Buhari", "Atiku", "Sowore", "Donald Duke"]

    if change_case in contestant:
        print(change_case + " is contesting for President")
    else:
        print(change_case + " is not contesting for President here is the list of contestant")
        for change_case in contestant:
            print(change_case)

in_list("sowore")
