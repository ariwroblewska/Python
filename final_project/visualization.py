import matplotlib.pyplot as plt
import seaborn as sns


class DataVisualization:
    def __init__(self, data):
        self.data_agg = None
        self.data = data

    def plot_barchart(self, column1, column2):
        try:
            plt.figure(figsize=(10, 6))
            sns.set_palette('husl')
            sns.barplot(x=self.data[column1], y=self.data[column2])
            plt.title(f'Bar Chart of {column1} and {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting histogram: {e}")

    def plot_graph(self, column1, column2):
        try:
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=self.data[column1], y=self.data[column2])
            plt.title(f'{column1} vs {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.grid(True)
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting graph: {e}")

    def plot_pie_chart(self, column1, column2):
        try:
            self.data_agg = self.data.groupby(column1)[column2].sum().reset_index()
            print(self.data_agg)
            plt.figure(figsize=(8, 8))
            plt.pie(self.data[column2], labels=self.data[column1], autopct='%1.1f%%', startangle=140)
            plt.title(f'Pie Chart of {column1} and {column2}')
            plt.show()
        except Exception as e:
            print(f"Error plotting pie chart: {e}")
