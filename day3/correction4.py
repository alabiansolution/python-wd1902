def any_list(var1, list):
    if var1 in list:
        return True
    else:
        return False

arg = input("Enter item in list: ")
prog_lang = ["PHP", "Python", "JS", "Java", "c#"]
if any_list(arg, prog_lang):
    print(arg + " is in a programing language")
else:
    print(arg + " is not a programing language here are some")
    for arg in prog_lang:
        print(arg)
