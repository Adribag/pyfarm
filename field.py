from farm import farm

class field(farm):
    def __init__(self, fieldName = "", height = 0, width = 0):
        self.fieldName = fieldName
        self.height = height
        self.width = width


    def createField(self):
        newField = self.height * self.width
        print(f"Champs créé d'une surface de {newField} cases")
        return newField

    

