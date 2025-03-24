import tkinter as tk
from tkinter import ttk, filedialog
from src.helpers import show_csv_content  # Ensure this function is correctly implemented


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the window title
        self.title("Iris")
        self.geometry("700x400")

        # Create a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Create "Clean" menu
        self.clean_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.clean_menu.add_command(label="Clean CSV", command=self.open_csv)
        self.clean_menu.add_command(label="Clean Excel", command="")

        # Create "Training" menu
        self.train_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.train_menu.add_command(label="Train with CSV data", command=lambda: print("Training with CSV"))
        self.train_menu.add_command(label="Train with Excel data", command=lambda: print("Training with Excel"))

        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Need help?", command=lambda: print("I need help"))

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label="Clean", menu=self.clean_menu)
        self.menu_bar.add_cascade(label="Train", menu=self.train_menu)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Create the main frame
        self.mainFrame = ttk.Frame(self, borderwidth=3, relief="flat")
        self.mainFrame.pack(fill="both", ipadx=10, ipady=10, expand=True)
        self.mainFrame.pack_propagate(False)

        # Create the tree frame
        self.tree_frame = ttk.Frame(self.mainFrame)
        self.tree_frame.pack(fill="both", expand=True)
        self.tree_frame.pack_propagate(False)  # Prevents shrinking

        # Create Treeview
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(side="left", fill="both", expand=True)

        # Create and add vertical scrollbar
        self.vertical_scroll_bar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.vertical_scroll_bar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.vertical_scroll_bar.set)

        # Create and add horizontal scrollbar
        self.horizontal_scroll_bar = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.horizontal_scroll_bar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=self.horizontal_scroll_bar.set)


        # create a frame to hold cleaning buttons
        self.clean_btn_frame = ttk.Button(self.mainFrame)
        self.clean_btn_frame.pack(side="bottom", fill="x")


        # create the clean button
        self.clean_btn = ttk.Button(self.clean_btn_frame, text="Clean")
        

    def open_csv(self):
        """Open a CSV file and display its content in the Treeview"""
        csv_path = filedialog.askopenfilename(
            title="Open a CSV file",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not csv_path:
            return
        
        # Clear previous data in the tree
        self.tree.delete(*self.tree.get_children())

        # Load and display the CSV file
        if show_csv_content(csv_file_path=csv_path, tree=self.tree):
            self.clean_btn.pack(side="right")


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
