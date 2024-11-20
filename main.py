from models.swordsman import Swordsman
from models.spearman import Spearman
from models.archer import Archer

def main():
    # Создаем объекты для каждого типа рыцаря
    swordsman = Swordsman("Артур")
    spearman = Spearman("Галахад")
    archer = Archer("Ланселот")

    # Бой между рыцарями
    print(f"{swordsman.name} атакует {spearman.name}:")
    swordsman.attack(spearman)

    print(f"{spearman.name} атакует {archer.name}:")
    spearman.attack(archer)

    print(f"{archer.name} атакует {swordsman.name}:")
    archer.attack(swordsman)

if __name__ == "__main__":
    main()
