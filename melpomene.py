from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
from pydub.playback import play

#window
beepboop = Tk()
beepboop.title("jamz :D")
beepboop.geometry("200x50")
beepboop.configure(bg="#e7a3f7")
#function to play selected song from file prompt
def select():
    Tk().withdraw()
    filename = askopenfilename()
    song = AudioSegment.from_mp3(filename)
    play(song)
    return(filename)
#button to activate file prompt command
sel = tk.Button(beepboop, text="Song Select!", font=("Georgia", 12), command=select, fg= "#ceff94", bg= "#ce94ff")
sel.pack(pady = 10, padx=8)

beepboop.mainloop()
