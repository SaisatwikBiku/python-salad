import pyautogui as pg
import time

print("program will run after 10 second")
time.sleep(10)
print("running")

for i in range(100):
    pg.write("Message Here")
    time.sleep(0.5)
    pg.press("Enter")
