from tkinter import Label, Tk
from time import strftime
root = Tk()
root.title("clock")
root.geometry("250x100")
root.configure(bg="white")
def update_time():
    current_time = strftime('%H:%M:%S %p')
    current_date = strftime("""%A / %B / %d / %Y""")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)
time_label = Label(root, font=('Garamond', 40, 'bold'), bg="white", fg="red")
time_label.pack(anchor='center')
date_label = Label(root, font=('Garamond', 30, 'bold'), bg='white',fg='red')
date_label.pack(anchor='center')
update_time()
root.mainloop()
