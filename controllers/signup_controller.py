import csv
from tkinter import messagebox

class SignupController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_signupcontroller(self, view):
        self.view = view

    def button_1_clicked(self):
        print("button_1 clicked")
        username = self.view.entry_1.get()
        email = self.view.entry_2.get()
        password = self.view.entry_3.get()
        print(f"Email: {email}")
        print(f"Username: {username}")
        print(f"Password: {password}")

        if self.is_duplicate(email, username):
            messagebox.showerror("Error", "Email atau Username sudah terdaftar!")
            print("sign up gagal, email atau username telah digunakan!")
            return
        else:
            print("Sign Up Berhasil!")

        # Save to CSV
        self.save_to_csv(email, username, password)

        # Show success message
        messagebox.showinfo("Sukses", "Sign Up telah berhasil dilakukan! Silakan kembali ke halaman Login untuk masuk ke dalam HYPE!")

        # Clear entry boxes
        self.clear_entries()

    def save_to_csv(self, email, username, password):
        file_path = 'signup_data.csv'
        fieldnames = ['Email', 'Username', 'Password']

        # Check if the file exists to write headers
        try:
            with open(file_path, mode='r') as file:
                pass
        except FileNotFoundError:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

        # Append the data to the CSV file
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Email': email, 'Username': username, 'Password': password})

    def clear_entries(self):
        self.view.entry_1.delete(0, 'end')
        self.view.entry_2.delete(0, 'end')
        self.view.entry_3.delete(0, 'end')

    def is_duplicate(self, email, username):
        file_path = 'signup_data.csv'
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Email'] == email or row['Username'] == username:
                        return True
        except FileNotFoundError:
            return False
        return False

    def button_2_clicked(self):
        print("button_2 clicked")
        self.clear_entries()

    def button_3_clicked(self):
        print("button_3 clicked")

    def button_4_clicked(self):
        print("button_4 clicked")
        self.view_manager.show_login_view()
