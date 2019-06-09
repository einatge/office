class Manager():
    def __init__(self , name):
        self.name = name
        self.employees = []

    def hireEmployee(self , employeeName):
         self.employees.append(employeeName)

    def askEmployeeToWork(self, office):
        for employee in self.employees:
            employee.work(office)
            
