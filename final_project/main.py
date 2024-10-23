from loading import DataLoading
from analysis import DataAnalysis
from visualization import DataVisualization

if __name__ == "__main__":
    loader = DataLoading()
    loader.load_csv("video_games_sales.csv")

    print(loader.data.head())

    analyzer = DataAnalysis(loader.data)
    # means
    print("Mean of Sales in Europe :", analyzer.calculate_mean("EU_Sales"))
    print("Mean of Sales in North America :", analyzer.calculate_mean("NA_Sales"))
    print("Mean of Sales in Japan :", analyzer.calculate_mean("JP_Sales"))
    print("Mean of Sales in All Other Countries :", analyzer.calculate_mean("Other_Sales"))
    print("Mean of Sales Globally :", analyzer.calculate_mean("Global_Sales"))

    # medians
    print("Median of Sales in Europe :", analyzer.calculate_median("EU_Sales"))
    print("Median of Sales in North America :", analyzer.calculate_median("NA_Sales"))
    print("Median of Sales in Japan :", analyzer.calculate_median("JP_Sales"))
    print("Median of Sales in All Other Countries :", analyzer.calculate_median("Other_Sales"))
    print("Median of Sales Globally :", analyzer.calculate_median("Global_Sales"))

    # standard deviations
    print("Standard Deviation European Sales :", analyzer.calculate_std_dev("EU_Sales"))
    print("Standard Deviation North American Sales :", analyzer.calculate_std_dev("NA_Sales"))
    print("Standard Deviation Japanese Sales :", analyzer.calculate_std_dev("JP_Sales"))
    print("Standard Deviation ALl Other Countries Sales :", analyzer.calculate_std_dev("Other_Sales"))
    print("Standard Deviation Global Sales :", analyzer.calculate_std_dev("Global_Sales"))

    # variances
    print("Variance European Sales :", analyzer.calculate_variance("EU_Sales"))
    print("Variance North American Sales :", analyzer.calculate_variance("NA_Sales"))
    print("Variance Japanese Sales :", analyzer.calculate_variance("JP_Sales"))
    print("Variance All Other Countries Sales  :", analyzer.calculate_variance("Other_Sales"))
    print("Variance Global Sales :", analyzer.calculate_variance("Global_Sales"))

    # visualizations
    visualizer = DataVisualization(loader.data)
    visualizer.plot_barchart("Publisher", "NA_Sales")
    visualizer.plot_graph("Platform", "EU_Sales")

    data_agg = loader.data.groupby('Genre')['JP_Sales'].sum().reset_index()
    visualizer1 = DataVisualization(data_agg)
    visualizer1.plot_pie_chart("Genre", "JP_Sales")
