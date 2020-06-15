import pyperclip as cb
import time

multi = []
dash = '-'*60

while True:
    time.sleep(1)
    cb.copy(cb.paste())
    
    if cb.paste() not in multi:
        multi.append(cb.paste())
        print(cb.paste(), end = '\n' + dash + '\n')