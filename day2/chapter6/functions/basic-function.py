def say_hello():
    print("Hello everyone")

say_hello()

def greeting(name):
    print("Hello Mr "+name)
greeting("Alabi")
greeting("Benedict")
greeting("Ope")

def addition(var1, var2):
    sum = var1 + var2
    print(sum)
addition(3, 5)

def person(name, age, occupation):
    result = "My name is "+name+" and my age is "+str(age)+" and a "+occupation
    print(result)
person("Benedict", 32, "Developer")
person("Alabi", 42, "CEO")
person("Ope", 28, "Developer")
