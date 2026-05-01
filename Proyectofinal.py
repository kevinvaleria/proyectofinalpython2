import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

# -------------------------
# FUNCIONES
# -------------------------
def abrir_registro_productos():
    messagebox.showinfo("Registro de Productos", "Aquí irá el módulo de registro de productos.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)

# -------------------------
# FONDO NEGRO ESTRELLADO
# -------------------------
canvas = tk.Canvas(ventana, width=500, height=600, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Estrellas
for _ in range(120):
    x = random.randint(0, 500)
    y = random.randint(0, 600)
    size = random.randint(1, 2)
    canvas.create_oval(x, y, x+size, y+size, fill="white", outline="white")

# -------------------------
# FRAME SOBRE EL FONDO
# -------------------------
frame = tk.Frame(ventana, bg="black")
canvas.create_window(250, 300, window=frame)

# -------------------------
# LOGO (logo.png)
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_img = Image.open(os.path.join(BASE_DIR, "logo.png"))
logo_img = logo_img.resize((250, 250))
logo = ImageTk.PhotoImage(logo_img)

lbl_logo = tk.Label(frame, image=logo, bg="black", bd=0)
lbl_logo.pack(pady=20)

# -------------------------
# BOTONES
# -------------------------
estilo = ttk.Style()
estilo.configure("TButton", font=("Arial", 12), padding=10)

btn_reg_prod = ttk.Button(frame, text="Registro de Productos", command=abrir_registro_productos)
btn_reg_prod.pack(pady=10)

btn_reg_ventas = ttk.Button(frame, text="Registro de Ventas", command=abrir_registro_ventas)
btn_reg_ventas.pack(pady=10)

btn_reportes = ttk.Button(frame, text="Reportes", command=abrir_reportes)
btn_reportes.pack(pady=10)

btn_acerca = ttk.Button(frame, text="Acerca de", command=abrir_acerca_de)
btn_acerca.pack(pady=10)

# -------------------------
# INICIO
# -------------------------
ventana.mainloop()