import customtkinter



class MainScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("My app")
        self.geometry("1000x800")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(master=self)
        self.main_frame.grid(row=0, column=0)
        # once add is slected I need to be able to click somewhere on the screen to place the textbox
        


        # should use place when adding the text boxes

        self.create_widgets()

    def create_widgets(self):
        button_frame = customtkinter.CTkFrame(self)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.place(x=0, y=0)

        self.open_button = customtkinter.CTkButton(button_frame, text="Open", command=self.on_open)
        self.open_button.grid(row=0, column=0, pady=10)

        self.save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.on_save)
        self.save_button.grid(row=1, column=0, pady=10)

        # add button
        self.add_button = customtkinter.CTkButton(button_frame, text="Add", command=self.on_add)
        self.add_button.grid(row=2, column=0, pady=20)

        self.delete_button = customtkinter.CTkButton(button_frame, text="Delete", command=self.on_delete)
        self.delete_button.grid(row=3, column=0, pady=5)

        # swtich for dark mode
        self.dark_mode_switch = customtkinter.CTkSwitch(button_frame, text="Dark mode", command=self.switch_on)
        self.dark_mode_switch.grid(row=4, column=0, pady=20)

    def on_add(self):
        tb1 = TextBoxes(self.main_frame, label_text="tb1")
        tb1.grid(row=0, column=0)

    def on_open(self):
        print("open pressed")

    def on_save(self):
        print("save pressed")
    
    def on_delete(self):
        print("delete pressed")
    
    def switch_on(self):
        print("switch turned on")
        customtkinter.set_appearance_mode("dark")
    
class TextBoxes(customtkinter.CTkFrame):
    def __init__(self, parent, label_text):
        super().__init__(parent)

        # self.label = customtkinter.CTkLabel(self)
        # self.label.grid(row=0, column=0)

        # make first line in box the text box
        # then everything else is the body text
        self.textbox = customtkinter.CTkTextbox(self, corner_radius=5, border_width=5)
        self.textbox.grid(row=0, column=0)

    # top of screen bar
        # add button that adds a text box
        # zoom in and out option
        # dark mode
        # Save button
        # open button
    
# main()
screen = MainScreen()
screen.mainloop()
# box = TextBoxes()