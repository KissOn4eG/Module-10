import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, we are under attack!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name} is fighting {self.days} day(s)... {self.enemies} enemies left.")
        print(f"{self.name} won after {self.days} day(s)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("The battles are over.")
