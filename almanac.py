#for the urlloader, just replace example sites with whatever sites you'd rather have as buttons
#imports
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from time import strftime
import calendar
import random
import webbrowser
import math

#main window
root = Tk()
root.title("almanac")
root.geometry("500x440")
root.configure(bg="#eef79b")

#urlloader definitions
def cisaloader():
    webbrowser.open('https://www.cisa.gov/')
def msnbcloader():
    webbrowser.open('https://www.msnbc.com/')
def cnnloader():
    webbrowser.open('https://www.cnn.com/')
def sp500loader():
    webbrowser.open('https://markets.businessinsider.com/index/s&p_500?op=1')
def weatherloader():
    webbrowser.open('https://weather.com/')

#fortune dict
fortune = {
    "fortune1": "A sudden opportunity will arise—seize it before the moon wanes.",
    "fortune2": "Beware of misplaced trust; not all who smile are friends.",
    "fortune3": "A long journey begins with a single step, but check your boots first.",
    "fortune4": "Luck favors the bold, but recklessness favors misfortune.",
    "fortune5": "A secret admirer will reveal themselves under the next full moon.",
    "fortune6": "Financial gains are on the horizon, but avoid risky ventures.",
    "fortune7": "An old grudge will resurface—forgiveness brings peace.",
    "fortune8": "Your creativity blooms; share your talents with the world.",
    "fortune9": "A misplaced item will return when Mercury goes direct.",
    "fortune10": "Patience is a virtue, but don’t wait too long to act.",
    "fortune11": "A chance encounter will lead to an unexpected friendship.",
    "fortune12": "Beware the ides of the month; double-check your plans.",
    "fortune13": "A change in the wind brings new perspectives—embrace them.",
    "fortune14": "Your hard work will soon be rewarded—keep pushing forward.",
    "fortune15": "A quarrel may arise; choose your words with care.",
    "fortune16": "The stars align in your favor—now is the time to take risks.",
    "fortune17": "A letter from afar will bring surprising news.",
    "fortune18": "Trust your instincts; they are sharper than you think.",
    "fortune19": "A small kindness will return to you tenfold.",
    "fortune20": "Avoid unnecessary conflict; harmony is within reach.",
    "fortune21": "A new skill learned today will prove invaluable tomorrow.",
    "fortune22": "An unexpected windfall is coming—use it wisely.",
    "fortune23": "The past cannot be changed, but the future is yours to shape.",
    "fortune24": "A dream will reveal hidden truths—pay attention.",
    "fortune25": "A rival’s envy may surface; stay humble and focused.",
    "fortune26": "Good health follows those who tend to body and mind.",
    "fortune27": "A delayed answer will arrive when least expected.",
    "fortune28": "Love blossoms where laughter is shared.",
    "fortune29": "A risky gamble may pay off, but know when to walk away.",
    "fortune30": "A change of scenery will bring renewed energy.",
    "fortune31": "Beware false promises; not all that glitters is gold.",
    "fortune32": "A mentor’s advice will guide you through uncertainty.",
    "fortune33": "The early bird gets the worm, but the wise bird avoids the cat.",
    "fortune34": "A long-held wish will soon come to fruition.",
    "fortune35": "A stranger’s kindness will restore your faith in humanity.",
    "fortune36": "A setback is merely a setup for a greater comeback.",
    "fortune37": "Your words carry weight—speak with intention.",
    "fortune38": "A forgotten goal resurfaces—now is the time to pursue it.",
    "fortune39": "A partnership strengthens under shared challenges.",
    "fortune40": "A hidden obstacle may delay progress—stay vigilant.",
    "fortune41": "The answer you seek lies within, not in the stars.",
    "fortune42": "A new chapter begins when the old one is released.",
    "fortune43": "A small sacrifice today leads to greater rewards tomorrow.",
    "fortune44": "A rival becomes an ally—keep an open mind.",
    "fortune45": "A whisper in the dark reveals what daylight hides.",
    "fortune46": "A leap of faith is required—trust in your path.",
    "fortune47": "A lost item is closer than you think—retrace your steps.",
    "fortune48": "A storm passes, leaving clarity in its wake.",
    "fortune49": "A stranger’s words hold the key to a puzzle.",
    "fortune50": "The universe conspires in your favor—act with confidence."
}
#defs for clock, cal, fortune, urls, and calc within almanac
#clock
def update_time():
    current_time = strftime('%H:%M %p')
    current_date = strftime("""%A, %B %d""")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)
