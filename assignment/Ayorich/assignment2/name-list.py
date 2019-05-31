x = str(input("Enter programming language:")).lower()
prog_lang = {"java", "python", "c++","c#","c","php","ruby","kotlin"}
# print(x in prog_lang)
status = x in prog_lang
if status == True:
    print(x, "is a programming language")
else:
    print(x, "is not a programming language")
