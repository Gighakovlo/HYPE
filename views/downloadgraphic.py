from tkinter import Canvas, Button, PhotoImage, Label

class DownloadGraphicView:
    def __init__(self, master, controller, model):
        self.master = master
        self.controller = controller
        self.model = model
        self.widgets = []

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
        self.widgets.append(self.canvas)

        self.create_text()
        self.create_images()
        self.create_buttons()

        self.controller.set_view_downloadgraphiccontroller(self)

        print(self.model.current_graphic_path)
        if self.model.current_graphic_path:
            self.graphic_label = Label(self.master)
            self.graphic_label.place(x=718, y=230)  # Adjust placement as needed
            img = PhotoImage(file=self.model.current_graphic_path)
            self.graphic_label.config(image=img)
            self.graphic_label.image = img
            self.widgets.append(self.graphic_label)
            print("chart berhasil dibuat")
        else:
            print("chart gagal dibuat")

    def create_text(self):
        text1 = self.canvas.create_text(
            49.0, 134.0, anchor="nw", text="Heart Yield\nPerformance Evaluator",
            fill="#311E10", font=("JosefinSansRoman Regular", 16 * -1)
        )
        text2 = self.canvas.create_text(
            49.0, 70.0, anchor="nw", text="HYPE",
            fill="#DD6031", font=("JosefinSlabRoman Regular", 64 * -1)
        )
        self.widgets.extend([text1, text2])

        self.name_label = Label(self.master, text=f"Nama: {self.model.temporary_name}", bg="#ECE4B7", font=("JosefinSansRoman Regular", 16))
        self.name_label.place(x=381, y=348)
        print("label telah dibuat")
        self.widgets.append(self.name_label)

        self.age_label = Label(self.master, text=f"Usia: {self.model.temporary_age}", bg="#ECE4B7", font=("JosefinSansRoman Regular", 16))
        self.age_label.place(x=381, y=463)
        print("label telah dibuat")
        self.widgets.append(self.age_label)

    def create_images(self):
        self.image_image_1 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("image_1.png"))
        image_1 = self.canvas.create_image(823.0, 449.0, image=self.image_image_1)
        self.widgets.append(image_1)

        self.image_image_2 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("image_2.png"))
        image_2 = self.canvas.create_image(1022.0, 436.0, image=self.image_image_2)
        self.widgets.append(image_2)
        
        self.image_image_3 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("image_3.png"))
        image_3 = self.canvas.create_image(486.0, 437.0, image=self.image_image_3)
        self.widgets.append(image_3)
    def create_buttons(self):
        self.button_image_hover_3 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_hover_1.png"))
        self.button_image_hover_4 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_hover_2.png"))
        self.button_image_hover_5 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_hover_3.png"))
        self.button_image_hover_6 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_hover_4.png"))
        self.button_image_hover_7 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_hover_5.png"))

        self.button_image_1 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_1.png"))
        self.button_1 = Button(
            self.master,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_1_click,
            relief="flat"
        )
        self.button_1.place(x=722.0, y=731.0, width=209.0, height=64.0)
        self.widgets.append(self.button_1)

        self.button_image_2 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_2.png"))
        self.button_2 = Button(
            self.master,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_2_click,
            relief="flat"
        )
        self.button_2.place(x=1199.0, y=688.0, width=141.0, height=140.0)
        self.widgets.append(self.button_2)

        self.button_image_3 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_3.png"))
        self.button_3 = Button(
            self.master,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_3_click,
            relief="flat"
        )
        self.button_3.place(x=50.0, y=279.0, width=189.0, height=52.0)
        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)
        self.widgets.append(self.button_3)

        self.button_image_4 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_4.png"))
        self.button_4 = Button(
            self.master,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_4_click,
            relief="flat"
        )
        self.button_4.place(x=50.0, y=354.0, width=189.0, height=52.0)
        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)
        self.widgets.append(self.button_4)

        self.button_image_5 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_5.png"))
        self.button_5 = Button(
           self.master,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_5_click,
            relief="flat"
        )
        self.button_5.place(x=50.0, y=429.0, width=189.0, height=52.0)
        self.button_5.bind('<Enter>', self.button_5_hover)
        self.button_5.bind('<Leave>', self.button_5_leave)
        self.widgets.append(self.button_5)

        self.button_image_6 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_6.png"))
        self.button_6 = Button(
            self.master,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_6_click,
            relief="flat"
        )
        self.button_6.place(x=49.0, y=504.0, width=189.0, height=52.0)
        self.button_6.bind('<Enter>', self.button_6_hover)
        self.button_6.bind('<Leave>', self.button_6_leave)
        self.widgets.append(self.button_6)

        self.button_image_7 = PhotoImage(file=self.model.relative_to_assets_downloadgraphic("button_7.png"))
        self.button_7 = Button(
            self.master,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_7_click,
            relief="flat"
        )
        self.button_7.place(x=52.0, y=791.0, width=184.0, height=52.0)
        self.button_7.bind('<Enter>', self.button_7_hover)
        self.button_7.bind('<Leave>', self.button_7_leave)
        self.widgets.append(self.button_7)

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
