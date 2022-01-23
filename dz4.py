
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


    


while True:
    os.system('cls')
    draw()
    moveBall()
    time.sleep(0.05)
