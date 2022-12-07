import pyautogui
import time
time.sleep(4)
count=0
while count<=10000:
    pyautogui.typewrite("virus.😁"+str(count))
    pyautogui.press("enter")
    count=count+1  