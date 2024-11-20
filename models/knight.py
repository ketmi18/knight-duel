class Knight:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        if self.health > 0:
            print(f"{self.name} наносит удар по {target.name} на {self.damage} урона!")
            target.take_damage(self.damage)
        else:
            print(f"{self.name} не может атаковать, так как он уничтожен!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} уничтожен!")
        else:
            print(f"{self.name} получил урон. Осталось здоровья: {self.health}")

