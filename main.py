import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack_power = random.randint(10, 30)
            self.player.attack(self.computer)
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен. {self.player.name} победил!")
                break

            self.computer.attack_power = random.randint(10, 30)
            self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            if not self.player.is_alive():
                print(f"{self.player.name} повержен. {self.computer.name} победил!")
                break

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player_hero = Hero(name=player_name)

    computer_hero = Hero(name="Компьютерный Герой", health=100, attack_power=20)

    game = Game(player=player_hero, computer=computer_hero)
    game.start()