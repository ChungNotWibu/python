class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def display_info(self):
        print(f"ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, employee_id, name, salary, department):
        super().__init__(employee_id, name, "Manager", salary)
        self.department = department
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def hire_employee(self, employee):
        self.employees.append(employee)
    def list_employees(self):
        for employee in self.employees:
            employee.display_info()

company = Company("ABC Company")

employee1 = Employee(1, "John Doe", "Developer", 50000)
employee2 = Employee(2, "Jane Smith", "Designer", 45000)
manager1 = Manager(3, "Alice Johnson", 60000, "HR Department")

company.hire_employee(employee1)
company.hire_employee(employee2)
company.hire_employee(manager1)
company.list_employees()