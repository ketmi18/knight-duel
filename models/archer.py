from models.knight import Knight

class Archer(Knight):
    def __init__(self, name):
        super().__init__(name, health=150, damage=30)

    def attack(self, target):
        print(f"{self.name} атакует с помощью лука!")
        super().attack(target)
