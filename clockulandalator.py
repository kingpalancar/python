#imports
import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Tk, Text
from time import strftime
import calendar

#defs for clock, cal, and calc within doubleshell
    #clock
root = Tk()
root.title("clockulandalator")
root.geometry("300x650")
root.configure(bg="white")

def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime("""%A / %B / %d / %Y""")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)
time_label = Label(root, font=('Garamond', 20, 'bold'), bg="white", fg="red")
time_label.pack(anchor='center')
date_label = Label(root, font=('Garamond', 10, 'bold'), bg='white',fg='red')
date_label.pack(anchor='center')
update_time()

    #calendar

def printCalendar():
    month = int(strftime("%m"))
    year = int(strftime("%Y"))
    output_calendar = calendar.month(year, month)
    calendar_field.delete(1.0, 'end')
    calendar_field.insert('end', output_calendar)
    lines = output_calendar.split('\n')
    max_length = max(len(line) for line in lines)
    centered_calendar = '\n'.join(line.center(max_length)for line in lines)
    calendar_field.delete(1.0, 'end')
    calendar_field.insert('end', centered_calendar)
calendar_field = Text(root, width=22, height=8, font=("courier new", "12"), borderwidth=2, relief = "solid", wrap='none')
calendar_field.pack(pady=10, anchor='center')
printCalendar()


    #calc
def addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        addition = num1 + num2
        addition_label.config(text=f"Sum: {addition}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        subtraction = num1 - num2
        subtraction_label.config(text=f"Sub: {subtraction}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def multiplication():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        multiplication = num1 * num2
        multiplication_label.config(text=f"Prod: {multiplication}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def division():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        division = num1 / num2
        division_label.config(text=f"Quot: {division}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")


    #user input boxes (entryx.get definitions)
tk.Label(root, text="First number:", bg="#ffffff", font=("Georgia", 12)).pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Second number:", bg="#ffffff", font=("Georgia", 12)).pack()
entry2 = tk.Entry(root)
entry2.pack()

    #individual buttons for four operation definitions
calculate_button = tk.Button(root, text="Add", font=("Georgia", 12), command=addition, bg="#ffffff", fg="#5ae129")
calculate_button.pack(pady=10)
calculate_button = tk.Button(root, text="Subtract", font=("Georgia", 12), command=subtraction, bg="#ffffff", fg="#5ae129")
calculate_button.pack(pady=10)
calculate_button = tk.Button(root, text="Divide", font=("Georgia", 12), command=division, bg="#ffffff", fg="#5ae129")
calculate_button.pack(pady=10)
calculate_button = tk.Button(root, text="Multiply", font=("Georgia", 12), command=multiplication, bg="#ffffff", fg="#5ae129")
calculate_button.pack(pady=10)

    #show individual outputs for each operation definition
addition_label = tk.Label(root, bg="#ffffff", font=("Georgia", 12), text="Sum: ", fg="#000000")
addition_label.pack()
subtraction_label = tk.Label(root, bg="#ffffff", font=("Georgia", 12), text="Sub: ", fg="#000000")
subtraction_label.pack()
multiplication_label = tk.Label(root, bg="#ffffff", font=("Georgia", 12), text="Prod: ", fg="#000000")
multiplication_label.pack()
division_label = tk.Label(root, bg="#ffffff", font=("Georgia", 12), text="Quot: ", fg="#000000")
division_label.pack()


root.mainloop()
