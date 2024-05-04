from time import sleep
import tkinter as tk
import os
os_name = os.name
if os_name == "posix":
    command = "clear"
else:
    command = "cls"

timer_time = int(input("Enter for how long the timer shoud be in Seconds: "))
for i in range(timer_time):
    print(f'{"Seconds passed: "} {i} {"/"} {timer_time}')
    sleep(1)
    os.system(command)

labal = tk.Label(None, text="Times up!!",font=('Times', '18'),fg='red')
labal.pack()
labal.mainloop()
