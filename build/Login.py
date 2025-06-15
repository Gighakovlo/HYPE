from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

class HypeView:
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
        self.create_entries()

    def relative_to_assets(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame10") / Path(path)

    def create_text(self):
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(881.0, 461.0, image=self.image_image_1)

        self.canvas.create_text(
            58.0, 62.0, anchor="nw", text="HYPE", fill="#DD6031", font=("JosefinSlabRoman Regular", 96 * -1)
        )
        self.canvas.create_text(
            58.0, 156.0, anchor="nw", text="Heart Yield\nPerformance Evaluator", fill="#311E10", font=("JosefinSansRoman Regular", 24 * -1)
        )
        self.canvas.create_text(
            787.0, 322.0, anchor="nw", text="USERNAME", fill="#DD6031", font=("JosefinSansRoman Regular", 32 * -1)
        )
        self.canvas.create_text(
            791.0, 459.0, anchor="nw", text="PASSWORD", fill="#DD6031", font=("JosefinSansRoman Regular", 32 * -1)
        )

    def create_images(self):
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(1258.0, 110.0, image=self.image_image_2)

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self.canvas,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_1_click,
            relief="flat"
        )
        self.button_1.place(x=1219.0, y=742.0, width=134.0, height=66.0)

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self.canvas,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_2_click,
            relief="flat"
        )
        self.button_2.place(x=1055.0, y=742.0, width=134.0, height=66.0)

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self.canvas,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_3_click,
            relief="flat"
        )
        self.button_3.place(x=41.0, y=457.0, width=312.0, height=64.0)
        self.button_image_hover_3 = PhotoImage(file=self.relative_to_assets("button_hover_1.png"))
        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            self.canvas,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.on_button_4_click,
            relief="flat"
        )
        self.button_4.place(x=41.0, y=373.0, width=312.0, height=64.0)
        self.button_image_hover_4 = PhotoImage(file=self.relative_to_assets("button_hover_2.png"))
        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)

    def create_entries(self):
        self.canvas.create_rectangle(652.0, 508.0, 1111.0, 572.0, fill="#D9DD92", outline="")
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(881.0, 539.5, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#ECE4B7", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=674.0, y=514.0, width=414.0, height=49.0)

        self.canvas.create_rectangle(652.0, 370.0, 1111.0, 434.0, fill="#D9DD92", outline="")
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(881.0, 402.5, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#ECE4B7", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=674.0, y=377.0, width=414.0, height=49.0)

    def button_3_hover(self, event):
        self.button_3.config(image=self.button_image_hover_3)

    def button_3_leave(self, event):
        self.button_3.config(image=self.button_image_3)

    def button_4_hover(self, event):
        self.button_4.config(image=self.button_image_hover_4)

    def button_4_leave(self, event):
        self.button_4.config(image=self.button_image_4)
