import random
import string
import tkinter
import pyperclip
from tkinter import *


window = Tk()

window.title("Passwort-Generator by Jon")
window.configure(width=1000, height=300)
window.configure(bg='#f0f0f0')



var1 = IntVar()
Checkbutton(window, text="Nummern", variable=var1).grid(row=2, sticky=W)
var2 = IntVar()
Checkbutton(window, text="Zeichen", variable=var2).grid(row=3, sticky=W)
T = Text(window, height=3, width=50)
T.config(state=DISABLED)
Label(window, text="Passwörtlänge:").grid(row=0, pady=5)
e1 = Entry(window, width=26)
e1.grid(row=0, column=1, pady=5)
Label(window, text="Output:            ").grid(row=1, pady=5)
T.grid(row=1, column=1, pady=5)

winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

def generate_password():
    T.config(state=NORMAL)
    T.delete(1.0, END)
    T.config(state=DISABLED)
    zeichen = e1.get()
    passwort = []

    if zeichen.isdigit():
        if int(zeichen) > 5 or int(zeichen) == 5:
            if int(zeichen) < 1000 or int(zeichen) == 1000:
                for i in range(int(zeichen)):
                    if var1.get() == 1 and var2.get() == 0:
                        passwort.append(random.choice([random.choice(string.ascii_letters), random.choice(string.digits)]))
                    if var2.get() == 1 and var1.get() == 0:
                        passwort.append(random.choice([random.choice(string.ascii_letters), random.choice(string.punctuation)]))
                    if var1.get() == 1 and var2.get() == 1:
                        passwort.append(random.choice([random.choice(string.ascii_letters), random.choice(string.digits), random.choice(string.punctuation)]))
                    if var1.get() == 0 and var2.get() == 0:
                        passwort.append(random.choice(string.ascii_letters))
                pyperclip.copy("".join(passwort))
                T.config(state=NORMAL)
                T.insert(END, "".join(passwort))
                T.config(state=DISABLED)

            else:
                T.config(state=NORMAL)
                T.insert(END, "Diese Zahl ist zu groß, es muss eine Zahl zwischen 5-1000 sein!")
                T.config(state=DISABLED)
        else:
            T.config(state=NORMAL)
            T.insert(END, "Diese Zahl ist zu klein, es muss eine Zahl zwischen 5-1000 sein!")
            T.config(state=DISABLED)
        
    else:
        T.config(state=NORMAL)
        T.insert(END, "Das war keine Zahl!")
        T.config(state=DISABLED)

    e1.delete(0,END)



Button(window, text='Generieren', command=generate_password).grid(row=4, column=1, sticky=W, pady=4)



window.mainloop()

