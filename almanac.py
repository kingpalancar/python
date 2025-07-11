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
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
from pydub.playback import play
#main window
root = Tk()
root.title("almanac")
root.geometry("420x200")
root.configure(bg="#250A29")
#url loader definitions
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
def discordloader():
    webbrowser.open('https://www.discord.com/')
def youtubeloader():
    webbrowser.open('https://youtube.com')
def twitchloader():
    webbrowser.open('https://twitch.tv')
#clock
def update_time():
    current_time = strftime('%H:%M %p')
    current_date = strftime("""%A, %B %d""")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)
time_label = Label(root, font=('Lato Hairline', 22, 'bold', 'italic'), bg="#250A29", fg="#9CCC65")
time_label.pack(anchor='nw')
date_label = Label(root, font=('Quicksand Light', 12, 'bold', 'italic'), bg='#250A29',fg='#9CCC65')
date_label.pack(anchor='nw')
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
calendar_field = Text(root, width=18, bg="#250A29", fg='#9CCC65', height=8, font=("Lato Hairline", "12", "bold"), borderwidth=2, relief = "solid", wrap='none')
calendar_field.pack(pady=5, anchor='se')
printCalendar()
#calculator
def calculator():
    calc = Tk()
    calc.title("Calculator")
    calc.geometry("570x470+890+50")
    calc.configure(bg="#250A29")
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
    tk.Label(calc, text="First number:", bg="#250A29", fg="#DDC1E1", font=("Georgia", 12)).pack()
    entry1 = tk.Entry(calc)
    entry1.pack()
    tk.Label(calc, text="Second number:", bg="#250A29", fg="#DDC1E1", font=("Georgia", 12)).pack()
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
    addition_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Sum: ", fg="#DDC1E1")
    addition_label.pack()
    subtraction_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Sub: ", fg="#DDC1E1")
    subtraction_label.pack()
    multiplication_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Prod: ", fg="#DDC1E1")
    multiplication_label.pack()
    division_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Quot: ", fg="#DDC1E1")
    division_label.pack()
    factorial_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Fact: ", fg="#DDC1E1")
    factorial_label.pack()
    sqrt_label = tk.Label(calc, bg="#250A29", font= ("Georgia", 12), text= "Sqrt: ", fg="#DDC1E1")
    sqrt_label.pack()
    ceiling_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Ceil: ", fg="#DDC1E1")
    ceiling_label.pack()
    floor_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Floor: ", fg="#DDC1E1")
    floor_label.pack()
    absolute_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Abso: ", fg="#DDC1E1")
    absolute_label.pack()
    remainder_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Rema: ", fg="#DDC1E1")
    remainder_label.pack()
    exp2_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Exp2: ", fg="#DDC1E1")
    exp2_label.pack()
    deg_label = tk.Label(calc, bg="#250A29", font= ("Georgia", 12), text= "Deg: ", fg="#DDC1E1")
    deg_label.pack()
    rad_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Rads: ", fg="#DDC1E1")
    rad_label.pack()
    cos_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Cos: ", fg="#DDC1E1")
    cos_label.pack()
    sin_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Sin: ", fg="#DDC1E1")
    sin_label.pack()
    tan_label = tk.Label(calc, bg="#250A29", font=("Georgia", 12), text="Tan: ", fg="#DDC1E1")
    tan_label.pack()
    calc.mainloop()
calculator_button = tk.Button(root, text="Calculator", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=calculator)
calculator_button.pack(pady=10)
calculator_button.place(x=5, y=100)
#notepad window
def clio():
    win = Tk()
    win.title("Notepad")
    win.geometry("400x700+480+50")
    win.configure(bg="#250A29")
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
    save_button = tk.Button(win, text="Save", font=("Lato Hairline", 12, "bold"), command=test, bg="#DDC1E1")
    save_button.pack(pady=20)
    win.mainloop()
clio = tk.Button(root, text="Notepad", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=clio)
clio.pack(pady= 7)
clio.place(x=130, y=100)
#musicbox window
def melpomene():
    beepboop = Tk()
    beepboop.title("Musicbox")
    beepboop.geometry("200x50+100+300")
    beepboop.configure(bg="#250A29")
    #file selection
    def select():
        Tk().withdraw()
        filename = askopenfilename()
        song = AudioSegment.from_mp3(filename)
        play(song)
        return(filename)
    sel = tk.Button(beepboop, text="Select File", font=("Lato Hairline", 12, "bold"), command=select, bg= "#DDC1E1")
    sel.pack(pady = 10, padx=8)
    beepboop.mainloop()
music_button = tk.Button(root, text =" Musicbox", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=melpomene)
music_button.pack()
music_button.place(x=5, y=140)
#links window
def address():
    adwin = Tk()
    adwin.title("Links")
    adwin.geometry("140x350+330+300")
    adwin.configure(bg="#250A29")
#url button
    cisa_button = tk.Button(adwin, text="CISA", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=cisaloader)
    cisa_button.pack(pady= 8, anchor='center')
    msnbc_button = tk.Button(adwin, text="MSNBC", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=msnbcloader)
    msnbc_button.pack(pady= 5, anchor='center')
    cnn_button = tk.Button(adwin, text="CNN", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=cnnloader)
    cnn_button.pack(pady= 5, anchor='center')
    weather_button = tk.Button(adwin, text="Weather", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=weatherloader)
    weather_button.pack(pady= 5, anchor='center')
    youtube_button = tk.Button(adwin, text="Youtube", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=youtubeloader)
    youtube_button.pack(pady= 5, anchor='center')
    twitch_button = tk.Button(adwin, text="Twitch", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=twitchloader)
    twitch_button.pack(pady= 5, anchor='center')
    discord_button = tk.Button(adwin, text="Discord", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=discordloader)
    discord_button.pack(pady= 5, anchor='center')
    sp500_button = tk.Button(adwin, text="S&P 500", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=sp500loader)
    sp500_button.pack(pady= 5, anchor='center')
addressbut = tk.Button(root, text ="  Links   ", font=("Lato Hairline", 12, "bold"), bg= "#DDC1E1", command=address)
addressbut.pack()
addressbut.place(x=130, y=140)
root.mainloop()
