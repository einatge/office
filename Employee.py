from Document import Document

class Employee():
    def __init__(self , name):
        self.name = name        
    
    def work(self, office):
        for i in range(1,10):
            office.add_document(Document(self.name))
        