from pyautogui import *
import pyautogui
import time
import keyword
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('bob5.png', region=(0,0,1920,1080),  confidence = 0.5) is not None:
        print("i can see it")
        time.sleep(0.1)

