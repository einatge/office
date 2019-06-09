from Cleaner import Cleaner
from Manager import Manager

class Office():
    def __init__(self , name):
        self.name = name
        self.documents = []
        self.managers = []
        self.cleaners = []

    def hireCleaner(self, name):
        cleaner = Cleaner(name)
        self.cleaners.append(cleaner)

    def hireManager(self, name):
        manager = Manager(name)
        self.managers.append(manager)

    def add_document(self, document):
        self.documents.append(document)

    def start_work_day(self):
        for manager in self.managers:
            manager.askEmployeeToWork(self) 
        for cleaner in self.cleaners:
            cleaner.clean()


