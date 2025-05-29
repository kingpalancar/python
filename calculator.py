import tkinter as tk
from tkinter import *
from tkinter import messagebox
import math

calc = Tk()
calc.title("calculator")
calc.geometry("2000x470")
calc.configure(bg="#53be25")

#calculator
    #operations
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
def factorial():
    try:
        num1 = int(entry1.get())
        factorial = math.factorial(num1)
        factorial_label.config(text=f"Fact: {factorial}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg= "#000000")
def sqrt():
    try:
        num1 = int(entry1.get())
        sqrt = math.sqrt(num1)
        sqrt_label.config(text=f"Sqrt: {sqrt}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg= "#000000")
def ceil():
    try:
        num1 = int(entry1.get())
        ceil = math.ceil(num1)
        ceiling_label.config(text=f"Ceil: {ceil}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def floor():
    try:
        num1 = int(entry1.get())
        floor = math.floor(num1)
        floor_label.config(text=f"Floor: {floor}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def fabs():
    try:
        num1 = int(entry1.get())
        fabs = math.fabs(num1)
        absolute_label.config(text=f"Abso: {fabs}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def remainder():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        remainder = math.remainder(num1, num2)
        remainder_label.config(text=f"Rem: {remainder}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def exp2():
    try:
        num1 = int(entry1.get())
        exp2 = math.exp2(num1)
        exp2_label.config(text=f"Exp2: {exp2}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def deg():
    try:
        num1 = int(entry1.get())
        deg = math.degrees(num1)
        deg_label.config(text=f"Degr: {deg}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def rad():
    try:
        num1 = int(entry1.get())
        rad = math.radians(num1)
        rad_label.config(text=f"Rads: {rad}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def cos():
    try:
        num1 = int(entry1.get())
        cos = math.cos(num1)
        cos_label.config(text=f"Cos: {cos}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def sin():
    try:
        num1 = int(entry1.get())
        sin = math.sin(num1)
        sin_label.config(text=f"Sin: {sin}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
def tan():
    try:
        num1 = int(entry1.get())
        tan = math.tan(num1)
        tan_label.config(text=f"Tan: {tan}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")

    #user input
tk.Label(calc, text="First number:", bg="#53be25", font=("Georgia", 12)).pack()
entry1 = tk.Entry(calc)
entry1.pack()
tk.Label(calc, text="Second number:", bg="#53be25", font=("Georgia", 12)).pack()
entry2 = tk.Entry(calc)
entry2.pack()
    #individual buttons for operation definitions
calculate_button = tk.Button(calc, text="Root", font=("Georgia", 12), command=sqrt, bg= "#ffffff", fg= "#53be25")
calculate_button.pack(pady = 10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Add", font=("Georgia", 12), command=addition, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='right')
calculate_button = tk.Button(calc, text="Factorial",font=("Georgia", 12), command=factorial, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='right')
calculate_button = tk.Button(calc, text="Subtract", font=("Georgia", 12), command=subtraction, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='right')
calculate_button = tk.Button(calc, text="Divide", font=("Georgia", 12), command=division, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Multiply", font=("Georgia", 12), command=multiplication, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='left')
calculate_button = tk.Button(calc, text="Ceil", font=("Georgia", 12), command=ceil, bg= "#ffffff", fg= "#53be25")
calculate_button.pack(pady = 10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Floor", font=("Georgia", 12), command=floor, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='right')
calculate_button = tk.Button(calc, text="Absolute",font=("Georgia", 12), command=fabs, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='right')
calculate_button = tk.Button(calc, text="Remainder", font=("Georgia", 12), command=remainder, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='right')
calculate_button = tk.Button(calc, text="Exp2", font=("Georgia", 12), command=exp2, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Degrees", font=("Georgia", 12), command=deg, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=2, side='left')
calculate_button = tk.Button(calc, text="Radians", font=("Georgia", 12), command=rad, bg= "#ffffff", fg= "#53be25")
calculate_button.pack(pady = 10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Cosine", font=("Georgia", 12), command=cos, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='right')
calculate_button = tk.Button(calc, text="Sine", font=("Georgia", 12), command=sin, bg= "#ffffff", fg= "#53be25")
calculate_button.pack(pady = 10, padx=8, side='left')
calculate_button = tk.Button(calc, text="Tangent", font=("Georgia", 12), command=tan, bg="#ffffff", fg="#53be25")
calculate_button.pack(pady=10, padx=8, side='right')
    #show individual outputs for each operation definition
addition_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Sum: ", fg="#000000")
addition_label.pack()
subtraction_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Sub: ", fg="#000000")
subtraction_label.pack()
multiplication_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Prod: ", fg="#000000")
multiplication_label.pack()
division_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Quot: ", fg="#000000")
division_label.pack()
factorial_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Fact: ", fg="#000000")
factorial_label.pack()
sqrt_label = tk.Label(calc, bg="#53be25", font= ("Georgia", 12), text= "Sqrt: ", fg="#000000")
sqrt_label.pack()
ceiling_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Ceil: ", fg="#000000")
ceiling_label.pack()
floor_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Floor: ", fg="#000000")
floor_label.pack()
absolute_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Abso: ", fg="#000000")
absolute_label.pack()
remainder_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Rema: ", fg="#000000")
remainder_label.pack()
exp2_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Exp2: ", fg="#000000")
exp2_label.pack()
deg_label = tk.Label(calc, bg="#53be25", font= ("Georgia", 12), text= "Deg: ", fg="#000000")
deg_label.pack()
rad_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Rads: ", fg="#000000")
rad_label.pack()
cos_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Cos: ", fg="#000000")
cos_label.pack()
sin_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Sin: ", fg="#000000")
sin_label.pack()
tan_label = tk.Label(calc, bg="#53be25", font=("Georgia", 12), text="Tan: ", fg="#000000")
tan_label.pack()






calc.mainloop()
