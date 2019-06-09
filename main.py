from Document import Document
from Employee import Employee
from Office import Office
from Manager import Manager
from Cleaner import Cleaner

einat = Employee("Einat")
toysrus = Office("ToysRUs")
tomer = Manager("Tomer")
tomer.hireEmployee(einat)
maya = Employee("Maya")
lili = Employee("Lili")
tomer.hireEmployee(maya)
guy = Manager("Guy")
guy.hireEmployee(einat)
guy.hireEmployee(lili)
nino = Cleaner("Nino")
toysrus.hireCleaner(nino)
toysrus.hireManager(tomer)
toysrus.start_work_day()
