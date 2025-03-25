import pandas as pd
from data import cluster_csv, cluster_excel, data_split
from training import knn_predict
from training import check_accuracy
from results import plot_for_tk


class HandleCSV:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path
        self.df = pd.read_csv(self.excel_file_path)
        self.is_clean = False

    def show_csv_content(self, tree):
        # Clear the old table content
        self.tree = tree
        self.tree.delete(*self.tree.get_children())

        # set new columns
        columns = ["#"] + list(self.df.columns)
        self.tree["columns"] = columns
        self.tree["show"] = "headings"

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="e")
        
        for i, row in self.df.iterrows():
            self.tree.insert("", "end", values=[i+1] + list(row))

        return True


    def cluster_csv(self, columns_to_use_for_clustering):
        clustered_data = cluster_csv(data=self.df, columns=columns_to_use_for_clustering)
        self.clustered = clustered_data
        self.is_clean = True

    def clean_csv(self):
        columns = [column for column in self.df.columns if pd.api.types.is_numeric_dtype(self.df[column])]
        self.valid_columns = columns
        return self.valid_columns
    
    def split_data(self):
        x_train, x_test, y_train, y_test, = data_split(self.clustered)
        return x_train, x_test, y_train, y_test


    def train_with_csv(self):
        x_train, x_test, y_train, y_test = self.split_data()
        y_pred = knn_predict(x_train, y_train, x_test)

        accuracy = check_accuracy(y_test, y_pred)
        return accuracy
    
    def plot(self, parent):
        """Plots the associated cluster plot"""
        canvas = plot_for_tk(self.clustered, parent=parent)
        return canvas



class HandleExcel:
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path
        self.df = pd.read_excel(self.excel_file_path)  # Read Excel file
        self.is_clean = False

    def show_excel_content(self, tree):
        # Clear the old table content
        self.tree = tree
        self.tree.delete(*self.tree.get_children())

        # Set new columns
        columns = ["#"] + list(self.df.columns)
        self.tree["columns"] = columns
        self.tree["show"] = "headings"

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="e")
        
        for i, row in self.df.iterrows():
            self.tree.insert("", "end", values=[i+1] + list(row))

        return True

    def cluster_excel(self, columns_to_use_for_clustering):
        clustered_data = cluster_excel(data=self.df, columns=columns_to_use_for_clustering)
        self.clustered = clustered_data
        self.is_clean = True

    def clean_excel(self):
        columns = [column for column in self.df.columns if pd.api.types.is_numeric_dtype(self.df[column])]
        self.valid_columns = columns
        return self.valid_columns
    
    def split_data(self):
        x_train, x_test, y_train, y_test = data_split(self.clustered)
        return x_train, x_test, y_train, y_test

    def train_with_excel(self):
        x_train, x_test, y_train, y_test = self.split_data()
        y_pred = knn_predict(x_train, y_train, x_test)

        accuracy = check_accuracy(y_test, y_pred)
        return accuracy
    
    def plot(self, parent):
        """Plots the associated cluster plot"""
        canvas = plot_for_tk(self.clustered, parent=parent)
        return canvas