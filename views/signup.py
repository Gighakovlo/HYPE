from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from models import HypeModel
from controllers.signup_controller import SignupController

class SignupView:
    def __init__(self, master, model, controller):
        model = HypeModel()
        self.master = master
        self.model = model
        self.controller = controller

        self.canvas = Canvas(
            self.master,
            bg="#ECE4B7",
            height=900,
            width=1440,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        self.create_text()
        self.create_images()
        self.create_buttons()
        self.create_entries()
               
        self.controller.set_view_signupcontroller(self)

    def create_text(self):
        self.image_image_1 = PhotoImage(
            file=self.model.relative_to_assets_signup("image_1.png"))
        self.image_1 = self.canvas.create_image(881.0, 461.0, image=self.image_image_1)
        self.canvas.create_text(
            58.0, 62.0, anchor="nw", text="HYPE", fill="#DD6031",
            font=("JosefinSlabRoman Regular", 96 * -1)
        )
        self.canvas.create_text(
            58.0, 156.0, anchor="nw", text="Heart Yield\nPerformance Evaluator",
            fill="#311E10", font=("JosefinSansRoman Regular", 24 * -1)
        )
        self.canvas.create_text(
            828.0, 240.0, anchor="nw", text="EMAIL", fill="#DD6031",
            font=("JosefinSansRoman Regular", 32 * -1)
        )
        self.canvas.create_text(
            788.0, 385.0, anchor="nw", text="USERNAME", fill="#DD6031",
            font=("JosefinSansRoman Regular", 32 * -1)
        )
        self.canvas.create_text(
            791.0, 537.0, anchor="nw", text="PASSWORD", fill="#DD6031",
            font=("JosefinSansRoman Regular", 32 * -1)
        )

    def create_images(self):
        self.image_image_2 = PhotoImage(
            file=self.model.relative_to_assets_signup("image_2.png"))
        self.image_2 = self.canvas.create_image(1258.0, 110.0, image=self.image_image_2)

    def create_buttons(self):
        self.button_image_1 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1, borderwidth=0, highlightthickness=0,
            command=self.controller.button_1_clicked, relief="flat"
        )
        self.button_1.place(x=1219.0, y=742.0, width=134.0, height=66.0)

        self.button_image_2 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2, borderwidth=0, highlightthickness=0,
            command=self.controller.button_2_clicked, relief="flat"
        )
        self.button_2.place(x=1055.0, y=742.0, width=134.0, height=66.0)

        self.button_image_3 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3, borderwidth=0, highlightthickness=0,
            command=self.controller.button_3_clicked, relief="flat"
        )
        self.button_3.place(x=41.0, y=457.0, width=312.0, height=64.0)
        self.button_image_hover_3 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_hover_1.png"))
        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_image_4 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4, borderwidth=0, highlightthickness=0,
            command=self.controller.button_4_clicked, relief="flat"
        )
        self.button_4.place(x=41.0, y=373.0, width=312.0, height=64.0)
        self.button_image_hover_4 = PhotoImage(
            file=self.model.relative_to_assets_signup("button_hover_2.png"))
        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)

    def create_entries(self):
        self.entry_image_1 = PhotoImage(
            file=self.model.relative_to_assets_signup("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(879.0, 475.5, image=self.entry_image_1)
        self.entry_1 = Entry(
            self.canvas, bd=0, bg="#ECE4B7", fg="#000716", highlightthickness=0
        )
        self.entry_1.place(x=672.0, y=450.0, width=414.0, height=49.0)

        self.entry_image_2 = PhotoImage(
            file=self.model.relative_to_assets_signup("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(880.0, 319.5, image=self.entry_image_2)
        self.entry_2 = Entry(
            self.canvas, bd=0, bg="#ECE4B7", fg="#000716", highlightthickness=0
        )
        self.entry_2.place(x=673.0, y=294.0, width=414.0, height=49.0)

        self.entry_image_3 = PhotoImage(
            file=self.model.relative_to_assets_signup("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(880.0, 615.5, image=self.entry_image_3)
        self.entry_3 = Entry(
            self.canvas, bd=0, bg="#ECE4B7", fg="#000716", highlightthickness=0
        )
        self.entry_3.place(x=673.0, y=590.0, width=414.0, height=49.0)

    def button_3_hover(self, event):
        self.button_3.config(image=self.button_image_hover_3)

    def button_3_leave(self, event):
        self.button_3.config(image=self.button_image_3)

    def button_4_hover(self, event):
        self.button_4.config(image=self.button_image_hover_4)

    def button_4_leave(self, event):
        self.button_4.config(image=self.button_image_4)
