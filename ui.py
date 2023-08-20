import tkinter as tk

class StatefulButton(tk.Button):
    def __init__(self, master=None, printer_data="", **kwargs):
        self.text_states = ["Ready", "Printing", "Finished", "Failure"]
        self.color_states = ["green", "yellow", "orange", "red"]
        
        printer_name, state, device = printer_data.strip().split(",")
        self.state = int(state)
        self.printer_name = printer_name
        self.device = device
        
        super().__init__(master, command=self.change_state, **kwargs)
        
        self.update_state()

    def change_state(self):
        self.state = (self.state + 1) % 4
        self.update_state()
        self.write_state_to_file()

    def update_state(self):
        self.config(text=f"{self.printer_name}\n{self.text_states[self.state]}\nDevice: {self.device}", justify=tk.CENTER)
        self.config(bg=self.color_states[self.state])
        self.config(font=('Arial', 12, 'bold'))

    def write_state_to_file(self):
        with open("printerConfig.txt", "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                printer_name, _, _ = line.strip().split(",")
                if printer_name == self.printer_name:
                    file.write(f"{printer_name},{self.state},{self.device}\n")
                else:
                    file.write(line)
            file.truncate()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Stateful Printer Buttons")
        
        self.create_buttons()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_buttons(self):
        printer_data_list = self.read_printer_data("printerConfig.txt")
        
        for index, printer_data in enumerate(printer_data_list):
            row = index // 5
            col = index % 5
            
            button = StatefulButton(self.root, printer_data=printer_data)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)
            
        for i in range(len(printer_data_list) // 5 + 1):
            self.root.grid_rowconfigure(i, weight=1)

    def read_printer_data(self, filename):
        with open(filename, 'r') as file:
            return file.readlines()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
