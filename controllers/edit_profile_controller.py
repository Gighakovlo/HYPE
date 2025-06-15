import csv
from tkinter import messagebox
import os

class EditProfileController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view_manager = view_manager
        self.view = None
        self.current_user = None

    def set_view_editprofilecontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("button_1 clicked")
        nama = self.view.entry_1.get()
        usia = self.view.entry_2.get()
        jenis_kelamin = self.view.entry_3.get()
        print(f"Nama: {nama}")
        print(f"Usia: {usia}")
        print(f"Jenis Kelamin: {jenis_kelamin}")

        # Get the current user from environment variable
        self.current_user = os.getenv('CURRENT_USER')

        # Save to CSV
        self.save_to_csv(self.current_user, nama, usia, jenis_kelamin)

        # Show success message
        messagebox.showinfo("Sukses", "Data berhasil disimpan")

        # Clear entry boxes
        self.clear_entries()

    def save_to_csv(self, user, nama, usia, jenis_kelamin):
        file_path = 'data_user.csv'
        fieldnames = ['User', 'Nama', 'Usia', 'Jenis Kelamin']
        rows = []

        # Read existing data
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                rows = list(reader)
        except FileNotFoundError:
            pass

        # Check if the user already exists
        user_exists = False
        for row in rows:
            if row['User'] == user:
                row['Nama'] = nama
                row['Usia'] = usia
                row['Jenis Kelamin'] = jenis_kelamin
                user_exists = True
                break

        # If user doesn't exist, append a new row
        if not user_exists:
            rows.append({'User': user, 'Nama': nama, 'Usia': usia, 'Jenis Kelamin': jenis_kelamin})

        # Write back to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    def clear_entries(self):
        self.view.entry_1.delete(0, 'end')
        self.view.entry_2.delete(0, 'end')
        self.view.entry_3.delete(0, 'end')

    def on_button_2_click(self):
        print("edit profile button_2 clicked")
        self.view_manager.show_profile_view()

    def on_button_3_click(self):
        print("edit profile button_3 clicked")

    def on_button_4_click(self):
        print("edit profile button_4 clicked")
        self.view_manager.show_graphic_view()

    def on_button_5_click(self):
        print("edit profile button_5 clicked")
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("edit profile button_6 clicked")
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("edit profile button_7 clicked")
        self.confirm_return_to_login()

    def confirm_return_to_login(self):
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()
