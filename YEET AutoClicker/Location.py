import keyboard
import pyautogui

im1 = pyautogui.screenshot(region=(170,370,620,440))
im1.save(r"F:\Apps\YEET AutoClicker\savedImage.png")

while keyboard.is_pressed('q') == False:
    print("pressed")