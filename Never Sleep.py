import pywinauto as auto
import time
import random

while True:
    i = random.randint(100,900)
    j = random.randint(100,900)
    print(i,j)
    auto.mouse.move(coords=(i,j))
    time.sleep(5)