#imports
import tkinter as tk
from tkinter import *
import time

#notepad window structure
root = Tk()
root.title("Clio")
root.geometry("400x700")
root.configure(bg="#ffb0f3")
entry = tk.Text(bg="white", fg="black", wrap="word") 
entry.place(x=10, y=90, width=380, height=600) 
entry.focus()

#notepad def
def notes():
    x = entry.get("1.0", "end-1c")
    with open("Notes.txt", "a") as file:
        file.write(x + "\n") 
    saved = tk.Label(root, text="Saved!", bg="white")
    saved.config(text="Saved!")
    saved.place(x=200, y=650)
    
#save button
save_button = tk.Button(root, text="Save", font=("Georgia", 12), command=notes, bg="#ffb0f3", fg="#f44848")
save_button.pack(pady=50)
root.mainloop()
