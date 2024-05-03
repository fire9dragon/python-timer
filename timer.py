from time import sleep
import tkinter as tk
from subprocess import call as run

timer_time = int(input("Enter the how long the timer shoud be in Seconds: "))
for i in range(timer_time):
    print(f'{"Seconds passed: "} {i} {"/"} {timer_time}')
    sleep(1)
    run("clear")

labal = tk.Label(None, text="Times up!!",font=('Times', '18'),fg='red')
labal.pack()
labal.mainloop()