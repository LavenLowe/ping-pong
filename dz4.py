
import time
import os
import pynput
from colorama import init
from colorama import Fore, Back, Style
init()
width = 30
height = 10
ballX = 5
ballY = 1
rocket1 = 0
rocket2 = 6
rocketLength = 2
dirX = 1
dirY = 1

def draw():
    y = 0
    while y < height:
        x = 0
        res = ''
        while x < width:
            if x == ballX and y == ballY:
                res += 'o'
            elif x == 0 \
                    and y >= rocket1 \
                    and y < rocket1 + rocketLength:
                res += '|'
            elif x == width - 1 \
                    and y >= rocket2 \
                    and y < rocket2 + rocketLength:
                res += '|'
            else:
                res += ' '
            x += 1
        print(res)
        y += 1
    


while True:
    os.system('cls')
    draw()
    moveBall()
    time.sleep(0.05)
