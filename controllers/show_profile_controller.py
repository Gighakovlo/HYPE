import csv
from tkinter import messagebox
import os

class ShowProfileController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view_manager = view_manager
        self.view = None

    def set_view_showprofilecontroller(self, view):
        self.view = view
        self.display_user_data()

    def display_user_data(self):
        current_user = os.getenv('CURRENT_USER')
        file_path = 'data_user.csv'

        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['User'] == current_user:
                        self.view.display_data(row['Nama'], row['Usia'], row['Jenis Kelamin'])
                        break
        except FileNotFoundError:
            print("File not found")

    def on_button_1_click(self):
        print("show profile button_1 clicked")
        self.view_manager.show_profile_view()

    def on_button_2_click(self):
        print("show profile button_2 clicked")

    def on_button_3_click(self):
        print("show profile button_3 clicked")
        self.view_manager.show_graphic_view()

    def on_button_4_click(self):
        print("show profile button_4 clicked")
        self.view_manager.show_aboutus_view()

    def on_button_5_click(self):
        print("show profile button_5 clicked")
        self.view_manager.show_history_view()

    def on_button_6_click(self):
        print("show profile button_6 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()