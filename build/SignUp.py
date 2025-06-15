from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame9")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x900")
window.configure(bg = "#ECE4B7")


canvas = Canvas(
    window,
    bg = "#ECE4B7",
    height = 900,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    58.0,
    62.0,
    anchor="nw",
    text="HYPE",
    fill="#DD6031",
    font=("JosefinSlabRoman Regular", 96 * -1)
)

canvas.create_text(
    58.0,
    156.0,
    anchor="nw",
    text="Heart Yield\nPerformance Evaluator",
    fill="#311E10",
    font=("JosefinSansRoman Regular", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    881.0,
    461.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1219.0,
    y=742.0,
    width=134.0,
    height=66.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1055.0,
    y=742.0,
    width=134.0,
    height=66.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=41.0,
    y=457.0,
    width=312.0,
    height=64.0
)

button_image_hover_3 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_3_hover(e):
    button_3.config(
        image=button_image_hover_3
    )
def button_3_leave(e):
    button_3.config(
        image=button_image_3
    )

button_3.bind('<Enter>', button_3_hover)
button_3.bind('<Leave>', button_3_leave)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=41.0,
    y=373.0,
    width=312.0,
    height=64.0
)

button_image_hover_4 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_4_hover(e):
    button_4.config(
        image=button_image_hover_4
    )
def button_4_leave(e):
    button_4.config(
        image=button_image_4
    )

button_4.bind('<Enter>', button_4_hover)
button_4.bind('<Leave>', button_4_leave)


canvas.create_text(
    828.0,
    240.0,
    anchor="nw",
    text="EMAIL",
    fill="#DD6031",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    788.0,
    385.0,
    anchor="nw",
    text="USERNAME",
    fill="#DD6031",
    font=("JosefinSansRoman Regular", 32 * -1)
)

canvas.create_text(
    791.0,
    537.0,
    anchor="nw",
    text="PASSWORD",
    fill="#DD6031",
    font=("JosefinSansRoman Regular", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1258.0,
    110.0,
    image=image_image_2
)

canvas.create_rectangle(
    651.0,
    583.0,
    1110.0,
    647.0,
    fill="#D9DD92",
    outline="")

canvas.create_rectangle(
    650.0,
    443.0,
    1109.0,
    507.0,
    fill="#D9DD92",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    879.0,
    475.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#ECE4B7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=672.0,
    y=450.0,
    width=414.0,
    height=49.0
)

canvas.create_rectangle(
    651.0,
    287.0,
    1110.0,
    351.0,
    fill="#D9DD92",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    880.0,
    319.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#ECE4B7",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=673.0,
    y=294.0,
    width=414.0,
    height=49.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    880.0,
    615.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#ECE4B7",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=673.0,
    y=590.0,
    width=414.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
