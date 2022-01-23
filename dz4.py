
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
rket1 = 0
rocket2 = 6
rocketLength = 2
dirX = 1
dirY = 1

def moveBall():
    global ballX, ballY, dirX, dirY
    if ballY == height - 1 or ballY == 0:
        dirY *= -1
    if ballX == width - 1 \
            and ballY >= rocket2 \
            and ballY < rocket2 + rocketLength:
        dirX *= -1
    elif ballX == width - 1:
        print(Fore.RED)
        exit("Player 1 win")
    if ballX == 0 \
            and ballY >= rocket1 \
            and ballY < rocket1 + rocketLength:
        dirX *= -1
    elif ballX == 0:
        print(Fore.CYAN)
        exit("Player 2 win")
    
    ballX += dirX
    ballY += dirY
    
def draw():
    y = 0
    while y < height:
        x = 0
        res = ''
        while x < width:
            if x == ballX and y == ballY:
                res += 'o'
            elif x == 0 \
                    and y >= rket1 \
                    and y < rket1 + rocketLength:
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

pynput.keyboard.Listener(
    on_press = on_press,
    on_release = on_release
).start()

def on_press(key):
    global rocket2, rocket1
    if key == pynput.keyboard.Key.up and rocket2 >= 1:
        rocket2 -= 1
    if key == pynput.keyboard.Key.down and rocket2 <= 7:
        rocket2 += 1
    if key == pynput.keyboard.KeyCode.from_char('w') and rket1 >= 1:
        rket1 -= 1
    if key == pynput.keyboard.KeyCode.from_char('s') and rket1 <= 7:
        rket1 += 1
    


while True:
    os.system('cls')
    draw()
    moveBall()
    time.sleep(0.05)
