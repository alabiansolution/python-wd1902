class Employee():

    company_name = "Alabian Solution"
    salary_increement = 0.10
    location = "Lagos"

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def employee_detail(self):
        detail = "{} {} age is {}".format(self.firstname, self.lastname, self.age)
        return detail

    def complete_detail(self):
        return "{} {} is {} years old and works at {} which is located in {}".format(self.firstname, self.lastname, self.age, self.company_name, self.location)



emp1 = Employee("Benedict", "Uwazie", 32)
print(emp1.employee_detail())
emp2 = Employee("Alabi", "Adebayo", 43)
print(emp2.employee_detail())
emp3 = Employee("Opeyemi", "Oyekunle", 28)
print(emp3.employee_detail())
emp4 = Employee("Agbolade", "Dayo", 22)
emp4.company_name = "MTN"
emp4.location = "Abuja"
print(emp4.complete_detail())
