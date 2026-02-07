
import customtkinter
from constants import BORDER_WIDTH, CORNER_RADIUS



class BorderFrame(customtkinter.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, border_width=BORDER_WIDTH, cursor="fleur")

        self.app = app
        
        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=BORDER_WIDTH, pady=BORDER_WIDTH)

        self.x_drag = 0
        self.y_drag = 0
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_realease)
        self.bind("<Enter>", self.on_enter)
        self.frame.bind("<Button-1>", self.on_click)
        self.frame.bind("<B1-Motion>", self.on_drag)

    def on_click(self, event):
        self.app.active_frame = self
        
        width = self.winfo_width()
        height = self.winfo_height()

        if (event.x > width - 10) and (event.y > height - 10):
            print("in corner")
            self.not_in_corner = False
        else:
            self.x_drag = event.x
            self.y_drag = event.y
            self.not_in_corner = True
            self.width_start = event.x
            self.height_start = event.y
            
    def on_enter(self, event):
        width = self.winfo_width()
        height = self.winfo_height()
        if event.x > width - 10 and event.y > height - 10:
            self.configure(cursor="bottom_right_corner")
            
    def on_drag(self, event):
        if self.not_in_corner:
            x = self.winfo_x() + event.x - self.x_drag
            y = self.winfo_y() + event.y - self.y_drag
            self.place(x=x, y=y)
        else:
            self.configure(cursor="bottom_right_corner")
            self.place_configure(width=event.x, height=event.y)
    
    def on_realease(self, event):
        self.configure(cursor="fleur")