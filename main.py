import pygame
from farm import farm
from field import field
from seed import seed


if __name__ == "__main__":
    # print("coucou")
    # field1 = field("ChampOne",10,5);
    # field1.createField()
    # seed1 = seed()
    # seed1.plantSeed()
    farm1 = farm("MyFarm", 1)
    if farm1.numberField > 0:
        field1 = field(
            input("Nom du champ : "),
            int(input("Hauteur du champ : ")),
            int(input("Largeur du champ : "))
        )
        fieldArea = field1.createField()
        if fieldArea > 0:
            print("Champ pret a etre semé !")
            seed1 = seed()
            newPlant = seed1.plantSeed()