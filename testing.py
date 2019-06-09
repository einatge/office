import pytest
from Cleaner import Cleaner
from Office import Office
from Employee import Employee
from Manager import Manager 

def inc(x):
    return x+1

def test():
    assert inc(3) == 4

def testClean():
    cleaner = Cleaner("Eli")
    assert cleaner.clean is "Eli is cleaning"

testClean()

def testOffice():
    abc = Office("abc")
    abc.hireCleaner("cleaner1")
    assert abc.cleaners[0].name == "cleaner1"

testOffice()

def workTest():
    abc = Office("abc")
    employee = Employee("Einat")
    employee.work(abc)
    assert abc.documents[0].name == "Einat"

workTest()

def hireEmployeeTest():
    employee = Employee("Einat")
    abc = Office("abc")
    manager = Manager("Tomer")
    manager.hireEmployee(employee)
    assert manager.employees[0].name == "Rinat"

hireEmployeeTest()