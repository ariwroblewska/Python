import pandas as pd


class DataLoading:
    def __init__(self):
        self.data = None

    def load_csv(self, file_path):
        try:
            self.data = pd.read_csv(file_path, nrows=250, sep=';')
            print("CSV file loaded successfully.")
        except Exception as e:
            print(f"Error loading CSV file: {e}")
