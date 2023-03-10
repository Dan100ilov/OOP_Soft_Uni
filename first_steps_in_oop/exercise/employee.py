class Employee:
    def __init__(self, id: int, first_name: str, last_name: str, salary: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, increase):
        self.salary += increase
        return self.salary

    def get_annual_salary(self):
        return self.salary * 12



employee2 = Employee(11111, "Kiro", "Smindow", 2000)
print(employee2.get_full_name())
print(employee2.raise_salary(500))
print(employee2.get_annual_salary())

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
