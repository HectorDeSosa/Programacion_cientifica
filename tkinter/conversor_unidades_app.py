import tkinter as tk

def convertir():
    try:
        metros = float(entrada.get())
        km = metros / 1000
        resultado.config(text=f"{km} km")
    except ValueError:
        resultado.config(text="Entrada no válida")

ventana = tk.Tk()
ventana.title("Conversor m a km")
ventana.geometry('300x200')
tk.Label(ventana, text="Metros:").pack()
entrada = tk.Entry(ventana)
entrada.pack()

tk.Button(ventana, text="Convertir", command=convertir).pack()
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
