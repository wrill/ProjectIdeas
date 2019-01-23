#This program is used to check if Google Chrome is running.
#If it is not running, it will open the Google homepage.
import os as os
import webbrowser as wb
import time as t

while True:
    b = (str(os.system('tasklist | find "chrome.exe"')))
    if b == '1':
        wb.open('www.google.com')
        t.sleep(2)
        break

    
        
