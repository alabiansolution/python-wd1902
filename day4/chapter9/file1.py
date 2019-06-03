firstname = input("Enter firstname: ")
middlename = input("Enter middlename: ")
lastname = input("Enter lastname: ")

fullname = firstname +" "+ middlename +" "+ lastname
f = open("demo.txt", "a")
f.write(fullname + "\n")