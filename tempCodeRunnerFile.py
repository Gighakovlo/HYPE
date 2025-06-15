from tkinter import Tk
from views.login import LoginView
from controllers.login_controller import LoginController
from views.signup import SignupView
from controllers.signup_controller import SignupController
from views.profile import ProfileView
from controllers.profile_controller import ProfileController
from views.edit_profile import EditProfileView
from controllers.edit_profile_controller import EditProfileController
from views.show_profile import ShowProfileView
from controllers.show_profile_controller import ShowProfileController
from views.aboutus import AboutusView
from controllers.aboutus_controller import AboutusController
from views.graphic import GraphicView
from controllers.graphic_controller import GraphicController
from views.input_graphic import InputGraphicView
from controllers.input_graphic_controller import InputGraphicController
from views.printgraphic import PrintGraphicView
from controllers.printgraphic_controller import PrintGraphicController
from views.downloadgraphic import DownloadGraphicView
from controllers.download_printgraphic_controller import DownloadGraphicController
from views.history import HistoryView
from controllers.history_controller import HistoryController

from models import HypeModel

class ViewManager:
    def __init__(self, root):
        self.root = root
        self.model = HypeModel()

    def show_login_view(self):
        self.clear_view()
        controller = LoginController(self.root, self)
        view = LoginView(self.root, controller, self.model)

    def show_signup_view(self):
        self.clear_view()
        controller = SignupController(self.root, self)
        view = SignupView(self.root, self.model, controller)

    def show_profile_view(self):
        self.clear_view()
        controller = ProfileController(self.root, self)
        view = ProfileView(self.root, controller, self.model)

    def show_editprofile_view(self):
        self.clear_view()
        controller = EditProfileController(self.root, self)
        view = EditProfileView(self.root, controller, self.model)

    def show_showprofile_view(self):
        self.clear_view()
        controller = ShowProfileController(self.root, self)
        view = ShowProfileView(self.root, controller, self.model)

    def show_aboutus_view(self):
        self.clear_view()
        controller = AboutusController(self.root, self)
        view = AboutusView(self.root, controller, self.model)
    
    def show_graphic_view(self):
        self.clear_view()
        controller = GraphicController(self.root, self)
        view = GraphicView(self.root, controller, self.model)

    def show_inputgraphic_view(self):
        self.clear_view()
        controller = InputGraphicController(self.root, self)
        view = InputGraphicView(self.root, controller, self.model)

    def show_printgraphic_view(self):
        self.clear_view()
        controller = PrintGraphicController(self.root, self)
        view = PrintGraphicView(self.root, controller, self.model)

    def show_downloadgraphic_view(self):
        self.clear_view()
        controller = DownloadGraphicController(self.root, self)
        view = DownloadGraphicView(self.root, controller, self.model)

    def show_history_view(self):  
        self.clear_view()
        controller = HistoryController(self.root, self)
        view = HistoryView(self.root, controller, self.model)

    def clear_view(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = Tk()
    root.geometry("1440x900")
    root.resizable(False, False)

    view_manager = ViewManager(root)
    view_manager.show_login_view()
    root.mainloop()
