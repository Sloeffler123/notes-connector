
import customtkinter
from constants import BORDER_WIDTH, CORNER_RADIUS

class BorderFrame(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, border_width=BORDER_WIDTH, corner_radius=CORNER_RADIUS)

        self.app = app

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=BORDER_WIDTH, pady=BORDER_WIDTH)

        self.x_drag = 0
        self.y_drag = 0
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.frame.bind("<Button-1>", self.on_click)
        self.frame.bind("<B1-Motion>", self.on_drag)
    
    
    def on_click(self, event):
        self.app.active_frame = self
        self.x_drag = event.x
        self.y_drag = event.y

    def on_drag(self, event):
        x = self.winfo_x() + event.x - self.x_drag
        y = self.winfo_y() + event.y - self.y_drag
        self.place(x=x, y=y)