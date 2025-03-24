import pandas as pd


def show_csv_content(csv_file_path, tree):
    # read CSV content using pandas

    df = pd.read_csv(csv_file_path)

    # Clear the old table content
    tree.delete(*tree.get_children())

    # set new columns
    columns = ["#"] + list(df.columns)
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="e")
    
    for i, row in df.iterrows():
        tree.insert("", "end", values=[i+1] + list(row))

    return True
