from models.knight import Knight

class Spearman(Knight):
    def __init__(self, name):
        super().__init__(name, health=180, damage=40)

    def attack(self, target):
        print(f"{self.name} атакует с помощью копья!")
        super().attack(target)
