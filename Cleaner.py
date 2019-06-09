class Cleaner():
    def __init__(self , name):
        self.name = name

    def clean(self):
        print("{} is cleaning".format(self.name))
        
    # def testClean():
    #     cleaner = Cleaner("Eli")
    #     assert cleaner.clean == "Eli is cleaning"