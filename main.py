from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:
        valor = float(polegadas.get())
        centimetros.set(valor * 2.54)
    except ValueError:
        pass

root = Tk()
root.title("Converter polegada para centímetro")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

polegadas = StringVar()
polegadas_entry = ttk.Entry(mainframe, width=7, textvariable=polegadas)
polegadas_entry.grid(column=2, row=1, sticky=(W,E))

centimetros = StringVar()
ttk.Label(mainframe, textvariable=centimetros).grid(column=2, row=2, sticky=())

ttk.Button(mainframe, text = "Calcular", command=calcular).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Polegada(s)").grid(column=3, row=1, sticky=(W))
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=(E))
ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=(W))

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

polegadas_entry.focus()
root.bind("<Return>", calcular)

root.mainloop()