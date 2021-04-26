# From Ishaan to Mom:
# The Time Magement program:
from tkinter import *
from tkinter.messagebox import showinfo
from datetime import date, timedelta
from functions import *

# The Variables:
tasks = read_from_file()

# Set up the window.
window = Tk()
window.title("Time Mangement")
window.configure(height=1000, width=1000, bg='black')

# Set up all the window contents.
welcome = Label(window, text='Welcome back, Deepti!', fg='orange', height=10, width=40, bg='black')

task_entry = Entry(window, fg='orange', bg='grey')

date_entry = Entry(window, fg='orange', bg='grey')

add_task = Button(window, text='Add Task', command=None)

welcome.pack()
task_entry.pack()
date_entry.pack()
add_task.pack()

# The GUL main event loop:
window.mainloop()