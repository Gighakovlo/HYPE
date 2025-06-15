# aboutus_view.py
from tkinter import Canvas, Button, PhotoImage


class AboutusView:
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

        self.controller.set_view_aboutuscontroller(self)

    def create_text(self):
        self.canvas.create_text(
            343.0, 106.0, anchor="nw", text="ABOUT US", fill="#311E10", font=("JosefinSansRoman Regular", 40 * -1)
        )
        self.canvas.create_text(
            49.0, 134.0, anchor="nw", text="Heart Yield\nPerformance Evaluator", fill="#311E10", font=("JosefinSansRoman Regular", 16 * -1)
        )
        self.canvas.create_text(
            49.0, 70.0, anchor="nw", text="HYPE",
            fill="#DD6031", font=("JosefinSlabRoman Regular", 64 * -1)
        )

    def create_images(self):
        self.image_image_1 = PhotoImage(file=self.model.relative_to_assets_aboutus("image_1.png"))
        self.image_1 = self.canvas.create_image(832.0, 453.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=self.model.relative_to_assets_aboutus("image_2.png"))
        self.image_2 = self.canvas.create_image(826.0, 449.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=self.model.relative_to_assets_aboutus("image_3.png"))
        self.image_3 = self.canvas.create_image(1075.0, 483.0, image=self.image_image_3)

        self.image_image_4 = PhotoImage(file=self.model.relative_to_assets_aboutus("image_4.png"))
        self.image_4 = self.canvas.create_image(568.0, 483.0, image=self.image_image_4)

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_1_click,
            relief="flat"
        )
        self.button_1.place(x=50.0, y=264.0, width=189.0, height=52.0)

        self.button_image_hover_1 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_hover_1.png"))
        self.button_1.bind('<Enter>', lambda e: self.button_1.config(image=self.button_image_hover_1))
        self.button_1.bind('<Leave>', lambda e: self.button_1.config(image=self.button_image_1))

        self.button_image_2 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_2_click,
            relief="flat"
        )
        self.button_2.place(x=50.0, y=339.0, width=189.0, height=52.0)

        self.button_image_hover_2 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_hover_2.png"))
        self.button_2.bind('<Enter>', lambda e: self.button_2.config(image=self.button_image_hover_2))
        self.button_2.bind('<Leave>', lambda e: self.button_2.config(image=self.button_image_2))

        self.button_image_3 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_3_click,
            relief="flat"
        )
        self.button_3.place(x=50.0, y=414.0, width=189.0, height=52.0)

        self.button_image_hover_3 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_hover_3.png"))
        self.button_3.bind('<Enter>', lambda e: self.button_3.config(image=self.button_image_hover_3))
        self.button_3.bind('<Leave>', lambda e: self.button_3.config(image=self.button_image_3))

        self.button_image_4 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_4.png"))
        self.button_4 = Button(
            self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_4_click,
            relief="flat"
        )
        self.button_4.place(x=49.0, y=489.0, width=189.0, height=52.0)

        self.button_image_hover_4 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_hover_4.png"))
        self.button_4.bind('<Enter>', lambda e: self.button_4.config(image=self.button_image_hover_4))
        self.button_4.bind('<Leave>', lambda e: self.button_4.config(image=self.button_image_4))

        self.button_image_5 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_5.png"))
        self.button_5 = Button(
            self.canvas,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_5_click,
            relief="flat"
        )
        self.button_5.place(x=52.0, y=776.0, width=184.0, height=52.0)

        self.button_image_hover_5 = PhotoImage(file=self.model.relative_to_assets_aboutus("button_hover_5.png"))
        self.button_5.bind('<Enter>', lambda e: self.button_5.config(image=self.button_image_hover_5))
        self.button_5.bind('<Leave>', lambda e: self.button_5.config(image=self.button_image_5))
