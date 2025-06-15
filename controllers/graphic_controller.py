from tkinter import messagebox

class GraphicController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_graphiccontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("Graphic Button 1 clicked")
        self.view_manager.show_inputgraphic_view()

    def on_button_2_click(self):
        print("Graphic Button 2 clicked")
        # Add logic for button 2 click
        self.view_manager.show_printgraphic_view()
    def on_button_3_click(self):
        print("Graphic Button 3 clicked")
        self.view_manager.show_profile_view()

    def on_button_4_click(self):
        print("Graphic Button 4 clicked")
        # Add logic for button 4 click

    def on_button_5_click(self):
        print("Graphic Button 5 clicked")
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("Graphic Button 6 clicked")
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("Graphic Button 7 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()