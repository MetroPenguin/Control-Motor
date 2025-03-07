import tkinter as tk
from tkinter import messagebox

def obtener_valores():
    user_velocity = velocidad_entry.get()

    if user_velocity.isnumeric():
        user_velocity = int(user_velocity)
        if user_velocity > 255 or user_velocity < 0:
            messagebox.showerror("Error", "La velocidad no está en el rango permitido")
            return
    else:
        messagebox.showerror("Error", "Velocidad inválida")
        return

    direction = direccion_var.get()
    
    if direction not in ["Horario", "Antihorario"]:
        messagebox.showerror("Error", "Debes seleccionar una dirección de giro")
        return

    messagebox.showinfo("Configuración", f"Velocidad seleccionada: {user_velocity}\nGiro: {direction}")

root = tk.Tk()
root.title("Control de Motor")
root.geometry("400x350")

welcome_message = "BIENVENIDOS AL SISTEMA MOTOR CONTROL\nIntroduce una velocidad deseada:"
tk.Label(root, text=welcome_message, wraplength=280, justify="center").pack(pady=10)

tk.Label(root, text="Introduce una velocidad [0-255]:").pack()
velocidad_entry = tk.Entry(root)
velocidad_entry.pack(pady=5)

direccion_var = tk.StringVar(value="")
tk.Label(root, text="Selecciona dirección de giro:").pack()
tk.Radiobutton(root, text="Horario", variable=direccion_var, value="Horario").pack()
tk.Radiobutton(root, text="Antihorario", variable=direccion_var, value="Antihorario").pack()

tk.Button(root, text="Confirmar", command=obtener_valores).pack(pady=20)

root.mainloop()