time_label = Label(root, font=('Garamond', 20, 'bold'), bg="#eef79b", fg="red")
time_label.pack(anchor='center')
date_label = Label(root, font=('Garamond', 10, 'bold'), bg='#eef79b',fg='red')
date_label.pack(anchor='center')
update_time()

#fortuneteller
def fortuneteller():
    random_fortune = random.choice(list(fortune.values()))
    fortune_label.config(text=random_fortune)
fortune_label = Label(root, font=('Garamond', 10, 'bold'), bg='#eef79b', fg='#7905ff')
fortune_label.pack(anchor='center')
fortuneteller()

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
calendar_field = Text(root, width=22, bg="#eef79b", height=8, font=("courier new", "12"), borderwidth=2, relief = "solid", wrap='none')
calendar_field.pack(pady=10, anchor='center')
printCalendar()

#calculator
def calculator():
    calc = Tk()
    calc.title("Calculator")
    calc.geometry("570x470")
    calc.configure(bg="#d8f965")
    #calculator
    #operations
    def addition():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            addition = num1 + num2
            addition_label.config(text=f"Sum: {addition}", font=("Georgia", 12), fg="#bba10b")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#bba10b")
    def subtraction():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            subtraction = num1 - num2
            subtraction_label.config(text=f"Sub: {subtraction}", font=("Georgia", 12), fg="#5e0bbb")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#5e0bbb")      
    def multiplication():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            multiplication = num1 * num2
            multiplication_label.config(text=f"Prod: {multiplication}", font=("Georgia", 12), fg="#bb2d0b")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#bb2d0b") 
    def division():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            division = num1 / num2
            division_label.config(text=f"Quot: {division}", font=("Georgia", 12), fg="#7b2d90")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#7b2d90")
    def factorial():
        try:
            num1 = int(entry1.get())
            factorial = math.factorial(num1)
            factorial_label.config(text=f"Fact: {factorial}", font=("Georgia", 12), fg="#68a24e")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg= "#68a24e")
    def sqrt():
        try:
            num1 = int(entry1.get())
            sqrt = math.sqrt(num1)
            sqrt_label.config(text=f"Sqrt: {sqrt}", font=("Georgia", 12), fg="#c33f74")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg= "#c33f74")
    def ceil():
        try:
            num1 = int(entry1.get())
            ceil = math.ceil(num1)
            ceiling_label.config(text=f"Ceil: {ceil}", font=("Georgia", 12), fg="#a0e669")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#a0e669")
    def floor():
        try:
            num1 = int(entry1.get())
            floor = math.floor(num1)
            floor_label.config(text=f"Floor: {floor}", font=("Georgia", 12), fg="#785db7")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#785db7")
    def fabs():
        try:
            num1 = int(entry1.get())
            fabs = math.fabs(num1)
            absolute_label.config(text=f"Abso: {fabs}", font=("Georgia", 12), fg="#52daa0")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#52daa0")
    def remainder():
        try:
            num1 = int(entry1.get())
            num2 = int(entry2.get())
            remainder = math.remainder(num1, num2)
            remainder_label.config(text=f"Rem: {remainder}", font=("Georgia", 12), fg="#dee0ab")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#dee0ab")
    def exp2():
        try:
            num1 = int(entry1.get())
            exp2 = math.exp2(num1)
            exp2_label.config(text=f"Exp2: {exp2}", font=("Georgia", 12), fg="#d0179a")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#d0179a")
    def deg():
        try:
            num1 = int(entry1.get())
            deg = math.degrees(num1)
            deg_label.config(text=f"Degr: {deg}", font=("Georgia", 12), fg="#00ffff")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#00ffff")
    def rad():
        try:
            num1 = int(entry1.get())
            rad = math.radians(num1)
            rad_label.config(text=f"Rads: {rad}", font=("Georgia", 12), fg="#7860dc")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#7860dc")
    def cos():
        try:
            num1 = int(entry1.get())
            cos = math.cos(num1)
            cos_label.config(text=f"Cos: {cos}", font=("Georgia", 12), fg="#ceabbd")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#ceabbd")
    def sin():
        try:
            num1 = int(entry1.get())
            sin = math.sin(num1)
            sin_label.config(text=f"Sin: {sin}", font=("Georgia", 12), fg="#3ea21c")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#3ea21c")
    def tan():
        try:
            num1 = int(entry1.get())
            tan = math.tan(num1)
            tan_label.config(text=f"Tan: {tan}", font=("Georgia", 12), fg="#d1ff00")
        except ValueError:
            messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#d1ff00")
    #user input
    tk.Label(calc, text="First number:", bg="#d8f965", font=("Georgia", 12)).pack()
    entry1 = tk.Entry(calc)
    entry1.pack()
    tk.Label(calc, text="Second number:", bg="#d8f965", font=("Georgia", 12)).pack()
    entry2 = tk.Entry(calc)
    entry2.pack()
    #individual buttons for operation definitions
    calculate_button = tk.Button(calc, text="Root", font=("Georgia", 12), command=sqrt, fg= "#ffffff", bg= "#c33f74")
    calculate_button.pack(pady = 10, padx=8)
    calculate_button.place(x=10, y=10)
    calculate_button = tk.Button(calc, text="Add", font=("Georgia", 12), command=addition, fg="#ffffff", bg="#bba10b")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=440, y=210)
    calculate_button = tk.Button(calc, text="Factorial",font=("Georgia", 12), command=factorial, fg="#ffffff", bg="#68a24e")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=440, y=260)
    calculate_button = tk.Button(calc, text="Subtract", font=("Georgia", 12), command=subtraction, fg="#ffffff", bg="#5e0bbb")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=440, y=310)
    calculate_button = tk.Button(calc, text="Divide", font=("Georgia", 12), command=division, fg="#ffffff", bg="#7b2d90")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=10, y=60)
    calculate_button = tk.Button(calc, text="Multiply", font=("Georgia", 12), command=multiplication, fg="#ffffff", bg="#bb2d0b")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=10, y=110)
    calculate_button = tk.Button(calc, text="Ceil", font=("Georgia", 12), command=ceil, fg= "#ffffff", bg= "#28b561")
    calculate_button.pack(pady = 10, padx=8)
    calculate_button.place(x=10, y=160)
    calculate_button = tk.Button(calc, text="Floor", font=("Georgia", 12), command=floor, fg="#ffffff", bg="#785db7")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=440, y=10)
    calculate_button = tk.Button(calc, text="Absolute",font=("Georgia", 12), command=fabs, fg="#ffffff", bg="#52daa0")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=440, y=160)
    calculate_button = tk.Button(calc, text="Remainder", font=("Georgia", 12), command=remainder, fg="#ffffff", bg="#b5a128")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=440, y=110)
    calculate_button = tk.Button(calc, text="Exp2", font=("Georgia", 12), command=exp2, fg="#ffffff", bg="#d0179a")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=10, y=210)
    calculate_button = tk.Button(calc, text="Degrees", font=("Georgia", 12), command=deg, fg="#ffffff", bg="#3fc9c6")
    calculate_button.pack(pady=10, padx=2)
    calculate_button.place(x=10, y=260)
    calculate_button = tk.Button(calc, text="Radians", font=("Georgia", 12), command=rad, fg= "#ffffff", bg= "#7860dc")
    calculate_button.pack(pady = 10, padx=8)
    calculate_button.place(x=10, y=310)
    calculate_button = tk.Button(calc, text="Cosine", font=("Georgia", 12), command=cos, fg="#ffffff", bg="#ceabbd")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=440, y=360)
    calculate_button = tk.Button(calc, text="Sine", font=("Georgia", 12), command=sin, fg= "#ffffff", bg= "#3ea21c")
    calculate_button.pack(pady = 10, padx=8)
    calculate_button.place(x=10, y=360)
    calculate_button = tk.Button(calc, text="Tangent", font=("Georgia", 12), command=tan, fg="#ffffff", bg="#6128b5")
    calculate_button.pack(pady=10, padx=8)
    calculate_button.place(x=440, y=60)
    #show individual outputs for each operation definition
    addition_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Sum: ", fg="#000000")
    addition_label.pack()
    subtraction_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Sub: ", fg="#000000")
    subtraction_label.pack()
    multiplication_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Prod: ", fg="#000000")
    multiplication_label.pack()
    division_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Quot: ", fg="#000000")
    division_label.pack()
    factorial_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Fact: ", fg="#000000")
    factorial_label.pack()
    sqrt_label = tk.Label(calc, bg="#d8f965", font= ("Georgia", 12), text= "Sqrt: ", fg="#000000")
    sqrt_label.pack()
    ceiling_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Ceil: ", fg="#000000")
    ceiling_label.pack()
    floor_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Floor: ", fg="#000000")
    floor_label.pack()
    absolute_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Abso: ", fg="#000000")
    absolute_label.pack()
    remainder_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Rema: ", fg="#000000")
    remainder_label.pack()
    exp2_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Exp2: ", fg="#000000")
    exp2_label.pack()
    deg_label = tk.Label(calc, bg="#d8f965", font= ("Georgia", 12), text= "Deg: ", fg="#000000")
    deg_label.pack()
    rad_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Rads: ", fg="#000000")
    rad_label.pack()
    cos_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Cos: ", fg="#000000")
    cos_label.pack()
    sin_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Sin: ", fg="#000000")
    sin_label.pack()
    tan_label = tk.Label(calc, bg="#d8f965", font=("Georgia", 12), text="Tan: ", fg="#000000")
    tan_label.pack()




    calc.mainloop()
