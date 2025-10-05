# Employee Payroll System

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def compute_salary(self):
        return self.base_salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def compute_salary(self):
        return self.base_salary + self.bonus

class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, rate_per_hour):
        super().__init__(name, base_salary)
        self.overtime_hours = overtime_hours
        self.rate_per_hour = rate_per_hour

    def compute_salary(self):
        return self.base_salary + (self.overtime_hours * self.rate_per_hour)


class Intern(Employee):
    def __init__(self, name, stipend, deduction):
        super().__init__(name, stipend)
        self.deduction = deduction

    def compute_salary(self):
        return self.base_salary - self.deduction

employees = [
    Manager("George", 80000, 10000),
    Developer("Vishal", 60000, 10, 500),
    Intern("Yaami", 20000, 2000)
]

for emp in employees:
    print(f"{emp.name}'s Monthly Salary: ₹{emp.compute_salary()}")
