import pandas as pd
from context import Visualizer
from strategies import *
from data_extractor import Extractor
import numpy as np
from distribution_context import Distribution
from distribution_strategies import *

df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

context = Visualizer()
s = ScatterPlotter()
# e = Extractor()
context.strategy = s
# tire_df = e.tire_age_vs_lap_time(1052)
# context.strategy = ScatterPlotter()
# context.plot(
#     df=tire_df,
#     x="tire_age",
#     y="seconds",
#     x_label="Age of tires (laps)",
#     y_label="Lap time (seconds)",
#     title="Lap times for different tire ages in Bahrain 2021"
# )
#
# data = Extractor("filip_csvs")
# basket_df = data.stats[data.stats["Year"] == 2020]
#
# context.strategy = ScatterPlotter()
# context.plot(df=basket_df, x="PF",y="PTS", x_label="Personal fouls", y_label="Points scored", title="Points scored vs personal fouls in 2020")

#

x = np.random.normal(0, 1, 1000)
y = x + np.random.normal(0, 3, 1000)

dummy_df = pd.DataFrame({
    "x": x,
    "y": y,
    "z": x + np.random.poisson(0.1, 1000),
    "w": np.random.chisquare(4, 1000)
})

# data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data = pd.DataFrame(data, columns=['x', 'y'])
# print(data)

# ds = ViolinPlotter()
# context.strategy = ds
# context.plot(dummy_df, title="title")
dummy_df.to_csv("processed_csvs/dummy.csv", index=False)

# bin_size = 20
# context.strategy = LinePlotter()
# context.plot(
#     df=dummy_df,
#     x="year",
#     y="dummy_time_series",
#     x_label="year",
#     y_label="dummy time series",
#     title=f"Dummy data to show scaling of x-axis with bin size {bin_size}",
#     bin_size=bin_size
# )
# bin_size = 100
# context.plot(
#     df=dummy_df,
#     x="year",
#     y="dummy_time_series",
#     x_label="year",
#     y_label="dummy time series",
#     title=f"Dummy data to show scaling of x-axis with bin size {bin_size}",
#     bin_size=bin_size
# )

# print(data.stats)
# heaviest = data.stats.drop_duplicates(subset=["Player"]).sort_values("weight", ascending=False)[:10][["Player", "weight"]]
# context.strategy = BarPlotter()
# context.plot(
#     heaviest,
#     x="Player",
#     y="weight",
#     x_label="Player",
#     y_label="Weight",
#     title="Top 10 heaviest players in NBA"
# )

# print(data.stats.drop_duplicates(subset=["Player"]).dropna().sort_values("PTS", ascending=False).head(50))
# MJ = data.select_rows("stats", "Player", "Michael Jordan", "==")
# MJ_sorted = MJ.sort_values("Year")
# print(MJ_sorted)
# context.strategy = LinePlotter()
# from pprint import pprint
# print("int" in str(MJ_sorted["Year"].dtype))
# context.plot(
#     MJ_sorted,
#     x="Year",
#     y="PTS",
#     x_label="Year",
#     y_label="Points scored",
#     title="Points scored by Michael Jordan"
# )
# v.strategy = s
# v.plot(df, x="a", y="b", x_label="values of b", y_label="values of a", title="Diagram")
#
# v.strategy = ScatterPlotter()
# v.plot(df, x="a", y="b", x_label="values of b", y_label="values of a", title="Diagram")
#
# v.strategy = BarPlotter()
# v.plot(df, x="a", y="b", x_label="values of b", y_label="values of a", title="Diagram")

