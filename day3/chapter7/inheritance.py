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

class Developer(Employee):
    def __init__(self, firstname, lastname, age, pay, prog_lang):
        super().__init__(firstname, lastname, age)
        self.pay = pay
        self.prog_lang = prog_lang

    def calc_salary(self):
        calc = self.pay * self.salary_increement
        return calc




dev1 = Developer("Benedict", "Uwazie", 32, 20000, "Python")
print(dev1.prog_lang)
print(dev1.complete_detail())
print(dev1.calc_salary())
