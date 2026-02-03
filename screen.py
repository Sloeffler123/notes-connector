import customtkinter
import tkinter
from border_frame import BorderFrame
from text_boxes import *


class MainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("My app")
        self.geometry("1000x800")
        self.update_idletasks()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        self.main_frame = customtkinter.CTkFrame(master=self)

        self.active_frame = None

        self.main_frame.grid(row=0, column=0, sticky="nesw", pady=(28,0))
        self.main_frame.configure()
        # once add is slected I need to be able to click somewhere on the screen to place the textbox

        # should use place when adding the text boxes

    def create_widgets(self):
        button_frame = customtkinter.CTkFrame(self)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.configure(height=30)
        button_frame.grid(row=0, column=0, sticky="nwe")

        self.open_button = customtkinter.CTkButton(button_frame, text="Open", command=self.on_open)
        self.open_button.grid(row=0, column=0, padx=5)

        self.save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.on_save)
        self.save_button.grid(row=0, column=1, padx=5)

        self.add_button = customtkinter.CTkButton(button_frame, text="Add", command=self.on_add)
        self.add_button.grid(row=0, column=2, padx=5)

        self.delete_button = customtkinter.CTkButton(button_frame, text="Delete", command=self.on_delete)
        self.delete_button.grid(row=0, column=3, padx=5)

        self.font_positive_button = customtkinter.CTkButton(button_frame, text="+", width=10, command=self.on_positive_button)
        self.font_positive_button.grid(row=0, column=4, padx=5)

        self.font_number_entry = customtkinter.CTkEntry(button_frame, width=30)
        self.font_number_entry.insert(index=0, string="12")
        self.font_number_entry.grid(row=0, column=5, padx=5)

        self.font_minus_button = customtkinter.CTkButton(button_frame, text="-", width=10)
        self.font_minus_button.grid(row=0, column=6, padx=5)

        self.dark_mode_switch = customtkinter.CTkSwitch(button_frame, text="Dark mode", command=self.switch_on)
        self.dark_mode_switch.grid(row=0, column=7, padx=5)

    def create_text_box(self, event):
        x = event.x
        y = event.y
        border_frame = BorderFrame(self.main_frame, self)
        border_frame.place(x=x,y=y)
        tb1 = TextBoxes(border_frame.frame)
        tb1.pack(fill="both", expand=True)
        
        self.unbind("<Button-1>")

    
    def on_positive_button(self):
        if self.active_frame is None:
            return 
        self.active_frame.get_highlighted_text()
        # get highlighted text and make font bigger

    def on_add(self):
        self.bind("<Button-1>", self.create_text_box)

    def on_open(self):
        print("open pressed")

    def on_save(self):
        print("save pressed")
    
    def on_delete(self):
        print("delete pressed")
    
    def switch_on(self):
        if customtkinter.get_appearance_mode() == "Dark":
            customtkinter.set_appearance_mode("light")
        else:
            customtkinter.set_appearance_mode("dark")
    

    
# main()
screen = MainScreen()
screen.mainloop()
# box = TextBoxes()