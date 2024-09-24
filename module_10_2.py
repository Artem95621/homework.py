import time
from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemies = 100
        num_days = 0
        while enemies > 0:
            time.sleep(1)
            num_days += 1
            enemies = enemies - self.power

            if enemies < 0:
                enemies = 0

            print(f"{self.name} сражается {num_days} день(дня)..., осатлось {enemies} воинов.")
        print(f"{self.name} одержал победу спустя {num_days} дней(дня)")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
first_knight.join()

second_knight.start()
second_knight.join()

print("Все битвы закончились")