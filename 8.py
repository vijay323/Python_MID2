"""Q8. Create a base class Employee and a derived class Manager. Override a method to include 
managerial incentives in salary computation.""" 
class Employee: 
    def __init__(self, name, salary): 
        self.name = name 
        self.salary = salary 
 
    def get_salary(self): 
        return self.salary 
 
class Manager(Employee): 
    def __init__(self, name, salary, incentive): 
        super().__init__(name, salary) 
        self.incentive = incentive 
 
    def get_salary(self): 
        return self.salary + self.incentive 
 
e = Employee("Vijay", 30000) 
m = Manager("Ravi", 40000, 8000) 
print("Employee Salary:", e.get_salary()) 
print("Manager Salary:", m.get_salary()) 
