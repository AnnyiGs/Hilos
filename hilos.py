import tkinter as tk
from tkinter import ttk
import threading
import time
import pytz
from datetime import datetime

#actualizacion del reloj en la etiqueta
def mostrar_hora(ciudad, zona_horaria, etiqueta):
    tz = pytz.timezone(zona_horaria)
    while True:
        hora_actual = datetime.now(tz).strftime("%H:%M:%S")
        etiqueta.config(text=f"{ciudad}: {hora_actual}")
        time.sleep(1)

#actializacion de los campos bloqueados
def actualizar_registro():
    tz_mex = pytz.timezone("America/Mexico_City")
    tz_china = pytz.timezone("Asia/Shanghai")
    while True:
        hora_mex = datetime.now(tz_mex).strftime("%H:%M:%S")
        hora_china = datetime.now(tz_china).strftime("%H:%M:%S")

        entrada_hora_mex.config(state="normal")
        entrada_hora_china.config(state="normal")

        entrada_hora_mex.delete(0, tk.END)
        entrada_hora_mex.insert(0, hora_mex)

        entrada_hora_china.delete(0, tk.END)
        entrada_hora_china.insert(0, hora_china)

        entrada_hora_mex.config(state="readonly")
        entrada_hora_china.config(state="readonly")

        time.sleep(1)

                                                    #botón del registro de llegada, para fines practicos solo imprime en consola ya que llamar a la base de datos no es el objetivo
def registrar_llegada():
    id_distribuidor = entrada_id.get()
    fecha = entrada_fecha.get()
    hora_mex = entrada_hora_mex.get()
    hora_china = entrada_hora_china.get()

    print(f"Llegada registrada ✔︎")
    print(f"ID: {id_distribuidor}")
    print(f"Fecha: {fecha}")
    print(f"Hora México: {hora_mex}")
    print(f"Hora China: {hora_china}")

# ------------------ Crear ventana ------------------
ventana = tk.Tk()
ventana.title("Registro de Distribuidores")
ventana.update_idletasks()
ancho = 500
alto = 300
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# ------------------ Relojes arriba a la derecha ------------------
frame_relojes = tk.Frame(ventana)
frame_relojes.pack(anchor="ne", padx=10, pady=5)

etiqueta_mex = tk.Label(frame_relojes, text="México: --:--:--", font=("Arial", 10, "bold"))
etiqueta_mex.pack(anchor="e")

etiqueta_china = tk.Label(frame_relojes, text="China: --:--:--", font=("Arial", 10, "bold"))
etiqueta_china.pack(anchor="e")

# Hilos para relojes
hilo_mex = threading.Thread(target=mostrar_hora, args=("México", "America/Mexico_City", etiqueta_mex), daemon=True)
hilo_mex.start()

hilo_china = threading.Thread(target=mostrar_hora, args=("China", "Asia/Shanghai", etiqueta_china), daemon=True)
hilo_china.start()

# ------------------ Formulario principal ------------------
frame_form = tk.Frame(ventana)
frame_form.pack(pady=20)

# ID
tk.Label(frame_form, text="ID:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada_id = tk.Entry(frame_form)
entrada_id.grid(row=0, column=1, padx=5, pady=5)

# Botón "Registrar llegada"
boton_registrar = tk.Button(frame_form, text="Registrar llegada", command=registrar_llegada)
boton_registrar.grid(row=1, column=0, columnspan=2, pady=10)

# ------------------ Campos bloqueados (solo lectura) ------------------
frame_registro = tk.LabelFrame(ventana, text="Registro de llegada", padx=10, pady=10)
frame_registro.pack(pady=10, fill="x")

# Fecha actual
tk.Label(frame_registro, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
fecha_actual = datetime.now().strftime("%Y-%m-%d")
entrada_fecha = tk.Entry(frame_registro, state="readonly")
entrada_fecha.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entrada_fecha.config(state="normal")
entrada_fecha.insert(0, fecha_actual)
entrada_fecha.config(state="readonly")

# Hora en México
tk.Label(frame_registro, text="Hora México:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entrada_hora_mex = tk.Entry(frame_registro, state="readonly")
entrada_hora_mex.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Hora en China
tk.Label(frame_registro, text="Hora China:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entrada_hora_china = tk.Entry(frame_registro, state="readonly")
entrada_hora_china.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Hilo para actualizar las horas en las casillas bloqueadas
hilo_registro = threading.Thread(target=actualizar_registro, daemon=True)
hilo_registro.start()

ventana.mainloop()