import pyautogui
import time

# y=500
# x=1000
# pyautogui.click(x,y)

# time.sleep(2)
# y=930
# x=1260
# pyautogui.click(x,y)

help_pos=pyautogui.locateOnScreen('room.png')
while help_pos == None:
    time.sleep(0.5)
    help_pos=pyautogui.locateOnScreen('room.png')
    print('detect')
    
print(help_pos)
