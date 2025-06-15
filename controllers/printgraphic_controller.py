from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

class PrintGraphicController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_printgraphiccontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("Button 1 clicked")
        nama = self.view.entry_1.get()
        usia = self.view.entry_2.get()
        self.view_manager.model.temporary_name = nama
        self.view_manager.model.temporary_age = usia
        print(f"Nama: {nama}")
        print(f"Usia: {usia}")

        self.create_graphic()
        self.view_manager.show_downloadgraphic_view()
        

    def create_graphic(self):
        file_path = self.view_manager.model.temporary_file_path
        if file_path:
            data = pd.read_csv(file_path)
            jam = data['CLOCK']
            detak_jantung = data['HEART']

            fig = plt.Figure(figsize=(6, 4), facecolor=("#EABE7C"))
            ax = fig.add_subplot(111)
            ax.set_facecolor("#EABE7C")
            ax.plot(jam, detak_jantung, linestyle='-')
            ax.tick_params(labelsize=7, colors = "white")
            fig.autofmt_xdate()
            ax.plot(jam, detak_jantung, color = "maroon")
            ax.grid(visible=True)
            ax.set_xlabel('Jam')
            ax.set_ylabel('Detak Jantung')
            ax.set_title('Detak Jantung Terhadap Waktu')

            # Save the figure
            fig_path = "current_graphic.png"
            fig.savefig(fig_path)
            self.view_manager.model.current_graphic_path = fig_path


    def on_button_2_click(self):
        print("Button 2 clicked")
        self.clear_temp_data()
        self.view_manager.show_graphic_view()

    def on_button_3_click(self):
        print("Button 3 clicked")
        self.clear_temp_data()
        self.view_manager.show_profile_view()

    def on_button_4_click(self):
        print("Button 4 clicked")
        self.clear_temp_data()
        self.view_manager.show_graphic_view()

    def on_button_5_click(self):
        print("Button 5 clicked")
        self.clear_temp_data()
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("Button 6 clicked")
        self.clear_temp_data()
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("Button 7 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.clear_temp_data()
            self.view_manager.show_login_view()

    def clear_temp_data(self):
        self.view_manager.model.temporary_name = ""
        self.view_manager.model.temporary_age = ""
        self.view_manager.model.temporary_file_path = ""
        self.view_manager.model.current_graphic_path = ""

