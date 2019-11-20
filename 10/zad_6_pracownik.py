class Pracownik:
    company = "Love Python"

    def __init__(self, name, surname, position, salary, seniority, is_student):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.seniority = seniority
        self.is_student = is_student

    def pay_up(self):
        return self.salary + (0.5 * self.salary)

    def tax(self):
        return self.salary * 0.02

    def health_care(self):
        if self.is_student:
            proc = 0
        else:
            proc = 0.1
            return self.salary *proc

    def employee_email(self):
        primary = self.name + "." + self.surname
        secondary = self.company.replace(" ", "").lower() + ".com"
        email = primary + "@" + secondary
        return email


p1 = Pracownik("Jan", "Kow", "programista", 5500, 3, False)
print(p1.name)
print(p1.salary)
print(p1.pay_up())
print(p1.company)
print(p1.employee_email())