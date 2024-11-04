# Домашнее задание
# по теме "Потоки на классах"

# Задача "За честь и отвагу!":

import threading
import time

class  Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # У каждого рыцаря свои 100 врагов
        self.days_passed = 0

    def run(self):
        print(f'{self.name}, на нас напали!"')
        while self.enemies > 0:
        # Сражаемся каждый день
            self.enemies -= self.power
        # Выводим статус каждые сутки
            self.days_passed += 1
            print(f'{self.name}, сражается {self.days_passed} день(дня), осталось {self.enemies} воинов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {self.days_passed} дней(дня)!')

if __name__ == "__main__":

    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()

print('Все битвы закончились!')