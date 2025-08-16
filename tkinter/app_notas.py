import tkinter as tk
from tkinter import messagebox, filedialog

class AppNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloc de Notas - Python")
        self.root.geometry("600x400")

        self.texto = tk.Text(self.root, wrap="word")
        self.texto.pack(fill="both", expand=True)

        self.crear_menu()

    def crear_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)

        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def nuevo_archivo(self):
        self.texto.delete(1.0, tk.END)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "r") as f:
                contenido = f.read()
            self.texto.delete(1.0, tk.END)
            self.texto.insert(tk.END, contenido)

    def guardar_archivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                               filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "w") as f:
                f.write(self.texto.get(1.0, tk.END))
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppNotas(root)
    root.mainloop()