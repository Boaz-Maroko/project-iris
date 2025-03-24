from tkinter import ttk


# Apply Treeview Style for Grid Lines
tree_style = ttk.Style()
tree_style.configure("Treeview", rowheight=25, borderwidth=1, relief="solid")
tree_style.configure("Treeview.Heading", font=("Arial", 10, "bold"))

# enable striped rows
tree_style.map("Treeview", background=[("selected", "#2A7FFF")])