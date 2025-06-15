from pathlib import Path

class HypeModel:
    def __init__(self):
        self.temporary_name = ""
        self.temporary_age = ""
        self.temporary_file_path = ""
        self.current_graphic_path = ""


    def relative_to_assets(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame10") / Path(path)

    def relative_to_assets_history(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame0") / Path(path)

    def relative_to_assets_downloadgraphic(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Documents\PPBO\HYPE\assets\frame1") / Path(path)

    def relative_to_assets_printgraphic(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame2") / Path(path)

    def relative_to_assets_inputgraphic(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Documents\PPBO\HYPE\assets\frame3") / Path(path)
    
    def relative_to_assets_graphic(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Documents\PPBO\HYPE\assets\frame4") / Path(path)

    def relative_to_assets_showprofile(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame5") / Path(path)

    def relative_to_assets_editprofile(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame6") / Path(path)

    def relative_to_assets_profile(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame7") / Path(path)

    def relative_to_assets_aboutus(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame8") / Path(path)

    def relative_to_assets_signup(self, path: str) -> Path:
        return Path(__file__).parent / Path(r"C:\Users\gigah\Downloads\Tkinter-Designer-master\Tkinter-Designer-master\build\assets\frame9") / Path(path)
