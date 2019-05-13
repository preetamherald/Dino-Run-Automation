from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (340, 390)
    dino = (199, 400)

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace(y):
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("jump")
    time.sleep(y*0.001)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def imageGrab():
    box = (Coordinates.dino[0]+5, Coordinates.dino[1]-1,
           Coordinates.dino[0]+145, Coordinates.dino[1]+3)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    y = 250
    while True:
        if(imageGrab() != 807):
            if(y < 10):
                y = y - 4
            pressSpace(y)
            #time.sleep(0.1)

main()
