import csv
from tkinter import messagebox
from datetime import datetime
import os

class LoginController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_logincontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("Button 1 clicked")
        username = self.view.entry_1.get()
        password = self.view.entry_2.get()
        print(f"Username: {username}")
        print(f"Password: {password}")

        if self.authenticate_user(username, password):
            # Save login info
            self.save_login_info(username, password)

            # Set current user environment variable
            os.environ['CURRENT_USER'] = username

            self.view_manager.show_profile_view()
        else:
            messagebox.showerror("Error", "Username atau Password salah!")
            print("Login Gagal! Username atau Password Salah")

    def authenticate_user(self, username, password):
        file_path = 'signup_data.csv'
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == username and row['Password'] == password:
                        return True
        except FileNotFoundError:
            return False
        return False
    
    def save_login_info(self, username, password):
        file_path = 'user_login.csv'
        fieldnames = ['Username', 'Password', 'Login Time']

        # Check if the file exists to write headers
        try:
            with open(file_path, mode='r') as file:
                pass
        except FileNotFoundError:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        # Append the login data to the CSV file
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Username': username, 'Password': password, 'Login Time': datetime.now()})

    def on_button_2_click(self):
        print("Button 2 clicked")
        self.view.entry_1.delete(0, 'end')
        self.view.entry_2.delete(0, 'end')

    def on_button_3_click(self):
        print("Button 3 clicked")
        self.view_manager.show_signup_view()

    def on_button_4_click(self):
        print("Button 4 clicked")

