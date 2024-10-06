import time
import threading


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power

            if self.enemies < 0:
                self.enemies = 0

            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


if __name__ == "__main__":
    knights = [
        Knight("Рыцарь Артур", 30),
        Knight("Рыцарь Ланселот", 25),
        Knight("Рыцарь Галахад", 20)
    ]

    for knight in knights:
        knight.start()

    for knight in knights:
        knight.join()
