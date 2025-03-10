from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

# Класс Fighter, представляющий бойца
class Fighter:
    weapon_names = {
        'Sword': 'меч',
        'Bow': 'лук'
    }

    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        weapon_name = self.weapon_names.get(weapon.__class__.__name__, weapon.__class__.__name__.lower())
        print(f"{self.name} выбирает {weapon_name}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
        else:
            print(f"{self.name} безоружен!")

# Класс Monster, представляющий монстра
class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"{self.name} повержен!")

# Реализация боя
def battle(fighter, monster):
    fighter.attack()
    monster.defeat()

# Пример использования
if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец")
    monster = Monster("Монстр")

    # Выбираем оружие и проводим бой
    sword = Sword()
    fighter.change_weapon(sword)
    battle(fighter, monster)

    # Меняем оружие и проводим еще один бой
    bow = Bow()
    fighter.change_weapon(bow)
    battle(fighter, monster)