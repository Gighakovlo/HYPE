from tkinter import messagebox

class AboutusController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view_manager = view_manager
        self.view = None

    def set_view_aboutuscontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("Button 1 clicked")
        self.view_manager.show_profile_view()

    def on_button_2_click(self):
        print("Button 2 clicked")
        self.view_manager.show_graphic_view()

    def on_button_3_click(self):
        print("Button 3 clicked")

    def on_button_4_click(self):
        print("Button 4 clicked")
        self.view_manager.show_history_view()

    def on_button_5_click(self):
        print("Button 5 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()