calculator_button = tk.Button(root, text="Calculator", font=("Georgia", 12), command=calculator)
calculator_button.pack(pady=10)

    #clio
def clio():
    win = Tk()
    win.title("Clio")
    win.geometry("400x700")
    win.configure(bg="#ffb0f3")
    entry = tk.Text(win, bg="white", fg="black", wrap="word", font=("Constantia", "12")) 
    entry.place(x=10, y=90, width=380, height=600) 
    entry.focus()
    #notepad def
    def test():
        x = entry.get("1.0", "end-1c")
        with open("Notes.txt", "a") as file:
            file.write(x + "\n") 
        saved = tk.Label(win, text="Saved!", bg="white")
        saved.config(text="Saved!")
        saved.place(x=200, y=650)
        #save button
    save_button = tk.Button(win, text="Save", font=("Georgia", 12), command=test, bg="#ffb0f3", fg="#f44848")
    save_button.pack(pady=50)
    win.mainloop()


    #urlloader buttons
cisa_button = tk.Button(root, text="CISA", font=("Garamond", 12), command=cisaloader)
cisa_button.pack(padx=8, side='right')
msnbc_button = tk.Button(root, text="MSNBC", font=("Garamond", 12), command=msnbcloader)
msnbc_button.pack(padx=2, side='right')
cnn_button = tk.Button(root, text="CNN", font=("Garamond", 12), command=cnnloader)
cnn_button.pack(padx=8, side='left')
weather_button = tk.Button(root, text="Weather", font=("Garamond", 12), command=weatherloader)
weather_button.pack(padx=2, side='left')
clio = tk.Button(root, text="Clio", font=("Garamond", 12), command=clio)
clio.pack(pady= 7, anchor='center')
sp500_button = tk.Button(root, text="S&P 500", font=("Garamond", 12), command=sp500loader)
sp500_button.pack(pady= 0, anchor='center')

root.mainloop()
