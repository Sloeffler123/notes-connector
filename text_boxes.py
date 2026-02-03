import customtkinter
import tkinter

class TextBoxes(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.textbox = customtkinter.CTkTextbox(self, width=150, height=150)
        self.textbox.pack(fill="both", expand=True)

    def get_highlighted_text(self):
        try:
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_add("sel_txt", start, end)
            self.textbox.tag_config("sel_txt", background="yellow", foreground="red")
        except tkinter.TclError:
            pass 

    