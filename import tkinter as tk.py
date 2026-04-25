import tkinter as tk

ventana = tk.Tk()
ventana.title("Programa para subir a Repositorio")
ventana.geometry("350x320")
ventana.configure(bg="#0f0f1a")

# Lista de colores para simular el desvanecido (de oscuro a brillante)
colores = [
    "#0f0f1a", "#1a1a2e", "#2a2a4a",
    "#3a3a6a", "#5a5a9a", "#7a7acc",
    "#9a9aff", "#c2c2ff", "#ffffff"
]

indice = 0

etiqueta = tk.Label(
    ventana,
    text="Este programa es de Tsui y Bermudez",
    font=("Old English Text MT", 18, "bold"),  # fuente gótica (puede variar según tu sistema)
    fg=colores[0],
    bg="#0f0f1a",
    wraplength=300,
    justify="center"
)

# Centrado real en la ventana
etiqueta.place(relx=0.5, rely=0.5, anchor="center")

def fade_in():
    global indice
    if indice < len(colores):
        etiqueta.config(fg=colores[indice])
        indice += 1
        ventana.after(200, fade_in)  # velocidad del efecto

fade_in()

ventana.mainloop()