#generates a random country from the main list of 1936 countries in Hearts of Iron 4.
#imports
import random
import tkinter as tk
from tkinter import *
import time

#window
root = Tk()
root.title("HOI4 Country Generator")
root.geometry("300x100")
root.configure(bg="#ffffff")

#country array
countries = ["Afghanistan", "Albania", "Argentina," "Australia", "Austria", 
             "Belgium", "Bhutan", "Bolivia", "Brazil", "British Burma",
             "British Malaya", "British Raj", "Bulgaria", "Chile", "China", 
             "Columbia", "Communist China", "Costa Rica", "Cuba", "Czechoslovakia",
             "Denmark", "Dominican Republic", "Dominion of Canda", "Dutch East Indies",
             "Ecuador", "El Salvador", "Estonia", "Ethiopia", "Finland", "France",
             "Germany", "Greece", "Guangxi Clique", "Guatemala", "Haiti", "Honduras",
             "Iceland", "Iran", "Ireland", "Italy", "Japan", "Hungary", "Kuwait", 
             "Latvia", "Liberia", "Lithuania", "Luxembourg", "Manchukuo", "Mengkukuo",
             "Mexico", "Mongolia", "Nepal", "Netherlands", "New Zealand", "Norway", 
             "Nicaragua", "Norway", "Oman", "Panama", "Paraguay", "Peru", "Phillippines",
             "Poland", "Portugal", "Republican Spain", "Romania", "Saudi Arabia", "Shanxi",
             "Siam", "Sinkiang", "Soviet Union", "Sultanate of Aussa", "Sweden", "Switzerland",
             "Tannu Tuva", "Tibet", "Turkey", "Union of South Africa", "United Kingdom", "USA",
             "Uruguay", "Venezuela", "Xibei San Ma", "Yemen", "Yugoslavia", "Yunnan"]

#picker
def randcount():
    country_label = tk.Label(root,bg="#ffffff", font= ("Georgia", 12), text= "Country: ", fg="#000000")
    country_label.config(text=f"{(countries[random.randint(0,84)])}", font=("Georgia", 12), fg="#000000")
    country_label.pack()

#button
country_button = tk.Button(root, text="Generate", font=("Georgia", 12), command=randcount, bg= "#ffffff", fg= "#53be25")
country_button.pack(pady = 10, padx=8, anchor='center')

root.mainloop()
