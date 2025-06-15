# profile_view.py
from tkinter import Canvas, Button, PhotoImage


class ProfileView:
    def __init__(self, master, controller, model):
        self.master = master
        self.controller = controller
        self.model = model

        self.canvas = Canvas(
            master,
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

        self.controller.set_view_profilecontroller(self)

    def create_text(self):
        self.canvas.create_text(
            49.0, 134.0, anchor="nw", text="Heart Yield\nPerformance Evaluator",
            fill="#311E10", font=("JosefinSansRoman Regular", 16 * -1)
        )
        self.canvas.create_text(
            49.0, 70.0, anchor="nw", text="HYPE",
            fill="#DD6031", font=("JosefinSlabRoman Regular", 64 * -1)
        )

    def create_images(self):
        self.image_image_1 = PhotoImage(file=self.model.relative_to_assets_profile("image_1.png"))
        self.image_1 = self.canvas.create_image(823.0, 449.0, image=self.image_image_1)

    def create_buttons(self):
        # Initialize hover images before creating buttons
        self.button_image_hover_3 = PhotoImage(file=self.model.relative_to_assets_profile("button_hover_1.png"))
        self.button_image_hover_4 = PhotoImage(file=self.model.relative_to_assets_profile("button_hover_2.png"))
        self.button_image_hover_5 = PhotoImage(file=self.model.relative_to_assets_profile("button_hover_3.png"))
        self.button_image_hover_6 = PhotoImage(file=self.model.relative_to_assets_profile("button_hover_4.png"))
        self.button_image_hover_7 = PhotoImage(file=self.model.relative_to_assets_profile("button_hover_5.png"))

        self.button_image_1 = PhotoImage(file=self.model.relative_to_assets_profile("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_1_click, relief="flat"
        )
        self.button_1.place(x=348.0, y=351.0, width=452.0, height=173.0)

        self.button_image_2 = PhotoImage(file=self.model.relative_to_assets_profile("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_2_click, relief="flat"
        )
        self.button_2.place(x=854.0, y=351.0, width=452.0, height=173.0)

        self.button_image_3 = PhotoImage(file=self.model.relative_to_assets_profile("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_3_click, relief="flat"
        )
        self.button_3.place(x=50.0, y=264.0, width=189.0, height=52.0)
        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_image_4 = PhotoImage(file=self.model.relative_to_assets_profile("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_4_click, relief="flat"
        )
        self.button_4.place(x=50.0, y=339.0, width=189.0, height=52.0)
        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)

        self.button_image_5 = PhotoImage(file=self.model.relative_to_assets_profile("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_5_click, relief="flat"
        )
        self.button_5.place(x=50.0, y=414.0, width=189.0, height=52.0)
        self.button_5.bind('<Enter>', self.button_5_hover)
        self.button_5.bind('<Leave>', self.button_5_leave)

        self.button_image_6 = PhotoImage(file=self.model.relative_to_assets_profile("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_6_click, relief="flat"
        )
        self.button_6.place(x=49.0, y=489.0, width=189.0, height=52.0)
        self.button_6.bind('<Enter>', self.button_6_hover)
        self.button_6.bind('<Leave>', self.button_6_leave)

        self.button_image_7 = PhotoImage(file=self.model.relative_to_assets_profile("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_7_click, relief="flat"
        )
        self.button_7.place(x=52.0, y=776.0, width=184.0, height=52.0)
        self.button_7.bind('<Enter>', self.button_7_hover)
        self.button_7.bind('<Leave>', self.button_7_leave)

    def button_3_hover(self, event):
        self.button_3.config(image=self.button_image_hover_3)

    def button_3_leave(self, event):
        self.button_3.config(image=self.button_image_3)

    def button_4_hover(self, event):
        self.button_4.config(image=self.button_image_hover_4)

    def button_4_leave(self, event):
        self.button_4.config(image=self.button_image_4)

    def button_5_hover(self, event):
        self.button_5.config(image=self.button_image_hover_5)

    def button_5_leave(self, event):
        self.button_5.config(image=self.button_image_5)

    def button_6_hover(self, event):
        self.button_6.config(image=self.button_image_hover_6)

    def button_6_leave(self, event):
        self.button_6.config(image=self.button_image_6)

    def button_7_hover(self, event):
        self.button_7.config(image=self.button_image_hover_7)

    def button_7_leave(self, event):
        self.button_7.config(image=self.button_image_7)
