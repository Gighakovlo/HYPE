from tkinter import messagebox

class ProfileController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view_manager = view_manager
        self.view = None

    def set_view_profilecontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("profile button_1 clicked")
        self.view_manager.show_editprofile_view()

    def on_button_2_click(self):
        print("profile button_2 clicked")
        self.view_manager.show_showprofile_view()

    def on_button_3_click(self):
        print("profile button_3 clicked")

    def on_button_4_click(self):
        print("profile button_4 clicked")
        self.view_manager.show_graphic_view()

    def on_button_5_click(self):
        print("profile button_5 clicked")
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("profile button_6 clicked")
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("profile button_7 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()