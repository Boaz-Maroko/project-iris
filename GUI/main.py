import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from src.helpers import HandleCSV, HandleExcel
from GUI import Modal



class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the window title
        self.title("Iris")
        self.geometry("700x400")

        # Create a menu bar
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Create "Cluster" menu
        self.cluster_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.cluster_menu.add_command(label="Cluster CSV", command=self.open_csv)
        self.cluster_menu.add_command(label="Cluster Excel", command=self.open_excel)

        # Create "Training" menu
        self.train_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.train_menu.add_command(label="Train with CSV data", command=self.show_train_result_csv)
        self.train_menu.add_command(label="Train with Excel data", command=self.show_train_result_excel)

        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Need help?", command=lambda: print("I need help"))

        # Add menus to the menu bar
        self.menu_bar.add_cascade(label="Cluster", menu=self.cluster_menu)
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

        # Create a frame to hold clustering buttons
        self.cluster_button_frame = ttk.Frame(self.mainFrame)
        self.cluster_button_frame.pack(side="bottom", fill="x")

        # Create the cluster buttons
        self.cluster_csv_button = ttk.Button(self.cluster_button_frame, text="Cluster CSV", command=self.clean_csv)
        self.cluster_excel_button = ttk.Button(self.cluster_button_frame, text="Cluster Excel", command=self.clean_excel)

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
        self.csv_object = HandleCSV(excel_file_path=csv_path)
        if self.csv_object.show_csv_content(tree=self.tree):
            self.cluster_csv_button.pack(side="right")
            self.cluster_excel_button.pack_forget()

    def open_excel(self):
        """Open an Excel file and display its content in the Treeview"""
        excel_path = filedialog.askopenfilename(
            title="Open an Excel file",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not excel_path:
            return

        # Clear previous data in the tree
        self.tree.delete(*self.tree.get_children())

        # Load and display the Excel file
        self.excel_object = HandleExcel(excel_file_path=excel_path)
        if self.excel_object.show_excel_content(tree=self.tree):
            self.cluster_excel_button.pack(side="right")
            self.cluster_csv_button.pack_forget()

    def clean_csv(self):
        """Open modal for CSV cleaning"""
        columns = self.csv_object.clean_csv()
        self.modal = Modal(master=self, columns=columns, file_object=self.csv_object, tree=self.tree, file_type="csv")

    def clean_excel(self):
        """Open modal for Excel cleaning"""
        columns = self.excel_object.clean_excel()
        self.modal = Modal(master=self, columns=columns, file_object=self.excel_object, tree=self.tree, file_type="excel")

    def show_train_result_csv(self):
        """Show training results for CSV"""
        if not self.csv_object.is_clean:
            messagebox.showerror("Error!", f"The data in the file {self.csv_object.csv_file_path} isn't clustered!")
        else:
            train = self.csv_object.train_with_csv()
            messagebox.showinfo("Success", f"The Algorithm is trained with an accuracy of {train}")
            for widget in self.tree_frame.winfo_children():
                widget.pack_forget()
            self.canvas = self.csv_object.plot(parent=self.tree_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            

    def show_train_result_excel(self):
        """Show training results for Excel"""
        if not self.excel_object.is_clean:
            messagebox.showerror("Error!", f"The data in the file {self.excel_object.excel_file_path} isn't clustered!")
        else:
            train = self.excel_object.train_with_excel()
            messagebox.showinfo("Success", f"The Algorithm is trained with an accuracy of {train}")



if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
