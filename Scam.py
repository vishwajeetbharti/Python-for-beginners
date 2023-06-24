import random
import string
import time

import pyautogui

# initializing size of string
N = 25
 
# using random.choices()
# generating random strings
time.sleep(1)
count=0
while count<=50:
    res = ''.join(random.choices(string.ascii_letters, k=N))
    pyautogui.typewrite(str(res))
    res=''
    pyautogui.press("enter")
    count= count+1