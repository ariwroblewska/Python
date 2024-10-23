import pandas as pd


class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self, column):
        try:
            return self.data[column].mean()
        except Exception as e:
            print(f"Error calculating mean: {e}")

    def calculate_median(self, column):
        try:
            return self.data[column].median()
        except Exception as e:
            print(f"Error calculating median: {e}")

    def calculate_std_dev(self, column):
        try:
            return self.data[column].std()
        except Exception as e:
            print(f"Error calculating standard deviation: {e}")

    def calculate_variance(self, column):
        try:
            return self.data[column].var()
        except Exception as e:
            print(f"Error calculating variance: {e}")

