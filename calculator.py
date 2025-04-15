#import tkinter stuff
import tkinter as tk
from tkinter import messagebox

#define four operation definitions (addition, subtraction, multiplication) as labels referencing entryx.get
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

#create window for calculator interface
root = tk.Tk()
root.title("galculator")
root.configure(bg="#bdaae0")
root.minsize(400, 400)
root.maxsize(800, 800)
root.geometry("400x400+100+100")

#user input boxes (entryx.get definitions)
tk.Label(root, text="First number:", bg="#bdaae0", font=("Georgia", 12)).pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Second number:", bg="#bdaae0", font=("Georgia", 12)).pack()
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
addition_label = tk.Label(root, bg="#bdaae0", font=("Georgia", 12), text="Sum: ", fg="#000000")
addition_label.pack()
subtraction_label = tk.Label(root, bg="#bdaae0", font=("Georgia", 12), text="Sub: ", fg="#000000")
subtraction_label.pack()
multiplication_label = tk.Label(root, bg="#bdaae0", font=("Georgia", 12), text="Prod: ", fg="#000000")
multiplication_label.pack()
division_label = tk.Label(root, bg="#bdaae0", font=("Georgia", 12), text="Quot: ", fg="#000000")
division_label.pack()

root.mainloop()
