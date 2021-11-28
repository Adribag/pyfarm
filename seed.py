from field import field

class seed(field):
    def __init__(self, seedName = "blé", age = 10):
        self.seedName = seedName
        self.age = age

    def plantSeed(self):
        newSeed = input("Quelle graine planter ? : ")
        
        if newSeed == "blé":
            print(f"Tu as planté {self.seedName} dans le champs -> ")

    def growSeed(self):
        pass