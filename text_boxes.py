import customtkinter
import tkinter
from constants import BORDER_WIDTH, CORNER_RADIUS

class TextBoxes(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app


        self.board_frame = customtkinter.CTkFrame(self, border_width=BORDER_WIDTH, corner_radius=CORNER_RADIUS)
        self.board_frame.pack(fill="both", expand=True)
        self.board_frame.configure(border_color="gray")

        self.textbox = customtkinter.CTkTextbox(self.board_frame, width=150, height=150)
        self.textbox.pack(fill="both", expand=True, padx=BORDER_WIDTH, pady=BORDER_WIDTH)

        self.root = self.winfo_toplevel()

        self.board_frame.bind("<FocusIn>", self.on_focus)
        self.board_frame.bind("<B1-Motion>", self.on_drag)
        self.board_frame.bind("<ButtonRelease>", self.on_drop)

    def get_highlighted_text(self):
        try:
            start = self.textbox.index("sel.first")
            end = self.textbox.index("sel.last")
            self.textbox.tag_add("sel_txt", start, end)
            self.textbox.tag_config("sel_txt", background="yellow", foreground="red")
        except tkinter.TclError:
            pass 

    def on_focus(self, event):
        self.app.active_textbox = self
    
    def on_drag(self, event):
        self.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(), y=self.root.winfo_pointery()-self.root.winfo_rooty())

    def on_drop(self, event):
        self.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx(), y=self.root.winfo_pointery()-self.root.winfo_rooty())