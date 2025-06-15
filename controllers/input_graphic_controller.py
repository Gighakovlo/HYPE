from tkinter import messagebox

class InputGraphicController:
    def __init__(self, master, view_manager):
        self.master = master
        self.view = None
        self.view_manager = view_manager

    def set_view_inputgraphiccontroller(self, view):
        self.view = view

    def on_button_1_click(self):
        print("Button 1 clicked")
        file_path = self.view.entry_1.get()
        self.view_manager.model.temporary_file_path = file_path
        messagebox.showinfo("Notifikasi", "Data berhasil dimasukkan. Silakan print gambar!")
        print(self.view_manager.model.temporary_file_path)
        self.view_manager.show_graphic_view()

    def on_button_2_click(self):
        print("Button 2 clicked")
        self.view_manager.show_graphic_view()

    def on_button_3_click(self):
        print("Button 3 clicked")
        self.view_manager.show_profile_view()

    def on_button_4_click(self):
        print("Button 4 clicked")
        self.view_manager.show_graphic_view()

    def on_button_5_click(self):
        print("Button 5 clicked")
        self.view_manager.show_aboutus_view()

    def on_button_6_click(self):
        print("Button 6 clicked")
        self.view_manager.show_history_view()

    def on_button_7_click(self):
        print("Button 7 clicked")
        response = messagebox.askyesno("Konfirmasi", "Kamu ingin kembali ke halaman awal?")
        if response:
            self.view_manager.show_login_view()