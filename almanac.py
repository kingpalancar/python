#for the urlloader, just replace example sites with whatever sites you'd rather have as buttons
#imports
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from time import strftime
import calendar
import random
import webbrowser
#main window
root = Tk()
root.title("almanac")
root.geometry("500x700")
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
    #addition operation
def addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        addition = num1 + num2
        addition_label.config(text=f"Sum: {addition}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
    #subtraction operation
def subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        subtraction = num1 - num2
        subtraction_label.config(text=f"Sub: {subtraction}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
    #multiplication operation        
def multiplication():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        multiplication = num1 * num2
        multiplication_label.config(text=f"Prod: {multiplication}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000") 
    #division operation
def division():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        division = num1 / num2
        division_label.config(text=f"Quot: {division}", font=("Georgia", 12), fg="#000000")
    except ValueError:
        messagebox.showerror("Error", "need normal numbers", font=("Georgia", 12), fg="#000000")
    #user input boxes (entryx.get definitions)
tk.Label(root, text="First number:", bg="#eef79b", font=("Georgia", 12)).pack()
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="Second number:", bg="#eef79b", font=("Georgia", 12)).pack()
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
addition_label = tk.Label(root, bg="#eef79b", font=("Georgia", 12), text="Sum: ", fg="#000000")
addition_label.pack()
subtraction_label = tk.Label(root, bg="#eef79b", font=("Georgia", 12), text="Sub: ", fg="#000000")
subtraction_label.pack()
multiplication_label = tk.Label(root, bg="#eef79b", font=("Georgia", 12), text="Prod: ", fg="#000000")
multiplication_label.pack()
division_label = tk.Label(root, bg="#eef79b", font=("Georgia", 12), text="Quot: ", fg="#000000")
division_label.pack()
#urlloader buttons
cisa_button = tk.Button(root, text="CISA", font=("Garamond", 12), command=cisaloader)
cisa_button.pack(padx=8, side='right')
msnbc_button = tk.Button(root, text="MSNBC", font=("Garamond", 12), command=msnbcloader)
msnbc_button.pack(padx=2, side='right')
cnn_button = tk.Button(root, text="CNN", font=("Garamond", 12), command=cnnloader)
cnn_button.pack(padx=8, side='left')
weather_button = tk.Button(root, text="Weather", font=("Garamond", 12), command=weatherloader)
weather_button.pack(padx=2, side='left')
sp500_button = tk.Button(root, text="S&P 500", font=("Garamond", 12), command=sp500loader)
sp500_button.pack(pady= 7, anchor='center')

root.mainloop()
