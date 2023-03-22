#Project Name: Water Drink Reminder
#Author Name: Sai Satwik Bikumandla
#Date: 22nd March, 2023

import time

lastTime = time.time()
interval = 10 * 60 #reminder for every 10 minutes

while True:
    
    if time.time() - lastTime > interval:
        print("Drink Water!!!")
        lastTime = time.time()

    time.sleep(1*60)        

