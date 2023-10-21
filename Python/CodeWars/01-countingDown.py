import os
import time
seconds = int(input())
i=seconds

while i>0:
    print(f'Counting down {i} seconds to start HP CodeWars 2023')
    i-=1
    time.sleep(1)
    os.system('cls')