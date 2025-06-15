from tkinter import messagebox
from PIL import ImageGrab
import os

class DownloadGraphicController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_downloadgraphiccontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("download button_1 clicked")
        self.save_screenshot()
        self.clear_temp_data()

    def save_screenshot(self):
        # Tentukan nama dan path file untuk menyimpan gambar
        filename = f"screenshot_{self.view_manager.model.temporary_name}_{self.view_manager.model.temporary_age}.png"
        save_path = os.path.join(os.getcwd(), filename)

        # Ambil screenshot dari area Tkinter dan simpan sebagai file PNG
        x = self.master.winfo_rootx()
        y = self.master.winfo_rooty()
        width = x + self.master.winfo_width()
        height = y + self.master.winfo_height()
        # Ambil screenshot
        ImageGrab.grab(bbox=(x, y, width, height)).save(save_path)

        messagebox.showinfo("Screenshot Tersimpan", f"Gambar berhasil disimpan di {save_path}")

    def on_button_2_click(self):
        print("download button_2 clicked")
        self.clear_temp_data()
        self.view_manager.show_printgraphic_view()

    def on_button_3_click(self):
        print("download button_3 clicked")
        self.clear_temp_data()
        self.view_manager.show_profile_view()

    def on_button_4_click(self):
        print("download button_4 clicked")
        self.clear_temp_data()
        self.view_manager.show_graphic_view()

    def on_button_5_click(self):
        print("download button_5 clicked")
        self.clear_temp_data()
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("download button_6 clicked")
        self.clear_temp_data()
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("download button_7 clicked")
        self.clear_temp_data()
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()

    def clear_temp_data(self):
        self.view_manager.model.temporary_name = ""
        self.view_manager.model.temporary_age = ""
        