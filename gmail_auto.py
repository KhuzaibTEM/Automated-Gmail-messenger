import pyautogui
import time
import keyboard
import csv

num = 0
email = []

with open("students_mail.csv") as f:
    line = csv.reader(f)
    for i in line:
        email.append(i)

time.sleep(3)

#click on compose button (96,274)
pyautogui.click(96,274)
time.sleep(0.1)

#type the email addresses
while num < len(email[0]):
    keyboard.write(email[0][num])
    time.sleep(0.2)
    keyboard.press("enter")
    num += 1

    time.sleep(0.1)

#click on attach file (1395,981)
pyautogui.click(1395,981)
time.sleep(1)

#upload the farewell invite (378,224)
pyautogui.doubleClick(378,224)
time.sleep(0.1)


#type on the subject (1250,517)
pyautogui.click(1250, 517)
keyboard.write("Farewell")
time.sleep(1)

#send the mail (1254,974)
pyautogui.click(1254,974)
