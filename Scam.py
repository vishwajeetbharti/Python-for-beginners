import random
import string
import time
import pyautogui

# initializing size of string
N = 100
 
# using random.choices()
# generating random strings
time.sleep(1)
count=0
while count<=399:   
    #res = ''.join(random.choices(string.ascii_letters, k=N))
    res='HAPPYBIRTHDAYRAJNIKANT'
    pyautogui.typewrite(str(res))
    #res=''
    pyautogui.press("enter")
    count= count+1