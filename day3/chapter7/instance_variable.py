class Employee():

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


emp1 = Employee("Benedict", "Uwazie", 32)
print(emp1.firstname)
print(emp1.age)
emp2 = Employee("Alabi", "Adebayo", 43)
print(emp2.firstname)
print(emp2.age)
