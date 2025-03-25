import tkinter as tk
from tkinter import ttk


class Modal(tk.Toplevel):
    def __init__(self, master, columns, file_object, tree, file_type, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Choose Columns")
        self.geometry("300x250")
        self.transient(master)
        self.grab_set()

        self.file_object = file_object  # Could be either HandleCSV or HandleExcel
        self.file_type = file_type  # 'csv' or 'excel'
        self.columns_for_clustering = columns

        # Create a frame to hold the data
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        self.label = ttk.Label(self.frame, text="Select columns for clustering:", font=("Arial", 12))
        self.label.pack(pady=5)

        self.select_columns = tk.Listbox(self.frame, selectmode=tk.MULTIPLE, height=6)

        for option in self.columns_for_clustering:
            self.select_columns.insert(tk.END, option)

        self.select_columns.pack(pady=5, fill="x")

        self.done_button = ttk.Button(self.frame, text="Done", command=lambda: self.done(tree=tree))
        self.done_button.pack(pady=10)

    def done(self, tree):
        selected_items = [self.select_columns.get(item) for item in self.select_columns.curselection()]
        self.selected_items = selected_items

        # Check if it's a CSV or Excel file and call the appropriate method
        if self.file_type == "csv":
            self.file_object.cluster_csv(self.selected_items)
            self.file_object.show_csv_content(tree=tree)
        elif self.file_type == "excel":
            self.file_object.cluster_excel(self.selected_items)
            self.file_object.show_excel_content(tree=tree)

        self.destroy()
