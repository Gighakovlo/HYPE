from tkinter import Canvas, Button, PhotoImage, Label, Scrollbar, Frame, ttk
import os
import csv

class HistoryView:
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
        self.create_table()

        self.controller.set_view_historycontroller(self)

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
        self.image_image_1 = PhotoImage(file=self.model.relative_to_assets_history("image_1.png"))
        self.image_1 = self.canvas.create_image(823.0, 449.0, image=self.image_image_1)
        self.image_image_2 = PhotoImage(file=self.model.relative_to_assets_history("image_2.png"))
        self.image_2 = self.canvas.create_image(828.0, 443.0, image=self.image_image_2)

    def create_buttons(self):
        # Initialize hover images before creating buttons
        self.button_image_hover_1 = PhotoImage(file=self.model.relative_to_assets_history("button_hover_1.png"))
        self.button_image_hover_2 = PhotoImage(file=self.model.relative_to_assets_history("button_hover_2.png"))
        self.button_image_hover_3 = PhotoImage(file=self.model.relative_to_assets_history("button_hover_3.png"))
        self.button_image_hover_4 = PhotoImage(file=self.model.relative_to_assets_history("button_hover_4.png"))
        self.button_image_hover_5 = PhotoImage(file=self.model.relative_to_assets_history("button_hover_5.png"))

        self.button_image_1 = PhotoImage(file=self.model.relative_to_assets_history("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_1_click, relief="flat"
        )
        self.button_1.place(x=1199.0, y=688.0, width=141.0, height=140.0)
        self.widgets.append(self.button_1)

        self.button_image_2 = PhotoImage(file=self.model.relative_to_assets_history("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_2_click, relief="flat"
        )
        self.button_2.place(x=50.0, y=279.0, width=189.0, height=52.0)
        self.button_2.bind('<Enter>', self.button_2_hover)
        self.button_2.bind('<Leave>', self.button_2_leave)
        self.widgets.append(self.button_2)

        self.button_image_3 = PhotoImage(file=self.model.relative_to_assets_history("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_3_click, relief="flat"
        )
        self.button_3.place(x=50.0, y=354.0, width=189.0, height=52.0)
        self.button_3.bind('<Enter>', self.button_3_hover)
        self.button_3.bind('<Leave>', self.button_3_leave)
        self.widgets.append(self.button_3)

        self.button_image_4 = PhotoImage(file=self.model.relative_to_assets_history("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_4_click, relief="flat"
        )
        self.button_4.place(x=50.0, y=429.0, width=189.0, height=52.0)
        self.button_4.bind('<Enter>', self.button_4_hover)
        self.button_4.bind('<Leave>', self.button_4_leave)
        self.widgets.append(self.button_4)

        self.button_image_5 = PhotoImage(file=self.model.relative_to_assets_history("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_5_click, relief="flat"
        )
        self.button_5.place(x=49.0, y=504.0, width=189.0, height=52.0)
        self.button_5.bind('<Enter>', self.button_5_hover)
        self.button_5.bind('<Leave>', self.button_5_leave)
        self.widgets.append(self.button_5)

        self.button_image_6 = PhotoImage(file=self.model.relative_to_assets_history("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6, borderwidth=0, highlightthickness=0,
            command=self.controller.on_button_6_click, relief="flat"
        )
        self.button_6.place(x=52.0, y=791.0, width=184.0, height=52.0)
        self.button_6.bind('<Enter>', self.button_6_hover)
        self.button_6.bind('<Leave>', self.button_6_leave)
        self.widgets.append(self.button_6)

    def button_2_hover(self, event):
        self.button_2.config(image=self.button_image_hover_1)

    def button_2_leave(self, event):
        self.button_2.config(image=self.button_image_2)

    def button_3_hover(self, event):
        self.button_3.config(image=self.button_image_hover_2)

    def button_3_leave(self, event):
        self.button_3.config(image=self.button_image_3)

    def button_4_hover(self, event):
        self.button_4.config(image=self.button_image_hover_3)

    def button_4_leave(self, event):
        self.button_4.config(image=self.button_image_4)

    def button_5_hover(self, event):
        self.button_5.config(image=self.button_image_hover_4)

    def button_5_leave(self, event):
        self.button_5.config(image=self.button_image_5)

    def button_6_hover(self, event):
        self.button_6.config(image=self.button_image_hover_5)

    def button_6_leave(self, event):
        self.button_6.config(image=self.button_image_6)

    def create_table(self):
        # Get current user
        current_user = os.getenv('CURRENT_USER', '')

        # Create a frame for the table
        frame = Frame(self.master)
        frame.place(x=347, y=250, width=970, height=400)

        # Create a scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')

        # Create the treeview
        tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set)
        tree.pack(expand=True, fill='both')
        scrollbar.config(command=tree.yview)

        # Define columns
        tree['columns'] = ('Username', 'Login Time')
        tree.column('#0', width=0, stretch='no')
        tree.column('Username', anchor='center', width=400)
        tree.column('Login Time', anchor='center', width=400)

        # Create headings
        tree.heading('#0', text='', anchor='center')
        tree.heading('Username', text='Username', anchor='center')
        tree.heading('Login Time', text='Login Time', anchor='center')

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background = "#EABE7C", fieldbackgrounds = "#EABE7C", foreground = "white")
        style.configure("Treeview.Heading", background = "#311E10", fieldbackgrounds = "#311E10", foreground = "white")
        style.map("Treeview", background = [ ("selected", "#6C1D00") ])
        # Read CSV and insert data
        try:
            with open('user_login.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Username'] == current_user:
                        tree.insert('', 'end', values=(row['Username'], row['Login Time']))
        except FileNotFoundError:
            print("File user_login.csv tidak ditemukan.")
        
        self.widgets.append(frame)
        self.widgets.append(tree)
        self.widgets.append(scrollbar)
