import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk

# Baca data dari file CSV
file_path = r"C:\Users\gigah\Downloads\heart.csv"
data = pd.read_csv(file_path)

# Ambil kolom jam (time) dan detak jantung (heart_rate)
jam = data['CLOCK']
detak_jantung = data['HEART']

# Membuat plot
fig = plt.Figure(figsize=(8, 6), facecolor=("#EABE7C"))
ax = fig.add_subplot()
ax.set_facecolor("#EABE7C")
ax.plot(jam, detak_jantung, linestyle='-')
ax.tick_params(labelsize=7, colors = "white")
fig.autofmt_xdate()
ax.plot(jam, detak_jantung, color = "maroon")
ax.grid(visible=True)

# Menyeting label dan judul
ax.set_xlabel('Jam')
ax.set_ylabel('Detak Jantung')
ax.set_alpha(0.7)
ax.set_title('Detak Jantung Terhadap Waktu')

# Membuat GUI tkinter untuk menampilkan plot
root = tk.Tk()
root.title('Grafik Detak Jantung')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Menjalankan GUI
tk.mainloop()
