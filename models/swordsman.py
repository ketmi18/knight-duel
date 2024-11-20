from models.knight import Knight

class Swordsman(Knight):
    def __init__(self, name):
        super().__init__(name, health=200, damage=50)

    def attack(self, target):
        print(f"{self.name} наносит мощный удар мечом!")
        super().attack(target)
