import pyautogui as pg
import datetime as dt
import webbrowser as wb
import time as t
date = dt.datetime.now()
name = pg.prompt('What is your name?', 'Name Entry')
usern = pg.prompt('What is your email?', 'Username Entry')
passw = pg.password('Please enter your email password.', 'Password Entry', 'Password','*')
task = pg.confirm('What class would you like to work on?', 'Task Manager', ['English','Math','History'])
if task == 'English':
    task2 = pg.confirm('What will you be working on?', 'English Manager', ['Write an essay', 'Look up a Book', 'Check my Google Classroom'])
    if task2 == 'Write an essay':
        pg.press('winleft')
        pg.typewrite('Word\n',.25)
        t.sleep(3)
        pg.press('enter')
        t.sleep(2)
        pg.typewrite(name +'\n' + date.strftime('%x\n') + task)
    elif task2 == 'Look up a Book':
        wb.open('https://books.google.com')
    elif task2 == 'Check my Google Classroom':
        wb.open('https://classroom.google.com')
        
elif task == 'Math':
    task2 = pg.confirm('What will you be working on?', 'Math Manager', ['Solve a Problem', 'Research Math Topics', 'Check my Google Classroom'])
    if task2 == 'Solve a Problem':
        pg.press('winleft')
        pg.typewrite('calculator\n',.25)
    elif task2 == 'Research Math Topics':
        wb.open('https://www.wolframalpha.com/')
    elif task2 == 'Check my Google Classroom':
        wb.open('https://classroom.google.com')
elif task == 'History':
    task2 = pg.confirm('What will you be working on?', 'History Manager', ['Write an essay', 'Research Historical Event', 'Check my Google Classroom'])
    if task2 == 'Write an essay':
        pg.press('winleft')
        pg.typewrite('Word\n',.25)
        t.sleep(3)
        pg.press('enter')
        t.sleep(2)
        pg.typewrite(name +'\n' + date.strftime('%x\n') + task)
    elif task2 == 'Research Historical Event':
        wb.open('http://www.sciencepublishinggroup.com/journal/index?journalid=205')
    elif task2 == 'Check my Google Classroom':
        wb.open('https://classroom.google.com')
else:
    print('ok')
